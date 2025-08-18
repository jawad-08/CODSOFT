# Task 01 — Chatbot with Rule-Based Responses

This is my first task for the **CodSoft Artificial Intelligence Internship (Batch B46)**.  
It is a simple **rule-based chatbot** built in Python that responds using handcrafted regex rules and a small scoring system.

---

## 📌 Description
A **rule-based chatbot** works by matching user input against predefined patterns and giving a response if a rule is matched.  
In this implementation:
- Each **rule** has an intent, regex patterns, and possible responses (or a dynamic action).
- The chatbot **scores matches** and picks the best response.
- If nothing matches, it falls back to a default reply.
- The bot runs in the **terminal (CLI)** and supports greetings, small talk, date/time queries, and farewells.

---

## 📂 Project Structure
tasks/task_01/
├── README.md
├── requirements.txt
├── src/
│ ├── init.py
│ ├── rules.py # intent rules & responses
│ ├── utils.py # text normalization
│ ├── chatbot.py # chatbot engine
│ └── cli.py # interactive CLI
├── tests/
│ └── test_chatbot.py
├── data/
│ └── (optional patterns.json later)
└── notebooks/
└── (optional demo notebook later)


## ⚙️ Setup Instructions

1. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   
Windows (PowerShell)

```bash
.\.venv\Scripts\Activate.ps1
```
macOS/Linux
```bash
source .venv/bin/activate
```

2. Install dependencies

```bash
pip install -r tasks/task_01/requirements.txt
```

▶️ Running the Chatbot
From the repo root:

```bash

python -m tasks.task_01.src.cli
```

Example Run
```
Rule Bot 🤖 — type 'help' for ideas, 'exit' to quit.
you> hello
bot> Hello! What would you like to know?  (intent=greet, conf=0.67)

you> what time is it
bot> It’s 16:02:11.  (intent=time, conf=0.67)

you> bye
bot> See you around! 👋  (intent=bye, conf=0.67)
To quit: type exit or press Ctrl+C.
```

🧪 Running Tests
This project includes simple unit tests to verify responses.

```bash

python -m pytest tasks/task_01/tests/ -q
```
Expected output:
```
...                                                                 [100%]
3 passed in 0.15s
```

✨ Adding New Rules
You can extend the chatbot by adding new intents.

Open src/rules.py

Add a new Rule object:

```python

Rule(
    intent="weather",
    patterns=[r"\b(weather|forecast)\b"],
    responses=["I can't fetch live weather, but it's always sunny in code ☀️"],
    priority=1,
)
```

Save and re-run the chatbot:
```
you> weather
bot> I can't fetch live weather, but it's always sunny in code ☀️
```
