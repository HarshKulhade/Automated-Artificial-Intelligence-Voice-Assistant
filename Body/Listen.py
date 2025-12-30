from googletrans import Translator
import speech_recognition 
import googletrans


def Listen():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source,0,5)

    try:
        print("Understanding...")
        query = r.recognize_google(audio,language='en')
        print(f"You Said: {query}\n")
    #excepxception as e:
    except:
        #print("Say that Again")
        return ""
    
    query = str(query).lower()
    return query


def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"You Said:{data}")   
    return data


def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data

