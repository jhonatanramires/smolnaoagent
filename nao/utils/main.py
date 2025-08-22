from nao.nao import Nao
def setup_nao(IP,PORT):
  from qi import Session
  s = Session()
  s.connect(f"tcp://{IP}:{PORT}")
  nao = Nao(s)
  nao.autonomousBehavior()
  nao.speak("Como estan?")
  return nao