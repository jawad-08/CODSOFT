from .chatbot import Chatbot

def chat_loop() -> None:
    print("Rule Bot 🤖 — type 'help' for ideas, 'exit' to quit.")
    bot = Chatbot()
    while True:
        try:
            user = input("you> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nbot> Bye!")
            break

        if user.lower() in {"exit", "quit", "q"}:
            print("bot> Bye!")
            break

        result = bot.respond(user)
        print(f"bot> {result.response}  (intent={result.intent}, conf={result.confidence:.2f})")

if __name__ == "__main__":
    chat_loop()
