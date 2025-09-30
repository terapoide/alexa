import speech_recognition as sr
import pyttsx3
from playsound import playsound as ps
from datetime import datetime

from agenda import executar_agenda
from calculadora import calc_main
from ia import chamar_ollama


reconhecedor = sr.Recognizer()

def falar(texto):
    engine = pyttsx3.init()   # reinicia engine a cada uso (evita travamento)
    engine.say(texto)
    engine.runAndWait()
    engine.stop()

def hora_e_data():
    agora = datetime.now()
    hora = agora.strftime("%H:%M")
    data = agora.strftime("%d/%m/%Y")
    return hora, data

with sr.Microphone() as mic:
    reconhecedor.adjust_for_ambient_noise(mic, duration=20)
    
    # primeira fala
    falar("O que deseja executar, suas opções são: Agenda, Calculadora, Horário ou fazer alguma pergunta para mim, pode falar após o beep")
    # beep sound
    ps("sound/rrtong.mp3")
    audio = reconhecedor.listen(mic)
    ps("sound/reconhecendo.mp3")
    
    try:
        texto = reconhecedor.recognize_google(audio, language='pt')
        print(f"Texto reconhecido: {texto}")

        if "agenda" in texto.lower():
            executar_agenda(texto.lower())
        elif "calculadora" in texto.lower():
            calc_main()
        elif "horário" in texto.lower():
            hora, data = hora_e_data()
            resposta = f"Agora são {hora} do dia {data}"

            falar(resposta)

            print(resposta)
        else:
            chamar_ollama(texto.lower())
    except sr.UnknownValueError:
        print("Não entendi o que foi dito.")
