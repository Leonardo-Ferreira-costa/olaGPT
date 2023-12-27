import speech_recognition as sr
import openai

# Configurar sua chave da API OpenAI
openai.api_key = 'Sua_API_Aqui'

rec = sr.Recognizer()

def consulta_gpt():
    # Consultar o ChatGPT com o texto reconhecido
    try:
        with sr.Microphone(0) as mic:
            rec.adjust_for_ambient_noise(mic)
            print("Escutando...")
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language="pt-BR")

            resposta = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=texto,
                    max_tokens=50,
                    temperature=0.5,  # Adjust for creativity
                    top_p=1,  # Control response diversity
                    frequency_penalty=0,  # Fine-tune word frequency
                    presence_penalty=0  # Fine-tune word presence
                )

        resposta_gpt = resposta.choices[0].text.strip()
        
    except Exception as e:
        print(f"Texto passado: {texto}") #Debug
        print(f"Erro ao consultar a API do ChatGPT: {e}")
        # return "Ocorreu um erro ao processar a solicitação. Por favor, tente novamente."
 
    # Exibir a resposta do ChatGPT
    print("Resposta do ChatGPT:", resposta_gpt)

#Mantem sempre a aplicação escutando
while True:
    with sr.Microphone(0) as mic:
        rec.adjust_for_ambient_noise(mic)
        print("Esperando comando Olá GPT...")
        audio = rec.listen(mic)
        
        try:
            texto = rec.recognize_google(audio, language="pt-BR")
            if texto == "Olá GPT":
                print("Comando reconhecido. Executando função...") #Debug
                consulta_gpt()
        except sr.UnknownValueError:
            # Caso não tenha entendido a fala
            pass
