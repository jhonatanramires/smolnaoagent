class Nao:
  def __init__(self, session):
    self.tts = session.service("ALAnimatedSpeech")
    self.

  def speak(self, text):
    self.tts.say(text)