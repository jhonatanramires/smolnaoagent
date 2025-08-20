from dotenv import load_dotenv
from os import getenv

load_dotenv()

IP_ADDRESS = getenv("ROBOT_IP_ADDRESS")
PORT = getenv("ROBOT_PORT")
