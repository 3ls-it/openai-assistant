#!/data/data/com.termux/files/usr/bin/env python3
import openai
import os
import sys
from rich import print

print("[red]This will delete ALL files uploaded to your OpenAI account![/]")
ans = input("If you wish to continue, type 'YES':")
if ans != "YES":
    sys.exit()

print("Cleaning up uploaded files...")

homedir = os.path.expanduser("~") + "/"
os.makedirs(homedir + ".openai", exist_ok=True)
sys.path.insert(0, homedir + ".openai")
from settings import  OPENAI_API_KEY

client = openai.OpenAI(api_key=OPENAI_API_KEY)

# List all files
files = client.files.list()

# Delete each file
for file in files.data:
    file_id = file.id
    print(f"Deleting file: {file_id} ({getattr(file, 'filename', 'no name')})")
    client.files.delete(file_id)

print("All files deleted.")
