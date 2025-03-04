### intent_recognition.py
import spacy
nlp = spacy.load("en_core_web_sm")

def understand_query(command):
    location_keywords = ["where am i", "find my location", "my location"]
    if any(keyword in command for keyword in location_keywords):
        return "location"
    if any(keyword in command for keyword in ["what time", "current time"]):
        return "time"
    if "weather" in command:
        return "weather"
    if "open" in command:
        return "open_app"
    if "news" in command:
        return "news"
    if "play music" in command or "play song" in command:
        return "play_music"
    if "set alarm" in command:
        return "set_alarm"
    if "chat" in command or "bored" in command:
        return "chat"
    if "call" in command:
        return "call"
    return "search"