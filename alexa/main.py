import speech_recognition as sr
from agenda import executar_agenda
from calculadora import calc_main  # como exemplo, se você for usar
from ia import chamar_ollama
# Todo: 
# main aguardar ser chamado 
# main explicar funcoes 
# agenda 
# update na calc 
# identificador de face
# Que horas são

reconhecedor = sr.Recognizer()

with sr.Microphone() as mic:
    reconhecedor.adjust_for_ambient_noise(mic, duration=5)
    print("O que deseja executar? suas opções são: Agenda ou Calculadora...")
    audio = reconhecedor.listen(mic)
    print("Reconhecendo áudio, aguarde...")
    texto = reconhecedor.recognize_google(audio, language='pt')
    print(f"Texto reconhecido: {texto}")
    # 🔄 Decide o que fazer com base no texto:
    if "agenda" in texto.lower():
        executar_agenda(texto.lower())
    elif "calculadora" in texto.lower():
        calc_main()  # supondo que você tenha isso no seu módulo calculadora
    else:
        chamar_ollama(texto.lower())
