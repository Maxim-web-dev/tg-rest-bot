from dotenv import load_dotenv
import json, os

load_dotenv()

# --Othen variables--
TOKEN = os.getenv("TOKEN")

# --JSON--
with open("bot\\data\\configs\\config.json", "r") as file:
    j = json.load(file)
    
# --texts--
welcome_text = f"""<b>Добро пожаловать</b>!

Вы можете сделать доставку через этого бота.
-- Контактные данные для поддержки: {j['telephone_number_devilery']}

..."""