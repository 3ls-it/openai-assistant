# ChatGPT Assitant CLI Client
  
  This is a command-line ChatGPT client. I put this together
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
  
  While entering a query, you can use L|R arrow keys to navigate
your line of text. Hitting 'ENTER' will create a new line. To submit
your query, use 'TAB+ENTER'.  
  
-J Adams jfa63[at]duck[dot]com May 2025
