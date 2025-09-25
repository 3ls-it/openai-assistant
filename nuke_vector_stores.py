#!/data/data/com.termux/files/usr/bin/env python3
from openai import OpenAI
import os
import sys
from rich import print

print("[red]This will delete ALL Vector Stores![/]")
ans = input("If you wish to continue, type 'YES':")
if ans != "YES":
    sys.exit()

print("Nuking Vector Stores...")

homedir = os.path.expanduser("~") + "/"
os.makedirs(homedir + ".openai", exist_ok=True)
sys.path.insert(0, homedir + ".openai")
from settings import  OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

# Walk through every page of vector stores
for page in client.vector_stores.list(limit=100).iter_pages():
    for vs in page.data:
        client.vector_stores.delete(vector_store_id=vs.id)
        print(f"✔ Deleted {vs.id}")

print("[green]Done.[/]")
