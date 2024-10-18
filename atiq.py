import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia

# Initialize recognizer and text-to-speech engine
listener = aa.Recognizer()
machine = pyttsx3.init()

def talk(text):
    """Convert text to speech and speak it."""
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    """Listen for voice input and recognize commands."""
    global instruction
    try:
        with aa.Microphone() as origin:
            print("Listening...")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)  # Capture the speech
            print(f"User said: {instruction}")  # Debugging print to show what was heard
            instruction = instruction.lower()
    except aa.UnknownValueError:
        print("Sorry, I did not understand that.")
        instruction = ""
    except aa.RequestError:
        print("Sorry, my speech service is down.")
        instruction = ""
    
    return instruction

def play_atiq():
    """Process commands and perform actions based on the instruction."""
    instruction = input_instruction()  # Get user's input
    
    if instruction == "":
        talk("Sorry, I didn't catch that.")
    elif "play" in instruction:
        song = instruction.replace("play", "")
        talk("Playing " + song)
        pywhatkit.playonyt(song)

    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d/%m/%Y')
        talk("Today's date is " + date)

    elif 'how are you' in instruction:
        talk('I am fine, how about you?')

    elif 'what is your name' in instruction:
        talk('I am Atiq. What can I do for you?')

    elif 'who is' in instruction:
        human = instruction.replace('who is', " ")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)

    else: 
        talk('Please repeat that.')

# Start the virtual assistant
play_atiq()
