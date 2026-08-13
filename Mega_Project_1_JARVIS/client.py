import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)

voices = engine.getProperty("voices")

print("Available voices:")

for i, voice in enumerate(voices):
    print(i, voice.name, voice.id)

print("Testing voice...")

engine.say("Yes sir")
engine.runAndWait()

engine.say("Initializing Jarvis")
engine.runAndWait()

engine.say("Opening Google")
engine.runAndWait()

print("Finished")