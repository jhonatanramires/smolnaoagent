class Nao:
  def __init__(self, session):
    self.s = session
    self.tts = self.s.service("ALAnimatedSpeech")
    self.audio = self.s.service("ALAudioDevice")

  def speak(self, text):
    self.tts.say(text)

  def isSpeaking(self):
    output_energy = self.audio.getOutputEnergy()
    if output_energy > 0.1:
      return True
    else:
      return False

  def autonomousBehavior(self):
    self.s.service("ALAutonomousLife").setState("disabled")  
    self.s.service("ALSpeakingMovement").setEnabled(True)
    self.s.service("ALAutonomousLife").setState("solitary")
    self.s.service("ALBackgroundMovement").setEnabled(True)
    self.s.service("ALSpeakingMovement").setMode("contextual")

if __name__ == "__main__":
  from qi import Session
  s = Session()
  s.connect("tcp://10.42.0.44:9559")

  nao = Nao(s)
  nao.autonomousBehavior()
  nao.speak("hola, como estas? Tengo capacidad de moverme en base a lo que digo. Ya no tenemos que rellenar con animaciones en choreographe, al fin.")
  nao.speak("yo")