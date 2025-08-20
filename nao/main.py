from qi import Session
from cons import IP_ADDRESS, PORT

session = Session()

session.connect(f"tcp://{IP_ADDRESS}:{PORT}")

tts = session.service("ALAnimatedSpeech")

tts.say("Hello, I am ready to assist you!")