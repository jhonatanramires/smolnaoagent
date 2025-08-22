from nao.setupNao import setup_nao
from os import getenv
from dotenv import load_dotenv
from agent.main import chat
from RealtimeSTT import AudioToTextRecorder

load_dotenv()

nao = setup_nao(getenv("NAO_IP"),getenv("NAO_PORT"))

def main(userInput):
    out = chat("user",userInput,"eres un robot")
    nao.speak(out)

if __name__ == "__main__":
    recorder = AudioToTextRecorder()
    nao.autonomousBehavior()
    while True:
        recorder.text(main)