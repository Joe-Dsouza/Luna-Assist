import os
import subprocess

def open_application(app_name):
    app_name = app_name.lower()
    
    if "calculator" in app_name:
        os.system("calc" if os.name == "nt" else "gnome-calculator &")
    elif "notepad" in app_name or "editor" in app_name:
        os.system("notepad" if os.name == "nt" else "gedit &")
    elif "browser" in app_name or "chrome" in app_name:
        os.system("start chrome" if os.name == "nt" else "google-chrome &")
    elif "firefox" in app_name:
        os.system("start firefox" if os.name == "nt" else "firefox &")
    elif "edge" in app_name:
        os.system("start msedge" if os.name == "nt" else "microsoft-edge &")
    elif "word" in app_name:
        os.system("start winword" if os.name == "nt" else "libreoffice --writer &")
    elif "excel" in app_name:
        os.system("start excel" if os.name == "nt" else "libreoffice --calc &")
    elif "powerpoint" in app_name or "ppt" in app_name:
        os.system("start powerpnt" if os.name == "nt" else "libreoffice --impress &")
    elif "vlc" in app_name:
        os.system("start vlc" if os.name == "nt" else "vlc &")
    elif "spotify" in app_name:
        os.system("start spotify" if os.name == "nt" else "spotify &")
    elif "terminal" in app_name or "cmd" in app_name:
        os.system("start cmd" if os.name == "nt" else "gnome-terminal &")
    elif "task manager" in app_name:
        os.system("start taskmgr" if os.name == "nt" else "gnome-system-monitor &")
    elif "file explorer" in app_name or "explorer" in app_name:
        os.system("start explorer" if os.name == "nt" else "nautilus &")
    elif "paint" in app_name:
        os.system("start mspaint" if os.name == "nt" else "pinta &")
    elif "zoom" in app_name:
        os.system("start zoom" if os.name == "nt" else "zoom &")
    elif "telegram" in app_name:
        os.system("start telegram" if os.name == "nt" else "telegram-desktop &")
    elif "whatsapp" in app_name:
        os.system("start whatsapp" if os.name == "nt" else "whatsapp-desktop &")
    elif "discord" in app_name:
        os.system("start discord" if os.name == "nt" else "discord &")
    elif "obs" in app_name:
        os.system("start obs" if os.name == "nt" else "obs &")
    elif "visual studio code" in app_name or "vscode" in app_name:
        os.system("code" if os.name == "nt" else "code &")
    elif "android studio" in app_name:
        os.system("start studio64" if os.name == "nt" else "android-studio &")
    else:
        try:
            subprocess.run([app_name], shell=True)
        except Exception as e:
            print(f"Error opening application: {e}")
