import speech_recognition as sr
import webbrowser
import musiclibrary
import requests
import edge_tts
import asyncio
import os

recognizer = sr.Recognizer()

newsapi = "YOUR_API_KEY"


# =========================
# TEXT TO SPEECH
# =========================

def speak(text):

    print("Jarvis:", text)

    async def generate_voice():

        voice = "en-IN-PrabhatNeural"

        communicate = edge_tts.Communicate(
            text,
            voice
        )

        await communicate.save("jarvis.mp3")

    asyncio.run(generate_voice())

    os.startfile("jarvis.mp3")


# =========================
# PROCESS COMMAND
# =========================

def processcommand(c):

    c = c.lower()

    # Google
    if "open google" in c:

        speak("Yes sir, opening Google")

        webbrowser.open("https://google.com")


    # Facebook
    elif "open facebook" in c:

        speak("Yes sir, opening Facebook")

        webbrowser.open("https://facebook.com")


    # LinkedIn
    elif "open linkedin" in c:

        speak("Yes sir, opening LinkedIn")

        webbrowser.open("https://linkedin.com")


    # YouTube
    elif "open youtube" in c:

        speak("Yes sir, opening YouTube")

        webbrowser.open("https://youtube.com")


    # Play music
    elif c.startswith("play"):

        song = c.split(" ", 1)[1]

        if song in musiclibrary.music:

            speak("Yes sir, playing " + song)

            link = musiclibrary.music[song]

            webbrowser.open(link)

        else:

            speak("Sorry sir, I don't have that song")


    # News
    elif "news" in c:

        speak("Yes sir, fetching the latest news")

        url = f"https://newsdata.io/api/1/latest?apikey={newsapi}&language=en"

        response = requests.get(url)

        data = response.json()

        if "results" in data:

            for article in data["results"][:5]:

                title = article["title"]

                print(title)

                speak(title)

        else:

            speak("Sorry sir, I could not fetch the news")


    else:

        speak("Sorry sir, I don't understand that command")


# =========================
# MAIN PROGRAM
# =========================

if __name__ == "__main__":

    speak("Initializing Jarvis")

    while True:

        try:

            # Listen for Jarvis
            with sr.Microphone() as source:

                print("Listening for Jarvis...")

                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=3
                )

            word = recognizer.recognize_google(audio)

            print("You said:", word)


            # Wake word
            if "jarvis" in word.lower():

                speak("Yes sir, how can I help you?")


                # Listen for command
                with sr.Microphone() as source:

                    print("Jarvis Active...")

                    audio = recognizer.listen(source)

                    command = recognizer.recognize_google(audio)

                    print("Command:", command)

                    processcommand(command)


        except sr.WaitTimeoutError:

            print("Listening timed out")


        except sr.UnknownValueError:

            print("Sorry, I couldn't understand")


        except Exception as e:

            print("Error:", e)