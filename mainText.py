from agent.main import chat

def main(userInput):
    out = chat("user",userInput,"eres un robot. ",False)
    print("Agent: ", out)

if __name__ == "__main__":
    while True:
        userInput = input("user: ")
        main(userInput)