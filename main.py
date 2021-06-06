import googletrans
import speech_recognition as sr
import gtts
import playsound
import pyttsx3
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
translator = googletrans.Translator()
input_lang = 'ml'
output_lang = 'hi'


def take_command():
    try:
        with sr.Microphone() as source:
            print('Speak Now')
            voice = recognizer.listen(source)
            text = recognizer.recognize_google(voice, language=input_lang)
            print(text)
    except:
        pass
    return text


def translation():
    text=take_command()
    translated = translator.translate(text, dest=output_lang)
    print(translated.text)
    converted_audio = gtts.gTTS(translated.text, lang=output_lang)
    converted_audio.save('trans.mp3')
    playsound.playsound('trans.mp3')
    os.remove('trans.mp3')


while True:
    translation()