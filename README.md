# OpenAI Assistant CLI Client  
  
__About__  
  
  This is a command-line OpenAI Assistant client. I put this together
for personal use as I do most of my work in the shell.
  It was developed and is used on a Unix-like systems with no
consideration for that Other OS, though it should work on
any Unix-like platform.  
  
  To use this client, you will need OpenAI API credentials:  
https://platform.openai.com/docs/overview   
  
  The Assitants API is used for this client. This API provides
in-session memory, which is not persistent accross chats. To
provide a chat history, we log the chat dialogue. The chat log
and settings file live in `~/.openai/`. You will need to edit the
provided `settings.py` making sure to put your API key there.  
  
  At the start of each new chat, the chat history file is uploaded to
a Vector Store. You will see that when the Assistant object is first
instantiated, the tools 'file_search' and 'code_interpreter' are loaded.
See:  
https://platform.openai.com/docs/assistants/overview  
  
  At the time of this writing, the Assistants API is slated to
be depricated in favour of the newer Responses API sometime
in 2026. Before that time I will make the modifications needed
to use the Responses API.  
  
  You will need to choose a ChatGPT model that works with
this API, not all do. See:  
https://platform.openai.com/docs/models  
  
- J Adams jfa63[at]duck[dot]com May 2025   
  
__Features__  
  
- **Seamless Configuration**  
  • Auto-generates `~/.openai/settings.py` with all required and optional keys  
  • Built-in defaults for `MODEL` (`gpt-4.1`) and `TEMP` (0.3)  
  • Interactive prompting for missing values (especially your `OPENAI_API_KEY`)

- **Persistent Settings & IDs**  
  • In-situ prompts to save new `ASSISTANT_ID` and `VECTOR_STORE_ID` back to your settings file  
  • One-time setup—you won’t recreate assistants or stores unless you choose to

- **Chat History with Memory**  
  • Logs every conversation to `~/.openai/chat_log.txt`  
  • On startup, uploads the log to an OpenAI Vector Store for retrieval by the `file_search` tool

- **Assistants API Integration**  
  • Uses the OpenAI Assistants API to maintain conversational state  
  • Pluggable tools: built-in `code_interpreter` and `file_search`

- **Rich, Interactive CLI**  
  • Multi-line editing powered by `prompt_toolkit` (submit with Tab+Enter)  
  • Pretty Markdown rendering via `rich`  
  • Real-time streaming of responses with full event handling

- **Robust Error Handling & Debugging**  
  • Skips empty-file uploads to avoid “File is empty” errors  
  • Full tracebacks on unexpected exceptions for easy troubleshooting

- **Lightweight & Self-Contained**  
  • Single executable script (no additional files to copy)  
  • Minimal dependencies, all pinned via `requirements.txt`  
  
__Usage__
  
1. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```

2. Configure & Run  
   Simply invoke the script; on first run it will auto-generate `~/.openai/settings.py` and prompt for required values:
   ```bash
   ./openai-assistant
   ```
   – Enter your `OPENAI_API_KEY` when prompted.  
   – Defaults for `MODEL` (`gpt-4.1`) and `TEMP` (`0.3`) are applied automatically.  
   – You’ll be offered to save newly created `ASSISTANT_ID` and `VECTOR_STORE_ID` back into your settings file.

3. Chat  
   – Multi-line input is supported (press Enter for a new line).  
   – Submit your message with **Tab+Enter**.  
   – Responses stream in real-time, rendered as Markdown in your terminal.

4. Configuration  
   Edit `~/.openai/settings.py` directly to tweak:
   - `MODEL` (e.g. `gpt-3.5-turbo`, `gpt-4`)  
   - `TEMP` (0.0–2.0)  
   - Optional fields: `YOUR_NAME`, `ASSISTANT_NAME`, `FURTHER_INSTRUCTIONS`.

5. Chat History  
   – All sessions are logged to `~/.openai/chat_log.txt`.  
   – On startup, logs are uploaded to an OpenAI Vector Store (for `file_search`).

