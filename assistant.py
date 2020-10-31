import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

if __name__ == '__main__':
    lg = 'en'
    r = sr.Recognizer()
    with sr.Microphone() as source:
        text = "Speak something"
        print(text)
        speech = gTTS(text=text, lang=lg, slow=False)
        speech.save("text.mp3")
        playsound('text.mp3')
        audio = r.listen(source)
    try:
        x = ("Google Speech Recognition thinks you said:\n " + r.recognize_google(audio))
        print(x)


    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
