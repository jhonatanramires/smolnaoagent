from qi import Session
from nao.nao import Nao
from dotenv import load_dotenv
from os import getenv
from smolagents import tool

load_dotenv()

s = Session()
s.connect(f"tcp://{getenv("NAO_IP")}:{getenv("NAO_PORT")}")

nao = Nao(s)


# Lista de posturas válidas para evitar errores
VALID_POSTURES = [
    "StandInit", "SitRelax", "StandZero",
    "LyingBelly", "LyingBack", "Stand",
    "Crouch", "Sit"
]

@tool
def set_posture_to(posture: str) -> str:
    """
    Sets the robot's posture to one of the allowed predefined postures.

    Args:
        posture: Posture to apply. Must be a string and one of the following:
        ["StandInit", "SitRelax", "StandZero", "LyingBelly", "LyingBack", "Stand", "Crouch", "Sit"]

    Returns:
        Nothing

    Raises:
        ValueError: If the posture is not valid.
    """
    if posture not in VALID_POSTURES:
        raise ValueError(f"Invalid posture: '{posture}'. Must be one of {VALID_POSTURES}.")

    nao.posture.goToPosture(str(posture),0.5)

@tool
def walk(x: float, y: float, theta: float) -> None:
    """
    Moves the robot at the specified velocities along the X, Y axes and rotation around the Z-axis.

    Args:
        x (float): Velocity along the X-axis (in meters per second). Use negative values for backward motion.
        y (float): Velocity along the Y-axis (in meters per second). Use positive values to move to the left.
        theta (float): Velocity around the Z-axis (in radians per second). Use negative values to turn clockwise.

    Returns:
        None

    Raises:
        ValueError: If the velocities are not valid numbers (NaN or infinite).
    """
    # Ensure that the parameters are valid numbers
    if any(map(lambda v: not isinstance(v, (int, float)) or not (-float('inf') < v < float('inf')), [x, y, theta])):
        raise ValueError("Invalid velocity values. They must be finite numbers.")

    nao.motion.move(x, y, theta)


# Ejecución directa
if __name__ == "__main__":
    try:
        posture = input(f"Enter posture ({', '.join(VALID_POSTURES)}): ")
        result = set_posture_to(str(posture))
        print(result)
    except Exception as e:
        print(f"Error: {e}")