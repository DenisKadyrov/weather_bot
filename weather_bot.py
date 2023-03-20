import telebot
import schedule
import time
import math
import json
import requests

token = '5432636852:AAHJDIlpx0qAP5UBFirEc3eJ623jZhRffNg'
bot = telebot.TeleBot(token)

url = 'https://api.openweathermap.org/data/2.5/weather?lat=57.1522&lon=65.5272&appid=c6c3c7f3e904530075ff6b57666c3ed0&units=metric&lang=ru'
user_id = 5250094350
gleb = 1081723619


def get_weather():
    res = requests.get(url)
    weather_info = res.json()
    recomented = get_recoment(weather_info)

    message = 'Сегодня на улице {0}, {1}°C, при этом ощущаеться как {2}°C. Ветер {3} м/с'.format(weather_info['weather'][0]['description'], 
        math.ceil(weather_info['main']['temp']), math.ceil(weather_info['main']['feels_like']), weather_info['wind']['speed'])
    
    bot.send_message(user_id, f"{message}. {recomented}.")
    bot.send_message(gleb, f"{message}. {recomented}.")

def get_recoment(info):
    if math.ceil(info['main']['temp']) <= -15:
        l = "На улице холодно, нужно одеться теплее"

    elif math.ceil(info['main']['temp']) >= -15 & math.ceil(info['main']['temp']) <= 0:
        l = 'На улице прохладно без ветровки выходить не желательно '

    elif math.ceil(info['main']['temp']) >= 0 & math.ceil(info['main']['temp']) <= 20:
        l = 'На улице сегодня тепло, оденьте что то, но не перестарайтесь'

    elif math.ceil(info['main']['temp']) > 20:
        l = 'На улице жарко, футболки будет достаточно'

    return l
    
schedule.every().day.at('21:49').do(get_weather)

while True:
    schedule.run_pending()
    time.sleep(1)