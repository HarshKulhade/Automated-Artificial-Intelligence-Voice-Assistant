# Automated Artificial Intelligence Voice Assistant — Jarvis

A modular Python-based **Daily-Needs Voice Assistant / Agent** that listens to your voice, understands commands, and automates tasks like searching the web, sending WhatsApp messages, reading news, controlling the keyboard, calculating numbers, translating text, playing music, and more.

> Designed with a clean “Brain / Body / Features” architecture so new features can be added easily.

---

## ✨ Features

Jarvis currently supports (based on the implemented modules):

- 👋 Greetings & introduction (`INTRO`, `GreetMe`)
- 🎧 Listen & speak via microphone + TTS (`Body.Listen`, `Body.Speak`)
- 🌐 Web search & quick answers (`SearchNow`)
- 📰 Read latest news (`NewsRead`)
- 🎵 Play music (`Music`)
- 🧮 Calculate numbers (`Calculatenumbers`)
- ⌨️ Keyboard automation / typing (`keyboard`)
- 📱 WhatsApp messaging (`Whatsapp`)
- 🗣️ Text translation (`Translator`)
- 📚 Dictionary / app lookup (`Dictapp`)
- 🕹️ Built-in mini-game (`game`)
- 🎯 Focus / productivity graph (`FocusGraph`)
- ⚡ System & automation helpers (pyautogui actions, reminders, etc.)

The assistant coordinates everything through `Brain.AiBrain.ReplyBrain`.

---

## 🗂️ Project Structure

Automated-Artificial-Intelligence-Voice-Assistant/
├─ Brain/ # Core intent logic & response engine
├─ Body/ # Input (Listen) & Output (Speak) pipeline
├─ Features/ # Feature modules (search, music, news, etc.)
├─ Contents/ # Static / UI / resource content
├─ Data/ # Assets, audio, temp data
├─ DataBase/ # Persistent state / user data
├─ Jarvis_main.py # MAIN entrypoint for the assistant
└─ data.mp3 # Sample audio asset

yaml
Copy code

---

## 🧩 Requirements

These packages are imported directly in `Jarvis_main.py`:

numpy
pyautogui
pywhatkit
webbrowser
pygame
plyer
requests
bs4
speedtest

css
Copy code

Likely runtime dependencies from `Body.Listen` / `Body.Speak` (commonly used in voice assistants):

SpeechRecognition
pyttsx3
pyaudio

pgsql
Copy code

> If you already have a `requirements.txt`, keep that as the source of truth.  
> Otherwise, you can generate one after install using `pip freeze > requirements.txt`.

---

## 🚀 Installation

1️⃣ **Clone the repository**

```bash
git clone https://github.com/HarshKulhade/Automated-Artificial-Intelligence-Voice-Assistant.git
cd Automated-Artificial-Intelligence-Voice-Assistant
2️⃣ Create a virtual environment (recommended)

bash
Copy code
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
3️⃣ Install dependencies

bash
Copy code
pip install -r requirements.txt
# or, if not present:
pip install numpy pyautogui pywhatkit webbrowser pygame plyer requests bs4 speedtest SpeechRecognition pyttsx3 pyaudio
On some systems you may need system packages for pyaudio / portaudio.

⚙️ Configuration
Some features may require additional setup:

WhatsApp automation → ensure WhatsApp Web is logged in

News / APIs → add keys if you enable external sources

Microphone selection → configure inside Body/Listen.py

TTS engine or voice settings → configured in Body/Speak.py

If you use API keys, prefer storing them in environment variables or .env:

bash
Copy code
export NEWS_API_KEY="..."
▶️ Usage
Run the assistant:

bash
Copy code
python Jarvis_main.py
Typical workflow:

Jarvis listens for your voice

You give a command (examples):

“Search about artificial intelligence”

“Play music”

“Send WhatsApp message”

“Read today’s news”

“Translate this sentence”

Jarvis processes the intent and executes the feature module

🧠 How It Works
Body → handles listening and speaking

Brain → interprets the text and chooses the correct action

Features → each capability is isolated as its own module

Jarvis_main.py → orchestrator / main event loop

This separation makes the project easy to extend — just add a new module in Features/ and connect it in Brain.

🛠️ Troubleshooting
❌ “No microphone / audio device”
Install pyaudio correctly and give mic permissions.

❌ Module import errors
Re-install dependencies or check requirements.txt.

❌ No speech output
Test pyttsx3 with a short script and verify speakers.

❌ WhatsApp automation not working
Keep browser open and logged into WhatsApp Web.

🗺️ Roadmap / Ideas
Add wake-word detection (Hey Jarvis)

Add conversation memory / context

Package as desktop app (.exe / AppImage)

Add GUI dashboard

Add plug-in system for new skills

🤝 Contributing
Contributions are welcome!
Feel free to open issues or submit PRs for new features or improvements.

📄 License
Add your preferred license in a LICENSE file (MIT recommended for open projects).

🙌 Credits
Built by Harsh Kulhade — a modular and extensible personal AI assistant project.
