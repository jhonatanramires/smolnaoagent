from nao.setupNao import setup_nao
from os import getenv
from dotenv import load_dotenv
from agent.main import chat
from RealtimeSTT import AudioToTextRecorder
from generatePrompt import generate
from nao.tools import set_posture_to


load_dotenv()

nao = setup_nao(getenv("NAO_IP"),getenv("NAO_PORT"))
prompt = generate("Tu eres nao, el robot humanoide autonomo del SENA para desempeñar este rol debes seguir de manera estricta estas reglas solo uses las herramientas que tienes disponibles que en este caso SOLAMENTE tiene la herramienta set_posture_to, no uses otras herramientas porque vas a fallar no debes ni usar navegador ni usar el interprete de python ten esto muy MUY en cuenta. Eres un robot conversacional que esta teniendo conversaciones, por lo cual tu principal enfoque es buscar que la conversación sea fluida. NO DEBES DAR RESPUESTAS LARGAS y sobre todo recuerda que tus respuestas deben ser cortas",nao)

def main(userInput):
    print("User: ",userInput)
    out = chat("user",userInput,"eres un robot",False,[set_posture_to])
    nao.speak(str(out))
    print("Agent: ",str(out))

if __name__ == "__main__":
    recorder = AudioToTextRecorder(wake_words="oye, nao",model="base")
    nao.autonomousBehavior()
    while True:
        recorder.text(main)