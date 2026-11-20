
import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
from urllib.parse import quote_plus
import threading


# Text-to-Speech Setup
engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

running = False
engine_lock = threading.Lock()


def speak(text):
    root.after(0, lambda: add_message("Assistant", text))

    with engine_lock:
        engine.say(text)
        engine.runAndWait()


def add_message(sender, message):
    chat_box.config(state="normal")
    chat_box.insert(tk.END, f"{sender}: {message}\n\n")
    chat_box.see(tk.END)
    chat_box.config(state="disabled")


def update_status(message):
    root.after(0, lambda: status_label.config(text=message))


def listen():
    recognizer = sr.Recognizer()
    recognizer.operation_timeout = 10

    try:
        with sr.Microphone() as source:
            update_status("Listening... Speak now!")
            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

            update_status("Recognizing your voice...")
            text = recognizer.recognize_google(audio)

            root.after(0, lambda: add_message("You", text))
            return text.lower()

    except sr.WaitTimeoutError:
        speak("I could not hear you. Please try again.")

    except sr.UnknownValueError:
        speak("Sorry, I could not understand. Please repeat.")

    except sr.RequestError:
        speak("Speech recognition service is unavailable.")

    except OSError:
        speak("Please check your microphone.")

    except Exception as error:
        print("Unexpected error:", error)
        speak("Something went wrong.")

    return None


def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak("The current time is " + current_time)


def tell_date():
    current_date = datetime.datetime.now().strftime("%d %B %Y")
    speak("Today's date is " + current_date)


def google_search(query):
    search_url = "https://www.google.com/search?q=" + quote_plus(query)
    webbrowser.open(search_url)
    speak("Here are the search results for " + query)


def process_command(command):
    global running

    if command is None:
        return

    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        tell_time()

    elif "date" in command:
        tell_date()

    elif command.startswith("search"):
        query = command.replace("search", "", 1).strip()

        if query:
            google_search(query)
        else:
            speak("Please tell me what you want to search.")

    elif "exit" in command or "stop" in command:
        speak("Goodbye! Have a nice day.")
        running = False
        update_status("Assistant stopped.")

    else:
        speak("Sorry, I do not know that command yet.")


def voice_loop():
    global running

    while running:
        command = listen()

        if running and command:
            process_command(command)

    root.after(0, lambda: start_button.config(state="normal"))
    root.after(0, lambda: stop_button.config(state="disabled"))


def start_assistant():
    global running

    if running:
        return

    running = True
    start_button.config(state="disabled")
    stop_button.config(state="normal")

    speak("Hello! Welcome to your Python Voice Assistant.")

    threading.Thread(
        target=voice_loop,
        daemon=True
    ).start()


def stop_assistant():
    global running

    running = False
    update_status("Stopping assistant...")
    speak("Assistant stopped.")


def close_app():
    global running
    running = False
    root.destroy()


# GUI Window
root = tk.Tk()
root.title("Python Voice Assistant")
root.geometry("650x650")
root.resizable(False, False)
root.configure(bg="#14243B")

# Title
tk.Label(
    root,
    text="PYTHON VOICE ASSISTANT",
    font=("Arial", 21, "bold"),
    bg="#14243B",
    fg="white"
).pack(pady=(25, 8))

tk.Label(
    root,
    text="Your personal desktop voice assistant",
    font=("Arial", 10),
    bg="#14243B",
    fg="#CBD5E1"
).pack()

# Status
status_label = tk.Label(
    root,
    text="Status: Ready",
    font=("Arial", 11, "bold"),
    bg="#14243B",
    fg="#22C55E"
)
status_label.pack(pady=15)

# Chat Area
chat_frame = tk.Frame(root, bg="#14243B")
chat_frame.pack(padx=25, fill="both", expand=True)

chat_box = tk.Text(
    chat_frame,
    font=("Arial", 11),
    bg="#263B55",
    fg="white",
    insertbackground="white",
    wrap="word",
    height=15,
    relief="flat",
    padx=12,
    pady=12
)
chat_box.pack(fill="both", expand=True)
chat_box.config(state="disabled")

# Buttons
button_frame = tk.Frame(root, bg="#14243B")
button_frame.pack(pady=22)

start_button = tk.Button(
    button_frame,
    text="START LISTENING",
    font=("Arial", 11, "bold"),
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    cursor="hand2",
    command=start_assistant
)
start_button.grid(row=0, column=0, padx=8, ipadx=12, ipady=10)

stop_button = tk.Button(
    button_frame,
    text="STOP ASSISTANT",
    font=("Arial", 11, "bold"),
    bg="#DC2626",
    fg="white",
    activebackground="#B91C1C",
    cursor="hand2",
    state="disabled",
    command=stop_assistant
)
stop_button.grid(row=0, column=1, padx=8, ipadx=12, ipady=10)

# Footer
tk.Label(
    root,
    text="Powered by Python | Speech Recognition | Pyttsx3",
    font=("Arial", 9),
    bg="#14243B",
    fg="#94A3B8"
).pack(side="bottom", pady=12)

root.protocol("WM_DELETE_WINDOW", close_app)
root.mainloop()
