import re
from typing import Callable, List, Optional, Sequence

class Rule:
    """
    A simple rule = (intent, regex patterns, responses | action).
    If action is provided, it is used to generate the reply dynamically.
    """
    def __init__(
        self,
        intent: str,
        patterns: Sequence[str],
        responses: Optional[Sequence[str]] = None,
        priority: int = 0,
        action: Optional[Callable[[str], str]] = None,
    ) -> None:
        self.intent = intent
        self.compiled = [re.compile(pat, re.IGNORECASE) for pat in patterns]
        self.responses = list(responses) if responses else []
        self.priority = priority
        self.action = action

    def score(self, text: str) -> int:
        """Return how many patterns match; higher = better."""
        return sum(1 for rx in self.compiled if rx.search(text))

    def generate(self, text: str) -> str:
        import random
        if self.action:
            return self.action(text)
        if not self.responses:
            return "I have a rule for this, but no response is defined."
        return random.choice(self.responses)


# Example dynamic actions
def action_time(_: str) -> str:
    from datetime import datetime
    return f"It’s {datetime.now().strftime('%H:%M:%S')}."

def action_date(_: str) -> str:
    from datetime import date
    return f"Today is {date.today().isoformat()}."

# A small, original rule-set. Add/modify freely (that keeps your work unique).
DEFAULT_RULES: List[Rule] = [
    Rule(
        intent="greet",
        patterns=[r"\b(hi|hello|hey|namaste|hola)\b"],
        responses=[
            "Hey there! How can I help today?",
            "Hello! What would you like to know?",
            "Hi! Ask me anything about this demo.",
        ],
        priority=3,
    ),
    Rule(
        intent="how_are_you",
        patterns=[r"\bhow (are|r) (you|u)\b", r"\bwhat's up\b", r"\bhow's it going\b"],
        responses=[
            "Doing great and ready to chat!",
            "All good here — thanks for asking.",
        ],
        priority=1,
    ),
    Rule(
        intent="name",
        patterns=[r"\b(what('?| i)s your name|who are you)\b"],
        responses=[
            "I’m a tiny rule-based chatbot built for the CodSoft task.",
            "I don’t have a fancy name yet — I’m your rule bot 🤖.",
        ],
        priority=2,
    ),
    Rule(
        intent="help",
        patterns=[r"\bhelp\b", r"\bwhat can you do\b"],
        responses=[
            "I can greet, tell the time/date, answer small talk, and say goodbye. Try: 'time', 'date', 'bye'.",
        ],
        priority=2,
    ),
    Rule(
        intent="time",
        patterns=[r"\b(time|current time|what time)\b"],
        action=action_time,
        priority=2,
    ),
    Rule(
        intent="date",
        patterns=[r"\b(date|today'?s? date)\b"],
        action=action_date,
        priority=2,
    ),
    Rule(
        intent="thanks",
        patterns=[r"\b(thanks|thank you|thx|tysm)\b"],
        responses=["You’re welcome!", "Happy to help!"],
        priority=1,
    ),
    Rule(
        intent="bye",
        patterns=[r"\b(bye|goodbye|see (ya|you)|ciao)\b"],
        responses=["Bye! Have a great day.", "See you around! 👋"],
        priority=3,
    ),
]
