### utils.py
import datetime
import platform
import random
import psutil
import geocoder
import webbrowser
import os
from timezonefinder import TimezoneFinder

def get_system_info():
    uname_info = platform.uname()
    return f"System: {uname_info.system}, {uname_info.release}. CPU: {psutil.cpu_percent()}%. RAM: {psutil.virtual_memory().percent}%"

def get_location():
    g = geocoder.ip("me")
    return f"You are in {g.city}, {g.country}." if g.city else "Couldn't detect location."

def get_time():
    g = geocoder.ip("me")
    latitude, longitude = g.latlng if g.latlng else (None, None)
    timezone = TimezoneFinder().timezone_at(lng=longitude, lat=latitude) if latitude else None
    return datetime.datetime.now().strftime("%I:%M %p") if timezone else "Couldn't determine time."

def play_music(song_name=None):
    url = "https://open.spotify.com/"
    if song_name:
        url += f"search/{song_name.replace(' ', '%20')}"
    webbrowser.open(url)
    return f"Playing {song_name if song_name else 'song'} on Spotify."

def set_alarm(time):
    os.system(f"start /b explorer shell:AppsFolder\Microsoft.WindowsAlarms_8wekyb3d8bbwe!App")
    return f"Alarm set for {time}."

def chat():
    responses = ["Let's have fun! Tell me a joke first!", "I think we should start a debate!", "How about a fun fact?", "Wanna hear a riddle?"]
    return random.choice(responses)

def make_call(contact):
    os.system(f"start phone://call/{contact}")
    return f"Calling {contact} through Phone Link."
