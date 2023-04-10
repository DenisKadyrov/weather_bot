import telebot
import schedule
import time
import math
import json
import requests

token = '5432636852:AAHJDIlpx0qAP5UBFirEc3eJ623jZhRffNg'
bot = telebot.TeleBot(token)

url = 'https://api.openweathermap.org/data/2.5/weather?lat=57.1522&lon=65.5272&appid=c6c3c7f3e904530075ff6b57666c3ed0&units=metric&lang=ru'

list_if = [5250094350, 1081723619]

@bot.message_handler(content_types = ['text'])
def get_weather(message):

    if message.text == 'погода':
        res = requests.get(url)
        weather_info = res.json()

        messag = 'Сегодня на улице {0}, {1}°C, при этом ощущаеться как {2}°C. Ветер {3} м/с'.format(weather_info['weather'][0]['description'], 
            math.ceil(weather_info['main']['temp']), math.ceil(weather_info['main']['feels_like']), weather_info['wind']['speed'])
        
        bot.send_message(message.chat.id, messag)
    
schedule.every().day.at('23:17').do(get_weather)



while True:
    
    schedule.run_pending()
    time.sleep(1)
    bot.polling()
    bot.stop_polling()
