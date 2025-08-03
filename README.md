# AADI - AI Desktop Voice Assistant 🧠🎙️

AADI (Artificial Assistant Developed Intelligently) is your personal desktop voice assistant created in Python. It can perform various tasks like telling time and date, searching Wikipedia, opening websites and applications, managing files, telling jokes, taking screenshots, providing system info, and much more — all with your voice!

---

## 🛠️ Features

- 🎤 **Voice Recognition**: Talk to your computer via microphone.
- 📢 **Text-to-Speech**: Human-like vocal responses.
- 🕐 **Time & Date**: Know the current time and date.
- 🌐 **Open Websites**: Open YouTube, Google, Facebook, Instagram, etc.
- 📁 **File Management**: Create, rename, or delete files using voice.
- 📄 **Remember Things**: Ask AADI to remember and recall custom notes.
- 😂 **Jokes & Fun Facts**: Ask for jokes or random fun facts.
- 📰 **News Updates**: Opens Hindustan Times for latest headlines.
- 📸 **Screenshots**: Take screenshots and save them.
- 💻 **System Info**: Check CPU usage and available memory.
- 🧮 **Calculations**: Perform spoken mathematical calculations.
- 🎵 **Music Playback**: Play random music from your Music folder.
- 💻 **App Launcher**: Open VSCode, Chrome, Notepad, etc.
- 🔋 **Power Commands**: Shutdown, restart, or sleep your system.
- ❌ **Offline Mode**: Exit the assistant at any time with a command.

---

## 📦 Dependencies

Install these Python packages before running the assistant:

```bash
pip install pyttsx3 SpeechRecognition wikipedia pyautogui psutil
```

---
Note: You might also need to install pyaudio which can be tricky on some systems. You can try:

```bash
pip install pipwin
pipwin install pyaudio
```

---

## ▶️ How to Run

1. Clone this repository:
```bash
git clone https://github.com/yourusername/myai.git
cd myai
```
2. Make sure your microphone is working.
3. Run the script:
```bash
python myai.py
```
4. Speak your command after hearing the prompt.

---

## 📁 File Structure
```bash
aadi-voice-assistant/
│
├── myai.py              # Main Python script (your voice assistant)
├── screenshot.png       # Screenshot output file
├── README.md            # You're here!
```

---

## Voice Commands
```bash
Voice Commands	      
"What’s the time?" - Tells the current system time
"Open YouTube"     - Opens YouTube in browser
"Create file"      - Creates a new file
"Tell me a joke"   - Tells a random joke
"Shutdown"         - Shuts down the system
```

---

## 🧑‍💻 Created By

Harshada Patil 

Feel free to fork or contribute to this project!
