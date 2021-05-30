import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

 
import datetime

engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
  
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir.  Please tell me how may I help you")          

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try :
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        speak("Say that again please...")
        return "None" #None string will be returned
    return query



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kublaykumar1@gmail.com', 'goluverma@123')
    server.sendmail('kublaykumar1@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'G:\mm'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))    
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'about sathyabama' in query:
            speak("According to Wikipedia............Sathyabama Institute of Science and Technology (SIST), formerly Sathyabama University, is a Christian higher education deemed to be university institute, situated at Chennai, Tamil Nadu, India]. It was founded in 1987 as Sathyabama Engineering College by Jeppiaar and received its deemed to be university status in 2001")
             
        elif 'open code' in query:
           
            
            codePath = "C:\\Users\\SURBHI\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code.exe"
            os.startfile(codePath)
        elif 'email to golu' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "kublay1999@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")        








