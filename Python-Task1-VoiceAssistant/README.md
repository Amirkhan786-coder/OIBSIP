# Python Voice Assistant

## OIBSIP – Python Programming Internship | Task 1

## 1. Project Overview

The Python Voice Assistant is a command-line voice assistant that listens to spoken commands through a microphone, recognizes speech, and responds using text-to-speech technology.

It can greet users, tell the current date and time, perform Google searches, and handle unrecognized speech.

## 2. Features

- Voice input through a microphone.
- Speech recognition using SpeechRecognition.
- Text-to-speech responses using pyttsx3.
- Greeting command.
- Current time announcement.
- Current date announcement.
- Google search through voice commands.
- Error handling for unrecognized speech.
- Microphone and network error handling.
- Exit command to close the assistant.

## 3. Technologies Used

- Python 3
- SpeechRecognition
- PyAudio
- pyttsx3
- datetime
- webbrowser

## 4. Project Structure

```text
Python-Task1-VoiceAssistant/
│
├── assistant.py
├── requirements.txt
├── README.md
│
└── screenshots/
    ├── 01_assistant_start.png
    ├── 02_hello_command.png
    ├── 03_time_command.png
    ├── 04_date_command.png
    ├── 05_google_search.png
    ├── 06_error_handling.png
    └── 07_exit_command.png
```

## 5. Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/Amirkhan786-coder/OIBSIP.git
```

### Step 2: Open the project folder

```bash
cd OIBSIP/Python-Task1-VoiceAssistant
```

### Step 3: Create a virtual environment

```bash
python -m venv venv
```

### Step 4: Activate the virtual environment (Windows)

```powershell
venv\Scripts\activate
```

### Step 5: Install dependencies

```bash
pip install -r requirements.txt
```

## 6. How to Run

Execute the following command:

```bash
python assistant.py
```

Allow microphone access if Windows asks for permission.

## 7. Available Voice Commands

| Voice Command | Expected Action |
|---|---|
| Hello | Gives a greeting |
| What is the time? | Announces the current time |
| Today's date | Announces the current date |
| Search Python programming | Opens Google search results |
| Exit | Closes the assistant |

## 8. Error Handling

The application handles common situations such as:

- Unrecognized speech.
- No speech detected.
- Speech recognition service errors.
- Network connection problems.
- Microphone errors.

The assistant asks the user to repeat when speech cannot be understood.

## 9. Screenshots

Project screenshots are available in the `screenshots/` directory.

They demonstrate application startup, voice commands, date and time responses, Google search, error handling, and program exit.

## 10. Privacy Considerations

The application captures microphone audio when the user activates listening. It uses Google's online speech recognition service through `recognize_google()` to convert speech into text. Therefore, recorded audio is sent to an external recognition service for processing.

The project does not intentionally save microphone recordings or maintain a persistent voice history. Users should avoid speaking passwords or other sensitive information.

## 11. Learning Outcomes

Through this project, I practiced:

- Python functions and control flow.
- Working with external Python libraries.
- Microphone input and speech recognition.
- Text-to-speech implementation.
- Date and time handling.
- Browser automation through webbrowser.
- Exception handling and debugging.

## 12. Internship Task

**Organization:** Oasis Infobyte

**Track:** Python Programming

**Task:** Task 1 – Voice Assistant

**Tier:** Beginner

**Developer:** Md Amir Khan

---

**Project Status:** Beginner-tier core features implemented and tested. Final documentation and submission preparation in progress.
