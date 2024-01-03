import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os 
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
   
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>= 0 and hour<12:
            speak("GOOD MORNING!")
        
        elif hour>=12 and hour<18:
            speak("GOOD AFTERNOON!")

        else:
            speak("GOOD EVENING!")

        speak("I am JARVIS,Please tell me how may I help you")
    
def takeCommand():
        # it takes microphone input from the user and return string output

        r = sr.Recognizer()
        with sr.Microphone() as Source:
            print("listening..")
            r.pause_threshold = 1
            audio = r.listen(Source)

        try:
            print("Recognizing..")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said:{query}\n")
        except Exception as e:
             #print(e)
            print("say that again please..") 
            return "None"
        return query

def sendEmail(to, content):
     server = smtplib.SMTP('smtp.gmail.com', 587)
     server.ehlo()
     server.starttls()
     server.login('janu27113@gmail.com', 'N@RAY@N279')
     server.sendmail('janu27113@gmail.com', to,content)
     server.close()

if __name__=="__main__":  
    wishMe()
    while True:
    
        query = takeCommand().lower()

        if 'wikipedia' in query:
             speak('searching wikipedia...')
             query = query.replace("wikipedia","")
             results = wikipedia.summary(query, sentences=2)
             speak("According to wikipedia")
             print(results)
             speak(results)
             
        elif 'open youtube' in query:
             webbrowser.open("youtube.com")

        elif 'open google' in query:
             webbrowser.open("google.com")    

        elif 'open chatgpt' in query:
             webbrowser.open("openai.com")      

        elif 'play music' in query:
             music_dir= 'D:\\music'
             songs = os.listdir(music_dir)
             print(songs)
             os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"the time is {strTime}")

        elif 'open code' in query:
             codepath = "C:\\Users\\janhavi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"    
             os.startfile(codepath)

        elif  'email to janhavi' in query:
            try:
                  speak("what should i say?") 
                  content = takeCommand()
                  to = "janu27113@gmail.com"
                  sendEmail(to, content) 
                  speak("Email has been sent!")
            except Exception as e:
                 print(e)
                 speak("I am unable to send your email at the moment.")