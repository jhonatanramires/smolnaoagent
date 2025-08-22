import os
from smolagents import OpenAIServerModel, ToolCallingAgent
#from agent.tools import tools
from dotenv import load_dotenv
from os import getenv
from langchain_community.chat_message_histories import SQLChatMessageHistory

load_dotenv()

key = getenv("API_KEY")

print(key)

def init_agent() -> ToolCallingAgent:
    model = OpenAIServerModel(
        model_id="deepseek-chat",
        api_base="https://api.deepseek.com/v1",
        api_key=key,
        custom_role_conversions={"system": "system", "user": "user", "assistant": "assistant"}
    )
    return ToolCallingAgent(
        tools=[],
        model=model,
        add_base_tools=True
    )

def format_message(role: str, content: str) -> str:
    """Compact message formatting to save tokens"""
    return f"{role[0].upper()}: {content}"

def chat(session_id: str, user_query: str, system_prompt: str = None, max_context_tokens: int = 3000) -> str:
    agent = init_agent()
    history = SQLChatMessageHistory(
      session_id=session_id,
      connection="sqlite:///memory.db"
    )

    # Build compact context
    context_lines = []
    token_count = 0
    
    # Add system prompt if exists
    if system_prompt:
        sys_msg = format_message("system", system_prompt)
        context_lines.append(sys_msg)

    # Add history in reverse (newest first) until token limit
    for msg in reversed(history.messages):
        role = "user" if msg.type == "human" else "assistant"
        formatted = format_message(role, msg.content)

        context_lines.insert(0, formatted)  # Add to beginning
        token_count += len(formatted.split())
        if token_count > max_context_tokens:
            context_lines.pop(0)  # Remove oldest message
            break  # Stop when we reach token limit

    # Add current query
    user_msg = format_message("user", user_query)
    context_lines.append(user_msg)
    
    # Join with newlines for final prompt
    compact_prompt = "\n".join(context_lines) + "\nA:"
    
    # Get response
    response = agent.run(compact_prompt)

    # Persist interaction
    history.add_user_message(user_query)
    history.add_ai_message(response)
    
    return response

if __name__ == "__main__":
    session = "user123"
    sys_prompt = "Helpful assistant with conversation memory"
    
    # Test conversation
    print("Agent:", chat(session, "Hello my name is Juan!", sys_prompt))
    print("Agent:", chat(session, "What's my name?", sys_prompt))
    print("Agent:", chat(session, "iniciar sesión en Spotify", sys_prompt))