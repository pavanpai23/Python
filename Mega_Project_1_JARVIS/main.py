import speech_recognition as sr
import webbrowser
import pyttsx3
import requests 

try:
    import musiclibrary
except ImportError:
    musiclibrary = None

recognizer=sr.Recognizer()
engin=None
newsapi="pub_1e260ab94a574c7eaeb857191813dee8"

def init_engine():
    global engin
    if engin is None:
        engin=pyttsx3.init()
        engin.setProperty("rate", 170)
    return engin

def speak(text):
    print(f"Jarvis: {text}")
    try:
        engine=init_engine()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Speech error: {e}")

def processcommand(c):
    command=c.lower().strip()

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif command.startswith("play "):
        if musiclibrary is None:
            speak("Music library is not available")
            return

        song=command.replace("play ", "", 1).strip()
        link=musiclibrary.music.get(song)
        if link is None:
            speak(f"I could not find {song} in the music library")
            return

        speak(f"Playing {song}")
        webbrowser.open(link)
    elif "news" in command:
        speak("Getting the latest news")
        response = requests.get(
            "https://newsdata.io/api/1/latest",
            params={"apikey": newsapi, "language": "en"},
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        articles=data.get("results", [])

        if not articles:
            speak("I could not find any news right now")
            return

        for article in articles[:5]:
            title=article.get("title")
            if title:
                speak(title)
    else:
        speak("Sorry, I did not understand that command")



if __name__=="__main__":
    speak("Initializing Jarvis....")
    while True:
            #listen for wake word jarvis
            #obtain audio from the microphone
        r = sr.Recognizer()
        
        # recognize speech using Sphinx
        print("recognizing")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source,timeout=5,phrase_time_limit=3)
            word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Yes, sir")
                # listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source,timeout=5,phrase_time_limit=5)
                    command=r.recognize_google(audio)
                    print(f"Command: {command}")

                    processcommand(command)

            else:
                print(f"Wake word ignored: {word}")

        except sr.WaitTimeoutError:
            print("Listening timed out")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            speak("Speech recognition service is not available")
            print("Recognition error; {0}".format(e))
        except Exception as e:
            speak("Something went wrong")
            print("Error; {0}".format(e))
            
