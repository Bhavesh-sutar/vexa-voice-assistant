# 🤖 AI: Your Personal Voice Assistant

A Python-based voice assistant that can interact with you, launch apps, take notes, tell jokes, and more — all using your voice commands!

---

## 🚀 Features

- 🎙️ Voice command recognition
- 🗂️ Launch desktop applications (e.g., Notepad, Chrome, VS Code)
- 📓 Save and read voice notes
- 🌐 Open websites via voice
- 😂 Tell you random jokes
- 🕒 Give you current time and date

---

## 📁 Project Structure

ai/
├── main.py # Main script to run the assistant
├── .env
├── requirements.txt # List of all required Python packages
├── README.md

├── core/ # Core functionality
│ ├── listener.py # Handles voice input
│ ├── processor.py # Processes the spoken command
│ ├── speaker.py # Text-to-speech output

├── features/ # All feature-specific modules
│ ├── get_datetime.py # Tells current date/time
│ ├── launch_apps.py # Launches apps like Chrome, Notepad, etc.
│ ├── notes.py # Saves and reads voice notes
│ ├── open_web.py # Opens websites
│ ├── tell_joke.py

---

## 🛠️ Installation

```bash
git clone https://github.com/bhavesh-sutar/ai.git
cd Bhavesh-ai
pip install -r requirements.txt
python main.py
```

##📫 Contact
Developed by Bhavesh
Feel free to contribute or raise issues to improve this assistant!
