
def autonomousBehavior(s: Session):
  s.service("ALAutonomousLife").setState("disabled")  
  s.service("ALAutonomousLife").setState("solitary")
  s.service("ALBackgroundMovement").setEnabled(True)
  s.service("ALSpeakingMovement").setMode("random")
  s.service("ALSpeakingMovement").setEnabled(True)