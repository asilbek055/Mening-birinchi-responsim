import telebot
import requests

bot = telebot.TeleBot('7832465485:AAGjdU5hp1BRYu0oWDHwPEk2qRt-7OUYN68')
API_key = 'a4b771dfee576ca0ef67efb8bdba43c1'
URL = 'http://api.openweathermap.org/data/2.5/forecast'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Salom shahar nomini kiriting, men sizga 5 kunlik ob-havo malumotlarini yuboraman.')

@bot.message_handler(content_types=['text'])
def send(message):
    shahar = message.text.strip()

    params= {'q': shahar, 'appid': API_key, 'units': 'metric', 'lang': 'uz'}
    response = requests.get(URL, params=params)
    data = response.json()

    if data.get('cod') != '200':
        bot.send_message(message.chat.id, 'Shahar topilmadi. Iltimos, shahar nomiga etibor bering.')
    else:
        ob_havo = f"5 kunlik ob-havo - {shahar}:\n\n"
        for i in range(0, 40, 8):  # 5 kunlik prognozdan har 8 soatni olamiz
            date = data['list'][i]['dt_txt'].split(' ')[0]  # Sana
            temp = data['list'][i]['main']['temp']
            description = data['list'][i]['weather'][0]['description']
            ob_havo += f"{date}: {temp}°C, {description}\n"
        
        bot.send_message(message.chat.id, ob_havo)

bot.polling(none_stop=True)
