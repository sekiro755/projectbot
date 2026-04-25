import telebot
from telebot import types
from config import token

bot = telebot.TeleBot('7710261372:AAEQiGKLtOwa3OWltgl24Xgw5QM1H-N-dgo')



markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btn1 = types.KeyboardButton('Опросники')
btn2 = types.KeyboardButton('Помощь')
btn3 = types.KeyboardButton('Фидбек')
btn4 = types.KeyboardButton('Польза проекта')
btn5 = types.KeyboardButton('Главное меню')
btn6 = types.KeyboardButton('Автор проекта')
markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btn1 = types.KeyboardButton('Да')
btn2 = types.KeyboardButton('Нет')
btn3 = types.KeyboardButton('Меню')

markup2.add(btn1, btn2, btn3)

markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btn1 = types.KeyboardButton('Углекислые газы')
btn2 = types.KeyboardButton('Химических отходов')
btn3 = types.KeyboardButton('Меню')
markup3.add(btn1, btn2, btn3)

markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btn1 = types.KeyboardButton('2200')
btn2 = types.KeyboardButton('2100')
btn3 = types.KeyboardButton('Меню')
markup4.add(btn1, btn2, btn3)

markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btn1 = types.KeyboardButton('Вода, земля и продовольствие')
btn2 = types.KeyboardButton('Уголь, камень и дерево')
btn3 = types.KeyboardButton('Меню')
markup5.add(btn1, btn2, btn3)

markup6 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btn1 = types.KeyboardButton('120')
btn2 = types.KeyboardButton('140')
btn3 = types.KeyboardButton('Меню')
markup6.add(btn1, btn2, btn3)

markup7 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btn1 = types.KeyboardButton('50%')
btn2 = types.KeyboardButton('70%')
btn3 = types.KeyboardButton('Меню')
markup7.add(btn1, btn2, btn3)

markup8 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btn1 = types.KeyboardButton('67%')
btn2 = types.KeyboardButton('90%')
btn3 = types.KeyboardButton('Меню')
markup8.add(btn1, btn2, btn3)

@bot.message_handler(commands=['start'])
def start(message):
    username = message.from_user.username
    bot.send_message(message.chat.id,  "Let`s start!", reply_markup=markup)
    send_mess = f"Привет, {username}! Я твой личный опросник по знанию о глобальном потеплениим !"
    bot.send_message(message.chat.id, send_mess, reply_markup=markup)



def mess(message):
    send_mess = "Выбери подходящий вариант"
    bot.send_message(message.chat.id, send_mess, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text =='Главное меню')
def foo(message):
    final_message = "Решил попробовать что-то ещё?Выбери какое направление тебя интересует:"
    bot.send_message(message.chat.id, final_message, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text =='Да')
def foo(message):
    final_message = "Ну что первый вопрос:в результате добычи угля, нефти и газа в атмосферу выбрасываются.."
    bot.send_message(message.chat.id, final_message, reply_markup=markup3)

@bot.message_handler(func=lambda message: message.text =='Углекислые газы')
def foo(message):
    final_message = "Верно! Следующий вопрос! Если не замедлят темпы глобальных выбросов то к ... году температура может подняться до 3 градусов "
    bot.send_message(message.chat.id, final_message, reply_markup=markup4)

@bot.message_handler(func=lambda message: message.text =='Химических отходов')
def foo(message):
    final_message = "Неверно! Это нормально давай еще раз"
    bot.send_message(message.chat.id, final_message, reply_markup=markup3)

@bot.message_handler(func=lambda message: message.text =='140')
def foo(message):
    final_message = "Верно! Идем дальше и ты молодец следующий вопрос: Сегодня более ... процентов выбросов можно сократить благодаря готовым к использованию тех.разработкам"
    bot.send_message(message.chat.id, final_message, reply_markup=markup7)

