import telegram
import asyncio

token = "YOUR TELEGRAM TOKEN"
bot = telegram.Bot(token = token)
chat_id = "CHAT_ID"
text = 'Hello, Telegram!!!!!'
asyncio.run(bot.sendMessage(chat_id = chat_id , text=text))