### main.py
from speech import initialize_tts, speak, listen
from api_handler import query_huggingface, get_weather, get_news, search_wikipedia
from app_manager import open_application
from intent_recognition import understand_query
from utils import get_system_info, get_location, get_time, play_music, set_alarm, chat, make_call

def handle_command(command, engine):
    intent = understand_query(command)
    if intent == "location":
        speak(get_location(), engine)
    elif intent == "time":
        speak(get_time(), engine)
    elif intent == "weather":
        speak("Which city's weather would you like to know?", engine)
        location = listen()
        speak(get_weather(location) if location else "Couldn't get location.", engine)
    elif intent == "open_app":
        open_application(command.replace("open", "").strip())
    elif intent == "news":
        speak(get_news(), engine)
    elif intent == "play_music":
        song_name = command.replace("play music", "").strip()
        speak(play_music(song_name if song_name else None), engine)
    elif intent == "set_alarm":
        time = command.replace("set alarm for", "").strip()
        speak(set_alarm(time), engine)
    elif intent == "chat":
        speak(chat(), engine)
    elif intent == "call":
        contact = command.replace("call", "").strip()
        speak(make_call(contact), engine)
    else:
        speak(search_wikipedia(command), engine)

def main():
    engine = initialize_tts()
    speak("Hi! I am LUNA. How can I help you today?", engine)
    while True:
        command = listen()
        if command:
            handle_command(command, engine)

if __name__ == "__main__":
    main()
