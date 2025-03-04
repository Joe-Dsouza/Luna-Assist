# LUNA Assist - Voice AI Assistant

## 📌 Project Overview
LUNA Assist is a voice-controlled AI assistant that can:
- Recognize and process voice commands
- Play music on Spotify
- Set alarms using the Clock app
- Engage in fun interactive chat
- Call contacts using Phone Link
- Fetch the latest news, weather, and Wikipedia info
- Open applications and provide system details

The assistant has a **web interface** where a user can click a microphone button to start interacting with LUNA.

---

## 🛠️ Required Files
This project consists of the following files:

### **Backend (Python)**
1. `server.py` - Flask API to connect frontend and backend
2. `main.py` - The main assistant script
3. `speech.py` - Handles voice recognition and text-to-speech
4. `api_handler.py` - Handles API calls (weather, news, Wikipedia, etc.)
5. `app_manager.py` - Manages application opening and closing
6. `intent_recognition.py` - Uses NLP to recognize commands
7. `utils.py` - Contains helper functions for music, alarms, chat, and calls
8. `config.py` - Stores API keys and settings

### **Frontend (HTML/JavaScript)**
9. `userpage.html` - The user interface with a microphone button

---

## 🚀 Installation & Setup

### **1️⃣ Install Dependencies**
Ensure Python is installed, then install required modules:
```bash
pip install flask flask_cors pyttsx3 speechrecognition requests spacy wikipedia-api duckduckgo_search geocoder timezonefinder
```

Download the **English NLP model** for intent recognition:
```bash
python -m spacy download en_core_web_sm
```

### **2️⃣ Start the Backend**
Run the Flask server to handle API requests:
```bash
python server.py
```
This will start the backend at `http://127.0.0.1:5000`.

### **3️⃣ Open the Frontend**
Open `start.html` in a browser. Click the mic button to start interaction with LUNA.

---

## 🎤 How to Use
- Click the **mic button** to activate LUNA.
- Speak a command such as:
  - **"Play music"** → Opens Spotify and plays a random song.
  - **"Set alarm for 5 PM"** → Opens Clock app and sets an alarm.
  - **"Tell me a joke"** → Engages in fun chat.
  - **"Call John"** → Calls a contact via Phone Link.
  - **"What's the weather in New York?"** → Fetches weather data.

---

## 📌 Notes
- Initially it may take some time to start the process.
- Ensure your system microphone is enabled for voice recognition.
- For calling, Phone Link should be connected to your mobile device.
- LUNA will keep listening until the application is manually stopped.

---

![Screenshot 2025-03-02 150518](https://github.com/user-attachments/assets/39beef94-1681-46c1-bab7-e6b82c41aaaa)

---


- Developed by Josfer Dsouza


