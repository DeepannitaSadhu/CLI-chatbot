from ollama import chat, ResponseError
from collections import deque
import sys


MEMORY_SIZE = 5

def main():
    print("CLI Chatbot (Gemma 3, memory=5 turns)")
    print("Type your message after 'user:'. Type 'exit' or 'quit' to stop.\n")

    
    history = deque(maxlen=MEMORY_SIZE * 2)  

    while True:
        try:
            user_input = input("user: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if not user_input or user_input.lower() in {"exit", "quit"}:
            print("Goodbye.")
            break

        
        history.append({"role": "user", "content": user_input})

        try:
            
            response_stream = chat(model="gemma3", messages=list(history), stream=True)

            print("bot:", end=" ", flush=True)
            bot_message = ""

            for chunk in response_stream:
                content = chunk.get("message", {}).get("content", "")
                if content:
                    print(content, end="", flush=True)
                    bot_message += content
            print()

           
            history.append({"role": "assistant", "content": bot_message})

        except ResponseError as e:
            print("\n[Error] Ollama response error:", getattr(e, "error", str(e)))
        except Exception as e:
            print("\n[Error] Failed to call Ollama:", str(e))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
