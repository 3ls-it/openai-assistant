## OpenAI Assistant Terminal Client  
  
### About  
  
  This is a terminal-based OpenAI Assistant client, which as of v2.0.0-beta uses the Textual UI. I put this together for personal use as I do most of my work in the shell. This is not meant to take the place of OpenAI's Codex CLI tool, but is meant to be a general-purpose AI assistant for those of us who work in the terminal.  
  
<img src="https://github.com/3ls-it/images/blob/main/ai-assistant_screen-08.png" alt="Screenshot 8, new opening dialogue." resize="400">
   
  It was developed and is used on Unix-like systems with no
consideration for that Other OS, though it should work on
any Unix-like platform.  
  
  To use this client, you will need OpenAI API credentials:  
https://platform.openai.com/docs/overview   
  
  The Assitants API is used for this client. This API provides
in-session memory, which is not persistent across chats. To
provide a chat history, we log the chat dialogue. The chat log
and settings file live in `~/.openai/`.  
  
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
  
J Adams jfa63[at]duck[dot]com Aug 2025   
  
  
### Features  
  
- **Seamless Configuration**  
  • Auto-generates `~/.openai/settings.py` with all required and optional keys  
  • Built-in defaults for `MODEL` (gpt-4.1) and `TEMP` (0.3)  
  • Interactive prompting for missing values (especially your `OPENAI_API_KEY`)

- **Persistent Settings & IDs**  
  • In-situ prompts to save new `ASSISTANT_ID` and `VECTOR_STORE_ID` back to your settings file  
  • One-time setup — you won’t recreate assistants or stores unless you choose to

- **Chat History with Memory**  
  • Logs every conversation to `~/.openai/chat_log.txt`  
  • On startup, uploads the log to an OpenAI Vector Store for retrieval by the `file_search` tool

- **Assistants API Integration**  
  • Uses the OpenAI Assistants API to maintain conversational state  
  • Pluggable tools: built-in `code_interpreter` and `file_search`
  • API logging to `~/.openai/api.log`
  
- **Textual, Interactive TUI**  
  • Multi-line editing with support for Markdown (submit with **ctrl+backslash**)  
  • Pretty Markdown rendering via `textual` and `rich`  
  • Real-time streaming of responses with event handling
  • Textual provides built-in key-bindings and themes:
  
<img src="https://github.com/3ls-it/images/blob/main/ai-assistant_screen-07.png" alt="Screenshot 7" resize="400">  
  
- **Robust Error Handling & Debugging**  
  • Skips empty-file uploads to avoid “File is empty” errors  
  • Full tracebacks on unexpected exceptions for easy troubleshooting

- **Lightweight & Self-Contained**  
  • Single executable Python file, (no additional files to copy)  
  • Minimal dependencies, all pinned via `requirements.txt`  
  
  
### Usage
  
1. Install dependencies  
   Download the current release and unpack the archive. Change to the release directory and install the Python dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

2. Configure & Run  
   In the release directory, simply invoke the script; on first run it will auto-generate `~/.openai/settings.py` and prompt for required values.
   ```bash
   chmod 750 openai-assistant
   ./openai-assistant
   ```  
   or  
   ```bash
   python3 openai-assistant
   ```  
   – Enter your `OPENAI_API_KEY` when prompted.  
   – Defaults for `MODEL` (gpt-4.1) and `TEMP` (0.3) are applied automatically.  
   – You’ll be offered to save newly created `ASSISTANT_ID` and `VECTOR_STORE_ID` back into your settings file.
   
   Flags:
   - `--no-upload` — skip uploading `~/.openai/chat_log.txt` at startup
   - `--reset-assistant` — ignore and clear `ASSISTANT_ID` in your settings (forces new assistant creation)
   - `--reset-store` — ignore and clear `VECTOR_STORE_ID` in your settings (forces new vector store)
   - `--debug-api` — enable DEBUG-level API logging for more verbose diagnostics
  
<img src="https://github.com/3ls-it/images/blob/main/ai-assistant_screen-01.png" alt="Screenshot 1" resize="400">  
  
<img src="https://github.com/3ls-it/images/blob/main/ai-assistant_screen-02.png" alt="Screenshot 2" resize="400">  
  
3. Chat  
   – Multi-line input is supported (press **Enter** for a new line).  
   – Submit your message with **ctrl+backslash**.  
   – User input and responses are rendered as Markdown in the TUI.  
   – Quit session with **ctrl+q**
  
<img src="https://github.com/3ls-it/images/blob/main/ai-assistant_screen-04.png" alt="Screenshot 4" resize="400">  
    
<img src="https://github.com/3ls-it/images/blob/main/ai-assistant_screen-05.png" alt="Screenshot 5" resize="400">  
  
  
4. Configuration  
   Edit `~/.openai/settings.py` directly to tweak:
   - `MODEL` (e.g. gpt-3.5-turbo, gpt-4)  
   - `TEMP` (0.0–2.0)  
   - Optional fields: `YOUR_NAME`, `ASSISTANT_NAME`, `FURTHER_INSTRUCTIONS`.

