from qi import Session
from nao import Nao
from dotenv import load_dotenv
from os import getenv

load_dotenv()

s = Session()
s.connect(f"tcp://{getenv("NAO_IP")}:{getenv("NAO_PORT")}")

nao = Nao(s)

def 