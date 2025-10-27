#  CLI Chatbot with Sliding-Window Memory (Ollama + Gemma 3)

A lightweight **command-line chatbot** powered by the **Ollama** local LLM runtime and **Gemma 3**.
It uses a **sliding-window memory buffer** to keep recent conversation context for coherent replies — all running **locally**, with **no API keys or cloud dependencies**.

---

##  Features

*  **Sliding-window memory** — remembers the last *N* turns of conversation (default: 5)
*  **Runs locally via Ollama** — no internet connection or API key required
*  **Streaming responses** for real-time interaction
*  **Simple CLI interface** — type messages continuously and exit with `exit` or `quit`
*  **Clean modular codebase** with clear responsibilities:

  * `chatbot.py` → main CLI script with conversation loop and memory buffer
  * (optional future) `utils/` → helper modules for expansion (logging, formatting, etc.)

---

## Setup Instructions

### 1 Install Ollama

If Ollama isn’t installed yet:

```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

Then pull the **Gemma 3** model:

```bash
ollama pull gemma3
```

### 2 Create and Activate a Virtual Environment

```bash
python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3 Install Dependencies

```bash
pip install -r requirements.txt
```

### 4 Run the Chatbot

```bash
python chatbot.py
```

---

## Example Conversation

```
CLI Chatbot (Gemma 3, memory=5 turns)
Type your message after 'user:'. Type 'exit' or 'quit' to stop.

user: Hey there!
bot: Hi! How can I help you today?

user: Who discovered penicillin?
bot: Penicillin was discovered by Alexander Fleming in 1928.

user: Thanks!
bot: You're welcome!

user: exit
Goodbye.
```

---

## Customization

### Memory Size

Change how many turns the chatbot remembers by editing:

```python
MEMORY_SIZE = 5
```

For example, set `MEMORY_SIZE = 10` for a longer context window.

### Model Selection

You can use **any Ollama model** by changing this line in the script:

```python
response_stream = chat(model="gemma3", messages=list(history), stream=True)
```

Examples:

* `llama3`
* `mistral`
* `phi3`
* `gemma3:8b`

---

## Project Structure

```
project/
│
├── chatbot.py          # Main CLI chatbot with streaming + memory
├── requirements.txt    # Dependencies (Ollama client)
└── README.md           # Documentation
```

---

## Example Use Cases

* Simple **local AI assistant** for text conversations
* Demonstration of **Ollama Python API** usage
* Educational project for **memory-based dialogue systems**
* Starting point for integrating local LLMs into other Python apps

---

##  Requirements

```
ollama>=0.1.0
```

