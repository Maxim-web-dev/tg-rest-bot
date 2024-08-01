from dotenv import load_dotenv
import json, os

load_dotenv()

# --Othen variables--
TOKEN = os.getenv("TOKEN")

# --JSON--
with open("bot\\data\\configs\\config.json", "r") as file:
    j = json.load(file)
    
print(j)