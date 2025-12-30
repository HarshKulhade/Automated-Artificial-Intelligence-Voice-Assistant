from Body.Listen import MicExecution
from Body.Speak import Speak
import webbrowser
from time import sleep

Data = MicExecution()
Data = str(Data)

def searchMusic(Data):
    if "music" in Data:
        Speak("Ok Sir, Playing your Favourite Music!")
        web = "https://www.youtube.com/watch?v=H5v3kku4y6Q&list=PLRt3qGIZYRtg6qoscGfxCcSWggkIPNvSc&pp=gAQBiAQB8AUB"
        webbrowser.open(web)
