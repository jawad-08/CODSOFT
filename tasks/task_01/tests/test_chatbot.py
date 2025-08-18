from tasks.task_01.src.chatbot import Chatbot  

def test_greeting():
    bot = Chatbot()
    r = bot.respond("hello")
    assert r.intent == "greet"

def test_bye():
    bot = Chatbot()
    r = bot.respond("bye")
    assert r.intent == "bye"

def test_fallback():
    bot = Chatbot()
    r = bot.respond("unrelated 12345")
    assert r.intent in {"fallback"}
