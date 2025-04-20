# ChatGPT Assitant Client
  
  This is a command-line ChatGPT client. I put this together
for personal, and it uses some bits and pieces from example code
provided by OpenAI's documentation.  
https://platform.openai.com/docs  
  
  It was developed and is used on a Unix-like systems with no
consideration for that Other OS, though it should work on
most any platform.  
  
  To use this client, you will need OpenAI API credentials:  
https://platform.openai.com/docs/overview  
  
  The Assitants API is used for this client. This API provides
in-session memory, which is not persistent accross chats. To
provide a chat history, we log the chat dialogue. The chat log
and settings file live in `~/.openai/`. You will need to edit the
provided `settings.py` making sure to put your API there.
  
At the start of each new chat, the chat history file is uploaded. You will
see that when the assistants object is instantiated, the tools
'file_search' and 'code_interpreter' are loaded. See:  
https://platform.openai.com/docs/assistants/overview  
  
  At the time of this writing, the Assistants API is slated to
be depricated in favour of the newer Responses API sometime
in 2026.  
  
  You will need to choose a ChatGPT model that works with
this API, not all do.  
https://platform.openai.com/docs/models  
  
  While entering a query, you can use L|R arrow keys to navigate
your line of text. Hitting 'ENTER' will create a new line. To submit
your query, use 'TAB+ENTER'.  
  
-J Adams jfa63[at]duck[dot]com March 2025
