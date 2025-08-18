from dataclasses import dataclass
from typing import List, Tuple
from .rules import Rule, DEFAULT_RULES
from .utils import normalize

@dataclass
class MatchResult:
    intent: str
    confidence: float
    response: str

class Chatbot:
    """
    A tiny rule engine:
      - normalize the user text
      - score each rule (#regex matches + a tiny boost for priority)
      - choose the highest score (tie -> higher priority wins)
    """
    def __init__(self, rules: List[Rule] | None = None) -> None:
        self.rules = rules or DEFAULT_RULES
        self.fallbacks = [
            "Hmm, I’m not sure about that.",
            "I didn’t catch that — try 'help' to see examples.",
            "I don’t have a rule for this yet.",
        ]

    def _rank(self, text: str) -> List[Tuple[Rule, float]]:
        scores: List[Tuple[Rule, float]] = []
        for rule in self.rules:
            s = rule.score(text)
            if s > 0:
                # small deterministic boost from priority to break ties
                scores.append((rule, s + rule.priority * 0.01))
        # highest score first
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores

    def respond(self, user_text: str) -> MatchResult:
        cleaned = normalize(user_text)
        ranked = self._rank(cleaned)
        if not ranked:
            # basic fallback
            return MatchResult("fallback", 0.0, self.fallbacks[0])

        best_rule, score = ranked[0]
        # Convert rough score to 0..1 range for display
        max_possible = 3.0  # heuristic; adjust if you add many patterns/rules
        confidence = min(score / max_possible, 1.0)
        reply = best_rule.generate(cleaned)
        return MatchResult(best_rule.intent, confidence, reply)
