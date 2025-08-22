
def generate(prompt,nao):
    postures = "Tu como un robot Nao, tienes la capacidad de tomar diferentes posturas." \
    "para tomar estas posturas tienes una herramienta que puedes usar " \
    "y la debes usar en dos casos: " \
    "1. Cuando te lo pidan directamente, en el momento en el que te lo piden directamente puedes tomar la postura que te pidieron solo despues de pedir una confimación directa " \
    "2.En base al contexto, cuando vas a decir algo y cierta postura seria ideal para expresar mejor lo que diras puedes antes de decirlo pedir tomar cierta postura. Debes tomar la postura y luego decir lo que ibas a decir. " \
    f"Las posturas que tienes disponibles son:{(nao.s.service("ALRobotPosture")).getPostureList()} """

if __name__ == "__main__":
    from dotenv import load_dotenv
    from os import getenv

    load_dotenv()

    PORT = getenv("NAO_PORT")
    IP = getenv("NAO_IP")

    nao = setup_nao(IP,PORT)
    generate("hola",)