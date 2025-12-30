from Brain.AiBrain import ReplyBrain
from Body.Listen import MicExecution
from Body.Speak import Speak
from Body.Listen import Listen

from Features.INTRO import play_gif
play_gif

for i in range(3):
    Speak("Enter Password to Open Jarvis")
    a = input("Enter Password to Open Jarvis- ")
    pw_file = open("DataBase\\password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME BACK SIR")
       #Speak("WELCOME BACK SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME")
        from Features.GreetMe import greetMe
        greetMe()
        break
    elif (i==2 and a!=pw):
        exit()
    elif (a!=pw):
        print("Try Again")
        Speak("WrongPassword Try Again")

import datetime
import pyautogui
import pywhatkit
import webbrowser
from numpy import tile
import os
import random
from plyer import notification
from pygame import mixer
import speedtest
from time import sleep

def alarm(query):
    timehere = open("DataBase\\Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

def MainExecution():
    while True:
       
        Data = MicExecution()
        Data = str(Data)
        queryLen = len(Data)
        if int(queryLen)<3:
         pass
        
        #elif "what is" in Data or "why" in Data or "how" in Data:
             #Reply = QuestionReplyer(Data)

        elif "go to sleep" in Data:
                    Speak("Ok sir , You can call me anytime")
                    break 


        elif "change password" in Data:
                    Speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("DataBase\\password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    Speak("Done sir")
                    Speak(f"Your new password is{new_pw}")

        elif "schedule my day" in Data:
                    tasks = [] 
                    Speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    Data = Listen().lower()
                    if "yes" in Data:
                        file = open("DataBase\\tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("DataBase\\tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in Data:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("DataBase\\tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

        elif "show my schedule" in Data:
                    file = open("DataBase\\tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("Contents\\notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                    )

        elif "focus mode" in Data:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a==1):
                        Speak("Entering the focus mode....")
                        os.startfile("C:\\Users\\harsh\\Desktop\\Jarvis 3\\Features\\FocusMode.py")
                        exit()        
                    else:
                        pass

        elif "show my focus" in Data:
                    from Features.FocusGraph import focus_graph
                    focus_graph()

        elif "translate" in Data:
                    from Features.Translator import translategl
                    Data = Data.replace("jarvis","")
                    Data = Data.replace("translate","")
                    Data = Data.replace("karna","")
                    translategl(Data)

        elif "open" in Data:
                    from Features.Dictapp import openappweb
                    openappweb(Data)
        elif "close" in Data:
                    from Features.Dictapp import closeappweb
                    closeappweb(Data)

        elif "open" in Data:   
                    Data = Data.replace("open","")
                    Data = Data.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(Data)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")                       
                     
        elif "internet speed" in Data:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576        
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    Speak(f"Wifi download speed is {download_net}")
                    Speak(f"Wifi Upload speed is {upload_net}")
                    

        elif "ipl score" in Data:
                    from plyer import notification 
                    import requests 
                    from bs4 import BeautifulSoup 
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                        title = "IPL SCORE :- ",
                        message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout = 15
                    )
                
        elif "play a game" in Data:
                    from Features.game import game_play
                    game_play()

        elif "screenshot" in Data:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")
            

        elif "click my photo" in Data:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    Speak("SMILE")
                    pyautogui.press("enter")



        elif "tired" in Data:
                    Speak("Playing your Favourite songs, sir" )
                    a = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://youtu.be/h8m5T-9zJuc")
                    elif b==2:
                        webbrowser.open("https://youtu.be/1m6en0SQNFs")
                    elif b==3:
                        webbrowser.open("https://youtu.be/H5v3kku4y6Q")
                    elif b==4:
                        webbrowser.open("https://youtu.be/SlPhMPnQ58k")
                    elif b==5:
                        webbrowser.open("https://youtu.be/FgS1b2nU8AQ")
                    elif b==6:
                        webbrowser.open("https://youtu.be/_kqQDCxRCzM")
                    elif b==7:
                        webbrowser.open("https://youtu.be/UpsKGvPjAgw")
                    elif b==8:
                        webbrowser.open("https://youtu.be/nYh-n7EOtMA")
                    elif b==9:
                        webbrowser.open("https://youtu.be/JGwWNGJdvx8")
                    elif b==10:
                        webbrowser.open("https://youtu.be/aJOTlE1K90k")


        elif "google" in Data:
                    from Features.SearchNow import searchGoogle
                    searchGoogle(Data)
        elif "youtube" in Data:
                    from Features.SearchNow import searchYoutube
                    searchYoutube(Data)
        elif "wikipedia" in Data:
                    from Features.SearchNow import searchWikipedia
                    searchWikipedia(Data)

        elif "music" in Data:
                from Features.Music import searchMusic
                searchMusic(Data)


        elif "pause video" in Data:
                    pyautogui.press("k")
                    Speak("video paused")
        elif "play video" in Data:
                    pyautogui.press("k")
                    Speak("video played")
        elif "mute" in Data:
                    pyautogui.press("m")
                    Speak("video muted")
        elif "full screen" in Data:
                    pyautogui.press("f")
                    Speak("Screen Adjusted to best-fit")
        elif "exit full screen" in Data:
                    pyautogui.press("f")
     

        elif "volume up" in Data:
                    from Features.keyboard import volumeup
                    Speak("Turning volume up,sir")
                    volumeup()
        elif "volume down" in Data:
                    from Features.keyboard import volumedown
                    Speak("Turning volume down, sir")
                    volumedown()

                
        elif "news" in Data:
                    from Features.NewsRead import latestnews
                    latestnews()

        elif "calculate" in Data:
                    from Features.Calculatenumbers import WolfRamAlpha
                    from Features.Calculatenumbers import Calc
                    Data = Data.replace("calculate","")
                    Data = Data.replace("jarvis","")
                    Calc(Data)

        elif "whatsapp" in Data:
                    from Features.Whatsapp import sendMessage
                    sendMessage()

        elif "temperature" in Data:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    Speak(f"current{search} is {temp}")
        elif "weather" in Data:
                    search = "temperature in seoni"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    Speak(f"current{search} is {temp}")

        elif "set an alarm" in Data:
                    print("input time example:- 10 and 10 and 10")
                    Speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    Speak("Done,sir")
                           
        elif "the time" in Data:                                 #notification.mp3
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    Speak(f"Sir, the time is {strTime}")
        elif "finally sleep" in Data:
                    Speak("Going to sleep,sir")
                    exit()

        elif "remember that" in Data:
                    rememberMessage = Data.replace("remember that","")
                    rememberMessage = Data.replace("jarvis","")
                    Speak("You told me to remember that" + rememberMessage)
                    remember = open("DataBase\\Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
        elif "what do you remember" in Data:
                    remember = open("DataBase\\Remember.txt","r")
                    Speak("You told me to remember that" + remember.read())

        elif "shutdown system" in Data:
                    Speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break

       
        else:      
             Reply = ReplyBrain(Data)
             Speak(Reply)

MainExecution()



                


