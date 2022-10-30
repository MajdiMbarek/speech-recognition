import speech_recognition as sr

name = sr.Recognizer()

with sr.Microphone() as mic :
    while True :
        print("say somthing ...")
        audio = name.listen(mic)
        text = name.recognize_google(audio)

        if text in "hello":
            print("Hi Majdi , how are you?")
        elif text in ["I'm fine" , "good","I'm good"]:
            print("nice to meet you")
        elif text in "close" :
            exit()
        else :
            print("i don't understand you")