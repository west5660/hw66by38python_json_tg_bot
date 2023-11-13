import telebot
import hw382python, hw39python, hw391python, pogodaPskov
import pogodaPskov

bot = telebot.TeleBot('6148037034:AAGylTPYhWbrZce8J4aCULQF2x7Qns1zv5k')
bot.send_message(825113753, 'готов к работе')

@bot.message_handler(content_types=['text'])
def message(info):
    print(info.chat.id)
    if 'привет' in info.text:
        bot.send_message(info.chat.id,'privet')
    elif 'пока' in info.text:
        bot.send_message(info.chat.id,'poka')
    elif 'погода' in info.text:
        pogoda_info = pogodaPskov.get_weather()
        bot.send_message(info.chat.id, pogoda_info)
    elif 'прогноз' in info.text:
        forecast_data = pogodaPskov.get_forecast()
        for item in forecast_data:
            forecast_message = f"Прогноз на {item['dt_txt']}: Температура: {item['temp']}°C, Описание: {item['description']}"
            bot.send_message(info.chat.id, forecast_message)
    elif 'анекдот' in info.text:
        anek = hw382python.anekdot()
        bot.send_message(info.chat.id,anek)
    elif 'кино' in info.text:
        kino = hw39python.film()
        bot.send_message(info.chat.id,kino)
    elif 'новости' in info.text:
        news = hw391python.novosti
        bot.send_message(info.chat.id, news)
    else:
        bot.send_message(info.chat.id,'ya bot')
    pass

bot.polling(none_stop=True)