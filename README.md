## OpenAI Assistant Terminal Client  
  
### About  
  
  This is a terminal-based OpenAI Assistant client, which as of v2.0.0-beta uses the Textual UI. As of v3.0.0, the Requests API is used, and GPT-5.1 is the default model. (Model choice is configurable in the `settings.py` file.) The current version also supports file uploading and image generation.  
  I put this together for personal use as I do most of my work in the shell. It is meant to be a general-purpose AI assistant for those of us who work in the terminal.  
  
<img src="https://github.com/3ls-it/images/blob/main/ai-assistant_screen-08.png" alt="Screenshot 8, new opening dialogue." resize="400">
   
  It was developed and is used on Unix-like systems with no
consideration for that Other OS, though it should work on
any Unix-like platform.  
  
  To use this client, you will need OpenAI API credentials:  
https://platform.openai.com/docs/overview   
You will also need to configure a Prompt via your OpenAI Dashboard as well as a Vector Store. If you already have a Prompt configured, you can enter the ID on first run and use it. Caveat being that it must be configured to be used with the Responses API. You may also use an existing Vector Store, just provide it's ID on first run.  
  
  The Requests API is used for this client along with the Conversations API, which provides
session memory and context.
Each chat is logged locally, and can be used for chat continuation feature. The chat logs,
api logs, generated images, and settings are self-contained in `~/.openai-assistant/`.  
  
  
J Adams jfa63[at]duck[dot]com Nov 2025   
  
  
### Features  
  
- **Seamless Configuration**  
  • Auto-generates `~/.openai-assistant/settings.py` with all required and optional keys  
  • Built-in defaults for `MODEL` (gpt-5.1)  
  • Interactive prompting for missing values

- **Persistent Settings & IDs**  
  • In-situ prompts to save new IDs back to your settings file  
  • One-time setup — but you can always edit the settings if you choose to

- **Chat History with Memory**  
  • Logs every conversation to `~/.openai-assistant/chats/` to a time-stamped log file  
  • Uses Conversations API for per-chat context/memory  
  • Chat continuation feature  
   
- **Requests API Integration**  
  • Uses the OpenAI Requests API  
  • Uses all tools available for Requests: `code_interpreter`, `file_search`, `web_search`, `image_generation`...  
  • API logging to `~/.openai-assistant/api.log` with daily log rotation  
  
- **Textual, Interactive TUI**  
  • Multi-line editing with support for Markdown (submit with **ctrl+backslash**)  
  • Pretty Markdown rendering via `textual` and `rich`  
  • Real-time streaming of responses with event handling  
  • Textual provides built-in key-bindings and themes  
  
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
   You will also need to have the `feh` image program installed. Follow your operating system's method for package installation.  

2. Configure & Run  
   In the release directory, simply invoke the program; on first run it will auto-generate `~/.openai-assistant/settings.py` and prompt for required values.
   ```bash
   chmod 750 openai-assistant
   ./openai-assistant
   ```  
   or  
   ```bash
   python3 openai-assistant
   ```  
   • Default for `MODEL` (gpt-5.1) is applied automatically.  
   • Enter your `OPENAI_API_KEY`, `PROMPT_ID`, and `VECTOR_STORE_ID` when prompted.  
    
   Flags:
   - `--debug-api` — enable DEBUG-level API logging for more verbose diagnostics
  
<img src="https://github.com/3ls-it/images/blob/main/ai-assistant_screen-01.png" alt="Screenshot 1" resize="400">  
  
<img src="https://github.com/3ls-it/images/blob/main/ai-assistant_screen-02.png" alt="Screenshot 2" resize="400">  
  
3. Chat  
   • Multi-line input is supported (press **Enter** for a new line).  
   • Submit your message with **ctrl+backslash**.  
   • User input and responses are rendered as Markdown in the TUI.  
   • Quit session with **ctrl+q**  
   
<img src="https://github.com/3ls-it/images/blob/main/ai-assistant_screen-04.png" alt="Screenshot 4" resize="400">  
    
<img src="https://github.com/3ls-it/images/blob/main/ai-assistant_screen-05.png" alt="Screenshot 5" resize="400">  
   
4. Chat Continuation  
   • Select "Browse/Continue Chats" (F2) to browse past chat logs and continue the conversation   
        
5. Image Generation  
   • Generate images by entering description. Images are downloaded to `~/.openai-assistant/images/` and opened automatically with `feh`  
      
6. Configuration   
   Edit `~/.openai-assistant/settings.py` directly to tweak:  
   • `MODEL` (e.g. gpt-5.1, gpt-4o, etc.)  
   • Optional fields: `YOUR_NAME`, `ASSISTANT_NAME` for personalized display.   
   
