import speech_recognition as sr

reconhecedor = sr.Recognizer()

def ouvir_microfone(prompt="Fale agora..."):
    with sr.Microphone() as mic:
        reconhecedor.adjust_for_ambient_noise(mic, duration=2)
        print(prompt)
        audio = reconhecedor.listen(mic)
        print("Reconhecendo áudio, aguarde...")
        try:
            texto = reconhecedor.recognize_google(audio, language='pt')
            print(f"Texto reconhecido: {texto}")
            return texto.lower()
        except sr.UnknownValueError:
            print("Não entendi o que foi dito.")
        except sr.RequestError:
            print("Erro ao acessar o serviço de reconhecimento.")
    return None

def calcular(conta, valor_anterior=None):
    try:
        if valor_anterior is not None:
            operador, valor = conta[0], conta[1]
            num1 = float(valor_anterior)
            num2 = float(valor)
        else:
            num1 = float(conta[0])
            operador = conta[1]
            num2 = float(conta[2])

        if operador in ["x", "vezes", "*"]:
            return num1 * num2
        elif operador in ["+", "mais"]:
            return num1 + num2
        elif operador in ["/", "dividido"]:
            if num2 == 0:
                print("❌ Erro: divisão por zero.")
                return None
            return num1 / num2
        elif operador in ["-", "menos"]:
            return num1 - num2
        else:
            print("❌ Operador não reconhecido.")
            return None
    except IndexError:
        print("❌ Erro: expressão incompleta.")
    except ValueError:
        print("❌ Erro: valores inválidos.")
    return None

def calc_main():
    total = None

    while True:
        texto = ouvir_microfone("Fale uma conta simples (ex: 5 + 3):")
        if not texto:
            break

        conta = texto.split()

        resultado = calcular(conta, valor_anterior=total if total is not None else None)

        if resultado is not None:
            total = resultado
            print(f"✅ Resultado = {total}")
        else:
            print("❌ Não foi possível calcular.")

        continuar = ouvir_microfone("Deseja continuar com esse resultado? (sim/não)")
        if continuar != "sim":
            break

        texto = ouvir_microfone("O que fazer com o resultado anterior? (ex: + 5)")
        if texto:
            conta = texto.split()
        else:
            break
