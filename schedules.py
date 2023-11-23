import schedule
import time
import telegram
import pytz
import datetime
import asyncio

# Anaconda pip 모듈 설치
# pip install schedule --upgrade

# 특정 시간에는 알림이 가지 않도록
# pip install datetime --upgrade
# pip install pytz --upgrade


def job():

    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    # 30분마다 현재 시간을 일정하게 출력
    print("current time = ", str(now))
    # 오후 11시 부터 오전 6시까지는 메시지 출력 금지!!!
    if now.hour >= 23 or now.hour <= 6:
        return
    
    # 채널 메시지 보내기
    token = "YOUR TELEGRAM TOKEN"
    bot = telegram.Bot(token = token)
    public_chat_name='@limtest'
    chat_id = "CHAT_ID"
    text = 'Hello, Telegram!'
    asyncio.run(bot.sendMessage(chat_id = chat_id , text=text))

# 30분 마다 실행
schedule.every(30).minutes.do(job)

print("Start App")

# 파이선 스케줄러
while True:
    schedule.run_pending()
    time.sleep(1)


