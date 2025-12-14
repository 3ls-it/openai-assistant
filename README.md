## OpenAI Assistant Terminal Client  
  
### About  
  
  This is a terminal-based OpenAI Assistant client, which as of v2.0.0-beta uses the Textual UI. As of v3.0.0, the Requests API is used, and GPT-5.2 is the default model. (Model choice is configurable in the `settings.py` file.) The current version supports file uploading and image generation, and features "pretty printing" of LaTeX math expressions.  
  I put this together for personal use as I do most of my work in the shell. It is meant to be a general-purpose AI assistant for those of us who work in the terminal.  
  
  It was developed and is used on Unix-like systems with no consideration for that Other OS, though it should work on any Unix-like platform.  
  
  To use this client, you will need OpenAI API credentials:  
https://platform.openai.com/docs/overview   
You will also need to configure a Prompt via your OpenAI Dashboard as well as a Vector Store. If you already have a Prompt configured, you can enter the ID on first run and use it. Caveat being that it must be configured to use the Responses API with `effort: none`. You may also use an existing Vector Store, just provide it's ID on first run.  
  
  The Responses API is used for this client along with the Conversations API, which provides session-level memory and context.
Each chat is logged locally, and can be used for chat continuation feature. The chat logs, api logs, generated images, and settings are self-contained in `~/.openai-assistant/`.  
  
  
J Adams jfa63[at]duck[dot]com Dec 2025   
  
  
### Features  
  
- **Seamless Configuration**  
  • Auto-generates `~/.openai-assistant/settings.py` on first run with all required and optional keys  
  • Built-in defaults for `MODEL` (gpt-5.2)  
  • Interactive prompting for missing values

- **Persistent Settings & IDs**  
  • In-situ prompts to save new IDs back to your settings file  
  • One-time setup — but you can always edit the settings if you choose to

- **Chat History with Memory**  
  • Logs every conversation to `~/.openai-assistant/chats/` to a time-stamped log file  
  • Uses Conversations API for per-chat context/memory  
  • Chat continuation feature allows for additional instructions  
   
- **Requests API Integration**  
  • Uses the OpenAI Requests API  
  • Uses all tools available for Requests: `code_interpreter`, `file_search`, `web_search`, `image_generation`...  
  • API logging to `~/.openai-assistant/api.log` with daily log rotation  
  
- **Textual, Interactive TUI**  
  • Multi-line editing with support for Markdown (submit with **ctrl+backslash**)  
  • Pretty Markdown rendering via `textual` and `rich`  
  • Pretty LaTeX math rendering via `pylatexenc` (display only; log files unaltered)
  • Textual provides built-in key-bindings and themes  
  
- **Robust Error Handling & Debugging**  
  • Skips empty-file uploads to avoid “File is empty” errors  
  • Full tracebacks on unexpected exceptions for easy troubleshooting

- **Lightweight & Self-Contained**  
  • Single executable Python file, (no additional files to copy)  
  • Minimal dependencies, all pinned via `requirements.txt`  
  
  
### Usage
  
1. Install dependencies  
   • Download the current release and unpack the archive. Change to the release directory and install the Python dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
   • You will also need to have the `feh` image program installed if you want automatic image display. Follow your operating system's method for package installation.  
  
2. Configure & Run  
   • In the release directory, simply invoke the program; on first run it will auto-generate `~/.openai-assistant/settings.py` and prompt for required values. 
   ```bash
   chmod 750 openai-assistant
   ./openai-assistant
   ```  
   or  
   ```bash
   python3 openai-assistant
   ```  
   • Optionally (and recommended) copy `openai-assistant` to a location in your `PATH`, e.g., `~/bin/`, `~/.local/bin/`, etc.  
   • Default for `MODEL` (gpt-5.2) is applied automatically.  
   • Enter your `OPENAI_API_KEY`, `PROMPT_ID`, and `VECTOR_STORE_ID` when prompted.  
   • Flags:  
   &nbsp;&nbsp;- `--debug-api` — Enable DEBUG-level API logging for more verbose diagnostics  
   &nbsp;&nbsp;- `--reset-prompt` — Ignore and clear `PROMPT_ID` in settings before startup    
   
3. Chat  
   • Multi-line input is supported (press **Enter** for a new line).  
   • Submit your message with **ctrl+backslash**.  
   • User input and responses are rendered as Markdown in the TUI.  
   • Quit session with **ctrl+q**  
   
<img src="https://github.com/3ls-it/images/blob/main/assistant_v3_01.png" alt="Screenshot 1" resize="400">  
    
<img src="https://github.com/3ls-it/images/blob/main/assistant_v3_02.png" alt="Screenshot 2" resize="400">  
   
4. Chat Continuation  
   • Select "Browse/Continue Chats" (F2) to browse past chat logs and continue the conversation   
   • Left-click chat file to load it into the chat viewer     
   • Hit `Enter` to continue selected chat. Optionally type in further instructions  
   
<img src="https://github.com/3ls-it/images/blob/main/assistant_v3_03.png" alt="Screenshot 3" resize="400">  
  
<img src="https://github.com/3ls-it/images/blob/main/assistant_v3_04.png" alt="Screenshot 4" resize="400">  
  
5. Image Generation  
   • Generate images by making the request and entering descriptions in the input widget. Multiple images may be requested in one entry  
   • Images are downloaded to `~/.openai-assistant/images/` and opened automatically with `feh`, if installed or try to fall back on ImageMagick's `display`.  
  
<img src="https://github.com/3ls-it/images/blob/main/assistant_v3_05.png" alt="Screenshot 5" resize="400">  
   
6. Configuration   
   • Edit `~/.openai-assistant/settings.py` directly to tweak:  
   &nbsp;&nbsp;- `MODEL` (e.g. gpt-5.2, gpt-5-mini, gpt-4o, etc.)  
   &nbsp;&nbsp;- Optional fields: `YOUR_NAME`, `ASSISTANT_NAME` for personalized display.   
   
