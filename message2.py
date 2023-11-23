import telegram
import asyncio

token = "YOURTELEGRAM TOKEN"
bot = telegram.Bot(token = token)
# 자신이 설정한 link 주소 
public_chat_name = '@limtest'
id_channel = asyncio.run(bot.sendMessage(chat_id = public_chat_name , text="hi"))
print(id_channel)
