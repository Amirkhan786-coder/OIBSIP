
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
from urllib.parse import quote_plus

# Text-to-Speech Setup
engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


def speak(text):
    print("\nAssistant:", text)
    engine.say(text)
    engine.runAndWait()


# Voice Recognition
def listen():
    recognizer = sr.Recognizer()
    recognizer.operation_timeout = 10

    try:
        with sr.Microphone() as source:
            print("\nListening... Speak now!")
            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

            print("Recognizing your voice...")
            text = recognizer.recognize_google(audio)

            print("You:", text)
            return text.lower()

    except sr.WaitTimeoutError:
        speak("I could not hear you. Please try again.")
    except sr.UnknownValueError:
        speak("Sorry, I could not understand. Please repeat.")
    except sr.RequestError as error:
        print("Recognition service error:", error)
        speak("Speech recognition service is unavailable.")
    except OSError as error:
        print("Microphone error:", error)
        speak("Please check your microphone.")
    except Exception as error:
        print("Unexpected error:", error)
        speak("Something went wrong.")

    return None


# Current Time
def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak("The current time is " + current_time)


# Current Date
def tell_date():
    current_date = datetime.datetime.now().strftime("%d %B %Y")
    speak("Today's date is " + current_date)


# Google Search
def google_search(query):
    search_url = "https://www.google.com/search?q=" + quote_plus(query)
    webbrowser.open(search_url)
    speak("Here are the search results for " + query)


# Process Voice Commands
def process_command(command):

    if command is None:
        return True

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
        return False

    else:
        speak("Sorry, I do not know that command yet.")

    return True


# Main Program
def main():
    speak("Hello! Welcome to your Python Voice Assistant.")
    speak("You can say hello, time, date, search, or exit.")

    running = True

    while running:
        command = listen()
        running = process_command(command)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")
    finally:
        print("\nVoice Assistant closed.")
