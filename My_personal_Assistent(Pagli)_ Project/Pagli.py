import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning Paritosh!")
        speak("Good Morning Paritosh!")


    elif hour>=12 and hour<18:
        print("Good Afternoon Paritosh!")
        speak("Good Afternoon Paritosh!")   

    else:
        print("Good Evening Paritosh!")  
        speak("Good Evening Paritosh!")    


    print("I am your personal assistent sir. Please tell me how may I help you.......") 
    speak("I am your personal assistent sir. Please tell me how may I help you")   


def takeCommand():
    # It take microphone input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing.......")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said --> {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please......")
        return "None"

    return query


# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('paritoshpuitta@gmail.com', 'pasword*****')
#     server.sendmail('paritoshpuitta@gmail.com', to, content)
#     server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for exucating task based on query
        if 'wikipedia' in query:
            speak("Searching from wikipedia......")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif 'can you hear' in query:
            print("Yes Sir I can hear you! Please tell me how can I help you!")
            speak("Yes Sir I can hear you! Please tell me how can I help you!")

        elif 'thank you' in query:
            print("You are most welcome sir.......")
            speak("You are most welcome sir.......")

        elif 'your name' in query:
            print("My name is Pagli! And I am your personal assistent Sir!....")
            speak("My name is Paggli! And I am your personal assistent Sir!")

        
        elif 'pagali' in query:
            print("Yes Sir.......   Please tell me how can I help you!")
            speak("Yes Sir!.....   Please tell me how can I help you!......")

        elif 'name' in query:
            print("Thank you Sir.......  ")
            speak("Thank you Sir!.....   ")


        elif 'who are you' in query:
            print("My name is Pagli! And I am your personal assistent Sir!.....")
            speak("My name is Paggli! And I am your personal assistent Sir!")




        elif 'open youtube' in query:
            speak("Ok Sir!....")
            print("Ok Sir!....")
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            speak("Ok Sir!....")
            print("Ok Sir!....")
            webbrowser.open("google.com")

        # elif 'play music' in query:
        #     music_dir = 'E:\\Python Course with Notes\\1. Chapter 1'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[7]))
        
        elif 'feeling romantic' in query:
            speak("Ok Sir!....   I found a romantic song.......")
            print("Ok Sir!....  I found a romantic song.......")
            music_dir = 'E:\\Python Course with Notes\\1. Chapter 1'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[6]))
        elif 'play music' in query:
            print("What songs would you like to hear sir.......")
            speak("What songs would you like to hear sir.......")
        elif 'play a music' in query:
            print("What songs would you like to hear sir.......")
            speak("What songs would you like to hear sir.......")
        elif 'mood off' in query:
            speak("Ok Sir!....")
            print("Ok Sir!....")
            music_dir = 'E:\\Python Course with Notes\\1. Chapter 1'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[9]))
        elif 'as your wish' in query:
            speak("Ok Sir!....")
            print("Ok Sir!....")
            music_dir = 'E:\\Python Course with Notes\\1. Chapter 1'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[7]))    
        elif 'romantic song' in query:
            speak("Ok Sir!....")
            print("Ok Sir!....")
            music_dir = 'E:\\Python Course with Notes\\1. Chapter 1'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[8]))
        elif 'broken' in query:
            speak("Ok Sir!....")
            print("Ok Sir!....")
            music_dir = 'E:\\Python Course with Notes\\1. Chapter 1'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[5]))
        

        elif 'the time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           print(f"Sir, the time is {strTime}")
           speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            speak("Ok Sir!....")
            print("Ok Sir!....")
            codePath = "C:\\Users\\Paritosh Barman\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        

        # elif 'send email' in query:
        #    try:
        #        speak("What should I say?")
        #        content = takeCommand()
        #        to = "barmanpari163@gmail.com"
        #        sendEmail(to, content)
        #        speak("Email has been send!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry my frind Paritosh bhai. I am not able to send this mail")


        elif 'sleep' in query:
            print("Ok sir!.... I fell aseep!  Goog night Sir......Have a sweet dreams........")
            speak("Ok sir!.... I fell aseep!  Goog night Sir......Have a sweet dreams........")

            exit()
        elif 'asleep' in query:
            print("Ok sir!.... I fell aseep!  Goog night Sir......Have a sweet dreams........")
            speak("Ok sir!.... I fell aseep!  Goog night Sir......Have a sweet dreams........")

            exit()
            
        elif 'pagli' in query:
            print("Yes Sir.......   Please tell me how can I help you!")
            speak("Yes Sir!.....   Please tell me how can I help you!......")
