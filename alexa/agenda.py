import os
import speech_recognition as sr

ARQUIVO_AGENDA = "agendaescrita.txt"
reconhecedor = sr.Recognizer()

def ouvir_microfone(prompt="Fale agora:"):
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as mic:
        reconhecedor.adjust_for_ambient_noise(mic, duration=2)
        print(prompt)
        audio = reconhecedor.listen(mic)

    try:
        texto = reconhecedor.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {texto}")
        return texto.lower()
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
    except sr.RequestError:
        print("Erro ao acessar o serviço de reconhecimento.")
    return None

def ouvir_agenda():
    if os.path.exists(ARQUIVO_AGENDA):
        with open(ARQUIVO_AGENDA, "r", encoding="utf-8") as f:
            conteudo = f.read()
            if conteudo.strip():
                print("\n📅 Sua agenda:")
                print(conteudo)
            else:
                print("\n📭 Sua agenda está vazia.")
    else:
        print("Arquivo de agenda não encontrado.")

def anotar_agenda():
    print("Diga o que você quer anotar na agenda:")
    novo_item = ouvir_microfone()
    if novo_item:
        with open(ARQUIVO_AGENDA, "a", encoding="utf-8") as f:
            f.write(f"{novo_item}\n")
        print("Anotado com sucesso.")

def refazer_agenda():
    print("Diga o novo conteúdo da agenda (isso irá substituir tudo):")
    novo_conteudo = ouvir_microfone()
    if novo_conteudo:
        with open(ARQUIVO_AGENDA, "w", encoding="utf-8") as f:
            f.write(f"{novo_conteudo}\n")
        print("Agenda refeita com sucesso.")

def executar_agenda():
    with sr.Microphone() as mic:
        """Executa uma ação de agenda com base no texto reconhecido"""
        reconhecedor.adjust_for_ambient_noise(mic, duration=2)
        print("O que deseja executar? suas opções são: Ouvir, Anotar, Refazer...")
        audio = reconhecedor.listen(mic)
        print("Reconhecendo áudio, aguarde...")
        texto = reconhecedor.recognize_google(audio, language='pt')
        if "ouvir" in texto.lower():
            ouvir_agenda()
        elif "anotar" in texto.lower():
            anotar_agenda()
        elif "refazer" in texto.lower() or "apagar" in texto.lower():
            refazer_agenda()
        else:
            print("Comando de agenda não reconhecido.")
