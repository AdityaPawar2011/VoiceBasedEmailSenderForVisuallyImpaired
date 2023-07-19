import pyttsx3
import speech_recognition as sr
import smtplib
import datetime
Edict={"name1":"email1",
        "name2":"email2",
        "name3":"email3",
        "name4":"email4"
      }
engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    minute=int(datetime.datetime.now().minute)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else :
        speak("Good evening")
    speak ("I am voice based email sender, tell me the name of person")

def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")    
        name = r.recognize_google(audio, language='en-in')
        print(f"User: {name}\n")
    except Exception as e:
        print("Say that again please...")    
        return "None"
    return name

def sendemail(to,content):
    serwer= smtplib.SMTP('smtp.gmail.com',587)
    serwer.ehlo()
    serwer.starttls()
    serwer.login( 'j.a.r.v.i.s.020921@gmail.com','adityapawar2011')
    serwer.sendmail('j.a.r.v.i.s.020921@gmail.com', to,content)
    serwer.close()
if __name__ == "__main__":
    wishme()
    while True:
        try:
            name=Edict[takecommand().lower()]
            speak("okay what is the message")
            content=takecommand()
            print("Content: ",content)
            sendemail(name,content)
            speak("email is sent")
            break
        except Exception as e:
            print(e)
            speak("email is not sent, please resend it")