@bot.message_handler(func=lambda message: message.text =='70%')
def foo(message):
    final_message = "Верно! Идем дальше на последний вопрос!: В настоящее время ... процентов стихийных бедствий классифицируются связанные с климатом и погодой."
    bot.send_message(message.chat.id, final_message, reply_markup=markup8)

@bot.message_handler(func=lambda message: message.text =='67%')
def foo(message):
    final_message = "Неверно! Давай мы уже у конца!"
    bot.send_message(message.chat.id, final_message, reply_markup=markup8)    

@bot.message_handler(func=lambda message: message.text =='90%')
def foo(message):
    final_message = "Ура! Ты все прошел! Ваш тест отправлен в музей по климатическим бедам! Есть шанс получить бесплатное личное приглашение! Спасибо за пройденный тест удачи тебе!"
    bot.send_message(message.chat.id, final_message, reply_markup=markup) 

@bot.message_handler(func=lambda message: message.text =='50%')
def foo(message):
    final_message = "Неверно! Я в тебя верю!"
    bot.send_message(message.chat.id, final_message, reply_markup=markup7)

@bot.message_handler(func=lambda message: message.text =='120')
def foo(message):
    final_message = "Неверно! Давай еще раз.."
    bot.send_message(message.chat.id, final_message, reply_markup=markup6)   

@bot.message_handler(func=lambda message: message.text =='2100')
def foo(message):
    final_message = "Ты прав друг! Следующий вопрос: Последствия изменения климата проявляются в ожесточении конкуреции ресурсов как..."
    bot.send_message(message.chat.id, final_message, reply_markup=markup5)

@bot.message_handler(func=lambda message: message.text =='Вода, земля и продовольствие')
def foo(message):
    final_message = "Молодец! Хорошо идем следующий вопрос: По оценкам всемирного банка в отсуствие действии к 2050 году более ... миллионов человек в странах Африки будут вынуждены мигрировать в пределах своих регионов."
    bot.send_message(message.chat.id, final_message, reply_markup=markup6)

@bot.message_handler(func=lambda message: message.text =='2200')
def foo(message):
    final_message = "Неверно! Попробуй другой вариант:)"
    bot.send_message(message.chat.id, final_message, reply_markup=markup4)

@bot.message_handler(func=lambda message: message.text =='Уголь, камень и дерево')
def foo(message):
    final_message = "Неверно! Может еще раз?"
    bot.send_message(message.chat.id, final_message, reply_markup=markup5)    

@bot.message_handler(func=lambda message: message.text =='Нет')
def foo(message):
    final_message = "Возращайся как будешь готов!"
    bot.send_message(message.chat.id, final_message, reply_markup=markup)    

@bot.message_handler(func=lambda message: message.text =='Меню')
def foo(message):
    final_message = "Устал? Или нужно еще почитать? Конечно! Возращайся поскорее!"
    bot.send_message(message.chat.id, final_message, reply_markup=markup)



@bot.message_handler(func=lambda message: message.text =="Опросники")
def foo(message):
    final_message = "Ну что начинаем наш тест про глобальное потепление ты готов?"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup2)

@bot.message_handler(func=lambda message: message.text =="Помощь")
def foo(message):
    final_message = "Вот пару справочников на тему потепления: https://www.un.org/ru/un75/climate-crisis-race-we-can-win и https://www.un.org/ru/climatechange/science/causes-effects-climate-change"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text =="Фидбек")
def foo(message):
    final_message = "Вот наш менеджер: (крутой стильный ник) свяжетесь с ним для вопроса или обсуждения развития проекта"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text =="Польза проекта")
def foo(message):
    final_message = "Многая молодежь не знает что делать во время глобального потепления, поэтому был создан данный проект для изучения и закрепления знаний по нему!:)"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text =="Автор проекта")
def foo(message):
    final_message = "Данный бот был создан для музея 'КЛИМАТ ПРОБЛЕМС' Владелец:@sekirows (Роман)"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

bot.polling(none_stop=True)