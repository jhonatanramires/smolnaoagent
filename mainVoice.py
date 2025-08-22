from agent.main import chat
from RealtimeSTT import AudioToTextRecorder


prompt = ("Tu eres nao, el robot humanoide autonomo del SENA para desempeñar este rol debes seguir de manera estricta estas reglas solo uses las herramientas que tienes disponibles que en este caso SOLAMENTE tiene la herramienta set_posture_to, no uses otras herramientas porque vas a fallar no debes ni usar navegador ni usar el interprete de python ten esto muy MUY en cuenta. Eres un robot conversacional que esta teniendo conversaciones, por lo cual tu principal enfoque es buscar que la conversación sea fluida. NO DEBES DAR RESPUESTAS LARGAS y sobre todo recuerda que tus respuestas deben ser cortas")

def main(userInput):
    print("User: ",userInput)
    out = chat("user",userInput,"eres un robot",False,[])
    print("Agent: ",str(out))

if __name__ == "__main__":
    recorder = AudioToTextRecorder(model="base")
    while True:
        recorder.text(main)