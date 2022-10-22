import telebot
from telebot import types
from pymongo import MongoClient
from bson.objectid import ObjectId
from time import sleep
from random import randint
import motor.motor_asyncio
# from webserver import keep_alive

bot = telebot.TeleBot('5458746308:AAGnGLiej8ytMiOCYZSSPQVZLYP1BXYrP-E')

cluster = MongoClient("mongodb+srv://palladium:rinigu77@cluster0.fzugi.mongodb.net/alhimka?retryWrites=true&w=majority")
db = cluster["alhimka"]
mess = db["rul_mess"]
users = db["rul_users"]
member = db["users"]

print("Бот запущен")

admins = ['Kana_biz2', 'AntySma']

@bot.message_handler(commands=['game_create'])
def create(message):
    if message.from_user.username in admins:
        text = f"""<b>
✅ Вы успешно создали игру с 20 призовыми местами! Введите призы.

<code>Например:\nPVP-Alpha 1г - 2 призовых места.\nШШ 2г - 1 призовое место</code>

➖➖➖➖➖➖➖➖➖➖➖➖

⚜ Bot Version: <code>1.0</code>
♻ Teh-admin: @An_gelo_chek
🤖 Chat [NEWS | UPDATES]: <a href='https://t.me/+S6vb46FmjPxhMWEy'>Click me</a></b>""".strip()
        msg = bot.send_message(message.chat.id, text, parse_mode='html', disable_web_page_preview=True)
        mess.delete_one({"_id": ObjectId("6343f98db0e7d724daacb7f9")})
        mess.insert_one({"1":"свободное","2":"свободное","3":"свободное","4":"свободное","5":"свободное","6":"свободное","7":"свободное","8":"свободное","9":"свободное","10":"свободное","11":"свободное","12":"свободное","13":"свободное","14":"свободное","15":"свободное","16":"свободное","17":"свободное","18":"свободное","19":"свободное","20":"свободное","_id": ObjectId("6343f98db0e7d724daacb7f9"),"mess_id":0, "mess_id_chat":0, "city":"","prize":""})
        bot.register_next_step_handler(msg, add_prize)
    else:
        m_id = bot.send_message(message.chat.id, "<b>❌ Доступ запрещен!</b>", parse_mode='html')
        sleep(5)
        bot.delete_message(chat_id=message.chat.id, message_id=m_id.message_id)

def add_prize(message):
    if message.from_user.username in admins:
        if message.text:
            text = f"""
    <b>
    ✅ Вы успешно добавили призы!

    <code>{message.text}</code>

    Введите город, в котором будет проводиться розыгрыш.
    </b>
    """.strip()
            msg = bot.send_message(message.chat.id, text, parse_mode = 'html')
            mess.update_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')}, {"$set": {"prize": f"{message.text}"}})
            bot.register_next_step_handler(msg, add_city)

def add_city(message):
    if message.from_user.username in admins:
        text = f"""<b>✅ Вы успешно добавили город: <code>{message.text}</code>!\n\nЧтобы подтвердить создание рулетки, нажмите "✅ Подтвердить"</b>""".strip()
        mess.update_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')}, {"$set": {"city": f"{message.text}"}})
        markup = types.InlineKeyboardMarkup()
        ok = types.InlineKeyboardButton(text = "✅ Подтвердить", callback_data = "accept_create_game")
        markup.add(ok)
        bot.send_message(message.chat.id, text, parse_mode = 'html', reply_markup = markup)

@bot.callback_query_handler(func = lambda call: True)
def accept_create_game(call):
    update__text = f"""<b>‼️‼️‼️  РУЛЕТКА  ‼️‼️‼️\n\n🌆  Город: {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['city']}  🌆\n\n💰  Призовые места  💰\n\n{mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['prize']}\n\n\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n\n\n1 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['1']}\n2 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['2']}\n3 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['3']}\n4 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['4']}\n5 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['5']}\n6 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['6']}\n7 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['7']}\n8 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['8']}\n9 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['9']}\n10 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['10']}\n11 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['11']}\n12 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['12']}\n13 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['13']}\n14 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['14']}\n15 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['15']}\n16 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['16']}\n17 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['17']}\n18 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['18']}\n19 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['19']}\n20 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['20']}\n</b>"""

    if call.data == "accept_create_game":
        markup = types.InlineKeyboardMarkup()
        participate = types.InlineKeyboardButton('Учавствовать', callback_data='participate')
        markup.add(participate)
        ids = bot.send_message(-1001671467095, update__text, parse_mode='html', reply_markup=markup)
        bot.pin_chat_message(chat_id = -1001671467095, message_id = ids.message_id)
        mess.update_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')}, {"$set": {"mess_id": ids.message_id}})
        bot.send_message(call.message.chat.id, f"""✅ Вы подтвердили создание игры!""")
        bot.answer_callback_query(call.id)

    elif call.data == 'participate':
        markup = types.InlineKeyboardMarkup(row_width=1)
        check_conditions = types.InlineKeyboardButton('Проверить условия', callback_data='check_conditions')
        markup.add(check_conditions)
        user = users.count_documents({"username": f"{call.from_user.username}"})
        if not user:
            users.insert_one({"username": f"{call.from_user.username}", "active": 1, "check_conditions": 0, "check_user_rul": '-'})
            bot.send_message(call.message.chat.id, f"""<b>‼️‼️‼️  ВНИМАНИЕ  ‼️‼️‼️\n\n<a href='http://t.me/{call.from_user.username}'>@{call.from_user.full_name}</a>, Ваши условия для участия в рулетке:\n\n- Добавить в чат 3 и более пользователей.\n- После этого нажмите на кнопку 'Проверить условия'</b>""".strip(), parse_mode='html', disable_web_page_preview=True, reply_markup=markup)
            if member.count_documents({"user_id": call.from_user.id}):
                member_bal = member.find_one({"user_id": call.from_user.id})['cash']
                member.update_one({"user_id": call.from_user.id}, {"$set": {"cash": member_bal + 20}})
            else:
                member.insert_one({"user_id": call.from_user.id, "chat_id": call.message.chat.id, "username": call.from_user.username, "fullname": call.from_user.full_name, "cash": 20})
        else:
            m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы уже учавствуете в рулетке!</b>""", parse_mode='html')
            sleep(5)
            bot.delete_message(chat_id=message.chat.id, message_id=m_id.message_id)


        bot.answer_callback_query(call.id)

    elif call.data == 'check_conditions':
        if users.find_one({"username": f"{call.from_user.username}"})['check_user_rul'] == '-':
            if users.count_documents({"author_invite": f"{call.from_user.username}"}) >= 3:
                text = f"""<b>‼️‼️‼️  ВНИМАНИЕ  ‼️‼️‼️\n\n<a href='http://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, Вы выполнили все условия для участия в рулетке! Поздравляю!\n\nЧтобы занять место, нажмите на кнопку с свободным местом!</b>""".strip()
                markup = types.InlineKeyboardMarkup()
                one1 = types.InlineKeyboardButton('1', callback_data='one1')
                one2 = types.InlineKeyboardButton('2', callback_data='one2')
                one3 = types.InlineKeyboardButton('3', callback_data='one3')
                one4 = types.InlineKeyboardButton('4', callback_data='one4')
                one5 = types.InlineKeyboardButton('5', callback_data='one5')
                one6 = types.InlineKeyboardButton('6', callback_data='one6')
                one7 = types.InlineKeyboardButton('7', callback_data='one7')
                one8 = types.InlineKeyboardButton('8', callback_data='one8')
                one9 = types.InlineKeyboardButton('9', callback_data='one9')
                one10 = types.InlineKeyboardButton('10', callback_data='one10')
                one11 = types.InlineKeyboardButton('11', callback_data='one11')
                one12 = types.InlineKeyboardButton('12', callback_data='one12')
                one13 = types.InlineKeyboardButton('13', callback_data='one13')
                one14 = types.InlineKeyboardButton('14', callback_data='one14')
                one15 = types.InlineKeyboardButton('15', callback_data='one15')
                one16 = types.InlineKeyboardButton('16', callback_data='one16')
                one17 = types.InlineKeyboardButton('17', callback_data='one17')
                one18 = types.InlineKeyboardButton('18', callback_data='one18')
                one19 = types.InlineKeyboardButton('19', callback_data='one19')
                one20 = types.InlineKeyboardButton('20', callback_data='one20')
                markup.add(one1,one2,one3,one4,one5,one6,one7,one8,one9,one10,one11,one12,one13,one14,one15,one16,one17,one18,one19,one20)
                users.update_one({"username": f"{call.from_user.username}"}, {"$set": {"check_conditions": 1}})
                bot.send_message(call.message.chat.id, text, parse_mode='html', disable_web_page_preview=True, reply_markup=markup)
            else:
                text = f"""<b>‼️‼️‼️  ВНИМАНИЕ  ‼️‼️‼️\n\n<a href='http://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, Вы не выполнили условия для участия в рулетке либо не учавствуете в ней!</b>""".strip()
                msg = bot.send_message(call.message.chat.id, text, parse_mode='html', disable_web_page_preview=True)
        else:
            m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы уже учавствуете в рулетке!</b>""", parse_mode='html')
            sleep(5)
            bot.delete_message(chat_id=message.chat.id, message_id=m_id.message_id)
        bot.answer_callback_query(call.id)

    elif call.data == "one1":
        check_user = users.count_documents({"username": f'{call.from_user.username}'})
        check_conditions = users.find_one({"username": f'{call.from_user.username}'})['check_conditions']
        check_user_rul = users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']
        mess_rul = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['1']
        if check_user:
            if check_conditions == 1:
                if check_user_rul == "-" and mess_rul == "свободное":
                    time_sleep = bot.send_message(call.message.chat.id, f"""<b>⏰ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, подождите, записываю Вас в список учащихся!\n\nПодождите: <code>3 секунды!</code></b>""", parse_mode='html', disable_web_page_preview=True).message_id
                    sleep(3)
                    users.update_one({"username": f'{call.from_user.username}'}, {"$set": {"check_user_rul": 1}})
                    mess.update_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')}, {"$set": {"1": f'@{call.from_user.username}'}})
                    mess__id = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['mess_id']
                    bot.edit_message_text(chat_id=call.message.chat.id, text=f"""<b>✅ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, Вы в списке! Ваше место: <code>{users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']}</code></b>""", message_id=time_sleep, parse_mode='html', disable_web_page_preview=True)
                    markup = types.InlineKeyboardMarkup()
                    participate = types.InlineKeyboardButton('Учавствовать', callback_data='participate')
                    markup.add(participate)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=mess__id, text=f"""<b>‼️‼️‼️  РУЛЕТКА  ‼️‼️‼️\n\n🌆  Город: {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['city']}  🌆\n\n💰  Призовые места  💰\n\n{mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['prize']}\n\n\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n\n\n1 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['1']}\n2 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['2']}\n3 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['3']}\n4 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['4']}\n5 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['5']}\n6 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['6']}\n7 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['7']}\n8 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['8']}\n9 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['9']}\n10 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['10']}\n11 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['11']}\n12 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['12']}\n13 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['13']}\n14 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['14']}\n15 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['15']}\n16 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['16']}\n17 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['17']}\n18 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['18']}\n19 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['19']}\n20 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['20']}\n</b>""", parse_mode='html', reply_markup=markup)
                else:
                    m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Данное место занято либо вы уже находитесь в списке учащихся!</b>""", parse_mode='html')
                    sleep(5)
                    bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
            else:
                m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не выполнили условия для участия в рулетке!</b>""", parse_mode='html')
                sleep(5)
                bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        else:
            m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не участвуете в рулетке!</b>""", parse_mode='html')
            sleep(5)
            bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        bot.answer_callback_query(call.id)

    elif call.data == "one2":
        check_user = users.count_documents({"username": f'{call.from_user.username}'})
        check_conditions = users.find_one({"username": f'{call.from_user.username}'})['check_conditions']
        check_user_rul = users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']
        mess_rul = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['2']
        if check_user:
            if check_conditions == 1:
                if check_user_rul == "-" and mess_rul == "свободное":
                    time_sleep = bot.send_message(call.message.chat.id, f"""<b>⏰ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, подождите, записываю Вас в список учащихся!\n\nПодождите: <code>3 секунды!</code></b>""", parse_mode='html', disable_web_page_preview=True).message_id
                    sleep(3)
                    users.update_one({"username": f'{call.from_user.username}'}, {"$set": {"check_user_rul": 2}})
                    mess.update_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')}, {"$set": {"2": f'@{call.from_user.username}'}})
                    mess__id = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['mess_id']
                    bot.edit_message_text(chat_id=call.message.chat.id, text=f"""<b>✅ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, Вы в списке! Ваше место: <code>{users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']}</code></b>""", message_id=time_sleep, parse_mode='html', disable_web_page_preview=True)
                    markup = types.InlineKeyboardMarkup()
                    participate = types.InlineKeyboardButton('Учавствовать', callback_data='participate')
                    markup.add(participate)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=mess__id, text=f"""<b>‼️‼️‼️  РУЛЕТКА  ‼️‼️‼️\n\n🌆  Город: {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['city']}  🌆\n\n💰  Призовые места  💰\n\n{mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['prize']}\n\n\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n\n\n1 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['1']}\n2 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['2']}\n3 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['3']}\n4 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['4']}\n5 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['5']}\n6 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['6']}\n7 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['7']}\n8 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['8']}\n9 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['9']}\n10 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['10']}\n11 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['11']}\n12 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['12']}\n13 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['13']}\n14 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['14']}\n15 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['15']}\n16 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['16']}\n17 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['17']}\n18 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['18']}\n19 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['19']}\n20 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['20']}\n</b>""", parse_mode='html', reply_markup=markup)
                else:
                    m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Данное место занято либо вы уже находитесь в списке учащихся!</b>""", parse_mode='html')
                    sleep(5)
                    bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
            else:
                m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не выполнили условия для участия в рулетке!</b>""", parse_mode='html')
                sleep(5)
                bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        else:
            m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не участвуете в рулетке!</b>""", parse_mode='html')
            sleep(5)
            bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        bot.answer_callback_query(call.id)

    elif call.data == "one3":
        check_user = users.count_documents({"username": f'{call.from_user.username}'})
        check_conditions = users.find_one({"username": f'{call.from_user.username}'})['check_conditions']
        check_user_rul = users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']
        mess_rul = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['3']
        if check_user:
            if check_conditions == 1:
                if check_user_rul == "-" and mess_rul == "свободное":
                    time_sleep = bot.send_message(call.message.chat.id, f"""<b>⏰ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, подождите, записываю Вас в список учащихся!\n\nПодождите: <code>3 секунды!</code></b>""", parse_mode='html', disable_web_page_preview=True).message_id
                    sleep(3)
                    users.update_one({"username": f'{call.from_user.username}'}, {"$set": {"check_user_rul": 3}})
                    mess.update_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')}, {"$set": {"3": f'@{call.from_user.username}'}})
                    mess__id = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['mess_id']
                    bot.edit_message_text(chat_id=call.message.chat.id, text=f"""<b>✅ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, Вы в списке! Ваше место: <code>{users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']}</code></b>""", message_id=time_sleep, parse_mode='html', disable_web_page_preview=True)
                    markup = types.InlineKeyboardMarkup()
                    participate = types.InlineKeyboardButton('Учавствовать', callback_data='participate')
                    markup.add(participate)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=mess__id, text=f"""<b>‼️‼️‼️  РУЛЕТКА  ‼️‼️‼️\n\n🌆  Город: {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['city']}  🌆\n\n💰  Призовые места  💰\n\n{mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['prize']}\n\n\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n\n\n1 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['1']}\n2 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['2']}\n3 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['3']}\n4 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['4']}\n5 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['5']}\n6 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['6']}\n7 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['7']}\n8 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['8']}\n9 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['9']}\n10 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['10']}\n11 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['11']}\n12 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['12']}\n13 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['13']}\n14 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['14']}\n15 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['15']}\n16 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['16']}\n17 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['17']}\n18 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['18']}\n19 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['19']}\n20 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['20']}\n</b>""", parse_mode='html', reply_markup=markup)
                else:
                    m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Данное место занято либо вы уже находитесь в списке учащихся!</b>""", parse_mode='html')
                    sleep(5)
                    bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
            else:
                m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не выполнили условия для участия в рулетке!</b>""", parse_mode='html')
                sleep(5)
                bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        else:
            m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не участвуете в рулетке!</b>""", parse_mode='html')
            sleep(5)
            bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        bot.answer_callback_query(call.id)

    elif call.data == "one4":
        check_user = users.count_documents({"username": f'{call.from_user.username}'})
        check_conditions = users.find_one({"username": f'{call.from_user.username}'})['check_conditions']
        check_user_rul = users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']
        mess_rul = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['4']
        if check_user:
            if check_conditions == 1:
                if check_user_rul == "-" and mess_rul == "свободное":
                    time_sleep = bot.send_message(call.message.chat.id, f"""<b>⏰ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, подождите, записываю Вас в список учащихся!\n\nПодождите: <code>3 секунды!</code></b>""", parse_mode='html', disable_web_page_preview=True).message_id
                    sleep(3)
                    users.update_one({"username": f'{call.from_user.username}'}, {"$set": {"check_user_rul": 4}})
                    mess.update_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')}, {"$set": {"4": f'@{call.from_user.username}'}})
                    mess__id = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['mess_id']
                    bot.edit_message_text(chat_id=call.message.chat.id, text=f"""<b>✅ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, Вы в списке! Ваше место: <code>{users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']}</code></b>""", message_id=time_sleep, parse_mode='html', disable_web_page_preview=True)
                    markup = types.InlineKeyboardMarkup()
                    participate = types.InlineKeyboardButton('Учавствовать', callback_data='participate')
                    markup.add(participate)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=mess__id, text=f"""<b>‼️‼️‼️  РУЛЕТКА  ‼️‼️‼️\n\n🌆  Город: {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['city']}  🌆\n\n💰  Призовые места  💰\n\n{mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['prize']}\n\n\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n\n\n1 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['1']}\n2 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['2']}\n3 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['3']}\n4 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['4']}\n5 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['5']}\n6 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['6']}\n7 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['7']}\n8 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['8']}\n9 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['9']}\n10 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['10']}\n11 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['11']}\n12 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['12']}\n13 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['13']}\n14 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['14']}\n15 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['15']}\n16 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['16']}\n17 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['17']}\n18 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['18']}\n19 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['19']}\n20 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['20']}\n</b>""", parse_mode='html', reply_markup=markup)
                else:
                    m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Данное место занято либо вы уже находитесь в списке учащихся!</b>""", parse_mode='html')
                    sleep(5)
                    bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
            else:
                m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не выполнили условия для участия в рулетке!</b>""", parse_mode='html')
                sleep(5)
                bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        else:
            m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не участвуете в рулетке!</b>""", parse_mode='html')
            sleep(5)
            bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        bot.answer_callback_query(call.id)

    elif call.data == "one5":
        check_user = users.count_documents({"username": f'{call.from_user.username}'})
        check_conditions = users.find_one({"username": f'{call.from_user.username}'})['check_conditions']
        check_user_rul = users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']
        mess_rul = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['5']
        if check_user:
            if check_conditions == 1:
                if check_user_rul == "-" and mess_rul == "свободное":
                    time_sleep = bot.send_message(call.message.chat.id, f"""<b>⏰ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, подождите, записываю Вас в список учащихся!\n\nПодождите: <code>3 секунды!</code></b>""", parse_mode='html', disable_web_page_preview=True).message_id
                    sleep(3)
                    users.update_one({"username": f'{call.from_user.username}'}, {"$set": {"check_user_rul": 5}})
                    mess.update_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')}, {"$set": {"5": f'@{call.from_user.username}'}})
                    mess__id = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['mess_id']
                    bot.edit_message_text(chat_id=call.message.chat.id, text=f"""<b>✅ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, Вы в списке! Ваше место: <code>{users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']}</code></b>""", message_id=time_sleep, parse_mode='html', disable_web_page_preview=True)
                    markup = types.InlineKeyboardMarkup()
                    participate = types.InlineKeyboardButton('Учавствовать', callback_data='participate')
                    markup.add(participate)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=mess__id, text=f"""<b>‼️‼️‼️  РУЛЕТКА  ‼️‼️‼️\n\n🌆  Город: {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['city']}  🌆\n\n💰  Призовые места  💰\n\n{mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['prize']}\n\n\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n\n\n1 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['1']}\n2 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['2']}\n3 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['3']}\n4 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['4']}\n5 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['5']}\n6 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['6']}\n7 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['7']}\n8 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['8']}\n9 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['9']}\n10 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['10']}\n11 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['11']}\n12 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['12']}\n13 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['13']}\n14 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['14']}\n15 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['15']}\n16 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['16']}\n17 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['17']}\n18 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['18']}\n19 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['19']}\n20 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['20']}\n</b>""", parse_mode='html', reply_markup=markup)
                else:
                    m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Данное место занято либо вы уже находитесь в списке учащихся!</b>""", parse_mode='html')
                    sleep(5)
                    bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
            else:
                m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не выполнили условия для участия в рулетке!</b>""", parse_mode='html')
                sleep(5)
                bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        else:
            m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не участвуете в рулетке!</b>""", parse_mode='html')
            sleep(5)
            bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        bot.answer_callback_query(call.id)

    elif call.data == "one6":
        check_user = users.count_documents({"username": f'{call.from_user.username}'})
        check_conditions = users.find_one({"username": f'{call.from_user.username}'})['check_conditions']
        check_user_rul = users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']
        mess_rul = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['6']
        if check_user:
            if check_conditions == 1:
                if check_user_rul == "-" and mess_rul == "свободное":
                    time_sleep = bot.send_message(call.message.chat.id, f"""<b>⏰ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, подождите, записываю Вас в список учащихся!\n\nПодождите: <code>3 секунды!</code></b>""", parse_mode='html', disable_web_page_preview=True).message_id
                    sleep(3)
                    users.update_one({"username": f'{call.from_user.username}'}, {"$set": {"check_user_rul": 6}})
                    mess.update_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')}, {"$set": {"6": f'@{call.from_user.username}'}})
                    mess__id = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['mess_id']
                    bot.edit_message_text(chat_id=call.message.chat.id, text=f"""<b>✅ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, Вы в списке! Ваше место: <code>{users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']}</code></b>""", message_id=time_sleep, parse_mode='html', disable_web_page_preview=True)
                    markup = types.InlineKeyboardMarkup()
                    participate = types.InlineKeyboardButton('Учавствовать', callback_data='participate')
                    markup.add(participate)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=mess__id, text=f"""<b>‼️‼️‼️  РУЛЕТКА  ‼️‼️‼️\n\n🌆  Город: {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['city']}  🌆\n\n💰  Призовые места  💰\n\n{mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['prize']}\n\n\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n\n\n1 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['1']}\n2 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['2']}\n3 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['3']}\n4 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['4']}\n5 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['5']}\n6 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['6']}\n7 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['7']}\n8 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['8']}\n9 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['9']}\n10 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['10']}\n11 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['11']}\n12 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['12']}\n13 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['13']}\n14 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['14']}\n15 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['15']}\n16 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['16']}\n17 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['17']}\n18 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['18']}\n19 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['19']}\n20 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['20']}\n</b>""", parse_mode='html', reply_markup=markup)
                else:
                    m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Данное место занято либо вы уже находитесь в списке учащихся!</b>""", parse_mode='html')
                    sleep(5)
                    bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
            else:
                m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не выполнили условия для участия в рулетке!</b>""", parse_mode='html')
                sleep(5)
                bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        else:
            m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не участвуете в рулетке!</b>""", parse_mode='html')
            sleep(5)
            bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        bot.answer_callback_query(call.id)

    elif call.data == "one7":
        check_user = users.count_documents({"username": f'{call.from_user.username}'})
        check_conditions = users.find_one({"username": f'{call.from_user.username}'})['check_conditions']
        check_user_rul = users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']
        mess_rul = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['7']
        if check_user:
            if check_conditions == 1:
                if check_user_rul == "-" and mess_rul == "свободное":
                    time_sleep = bot.send_message(call.message.chat.id, f"""<b>⏰ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, подождите, записываю Вас в список учащихся!\n\nПодождите: <code>3 секунды!</code></b>""", parse_mode='html', disable_web_page_preview=True).message_id
                    sleep(3)
                    users.update_one({"username": f'{call.from_user.username}'}, {"$set": {"check_user_rul": 7}})
                    mess.update_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')}, {"$set": {"7": f'@{call.from_user.username}'}})
                    mess__id = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['mess_id']
                    bot.edit_message_text(chat_id=call.message.chat.id, text=f"""<b>✅ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, Вы в списке! Ваше место: <code>{users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']}</code></b>""", message_id=time_sleep, parse_mode='html', disable_web_page_preview=True)
                    markup = types.InlineKeyboardMarkup()
                    participate = types.InlineKeyboardButton('Учавствовать', callback_data='participate')
                    markup.add(participate)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=mess__id, text=f"""<b>‼️‼️‼️  РУЛЕТКА  ‼️‼️‼️\n\n🌆  Город: {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['city']}  🌆\n\n💰  Призовые места  💰\n\n{mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['prize']}\n\n\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n\n\n1 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['1']}\n2 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['2']}\n3 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['3']}\n4 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['4']}\n5 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['5']}\n6 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['6']}\n7 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['7']}\n8 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['8']}\n9 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['9']}\n10 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['10']}\n11 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['11']}\n12 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['12']}\n13 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['13']}\n14 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['14']}\n15 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['15']}\n16 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['16']}\n17 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['17']}\n18 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['18']}\n19 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['19']}\n20 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['20']}\n</b>""", parse_mode='html', reply_markup=markup)
                else:
                    m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Данное место занято либо вы уже находитесь в списке учащихся!</b>""", parse_mode='html')
                    sleep(5)
                    bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
            else:
                m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не выполнили условия для участия в рулетке!</b>""", parse_mode='html')
                sleep(5)
                bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        else:
            m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не участвуете в рулетке!</b>""", parse_mode='html')
            sleep(5)
            bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        bot.answer_callback_query(call.id)

    elif call.data == "one8":
        check_user = users.count_documents({"username": f'{call.from_user.username}'})
        check_conditions = users.find_one({"username": f'{call.from_user.username}'})['check_conditions']
        check_user_rul = users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']
        mess_rul = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['8']
        if check_user:
            if check_conditions == 1:
                if check_user_rul == "-" and mess_rul == "свободное":
                    time_sleep = bot.send_message(call.message.chat.id, f"""<b>⏰ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, подождите, записываю Вас в список учащихся!\n\nПодождите: <code>3 секунды!</code></b>""", parse_mode='html', disable_web_page_preview=True).message_id
                    sleep(3)
                    users.update_one({"username": f'{call.from_user.username}'}, {"$set": {"check_user_rul": 8}})
                    mess.update_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')}, {"$set": {"8": f'@{call.from_user.username}'}})
                    mess__id = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['mess_id']
                    bot.edit_message_text(chat_id=call.message.chat.id, text=f"""<b>✅ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, Вы в списке! Ваше место: <code>{users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']}</code></b>""", message_id=time_sleep, parse_mode='html', disable_web_page_preview=True)
                    markup = types.InlineKeyboardMarkup()
                    participate = types.InlineKeyboardButton('Учавствовать', callback_data='participate')
                    markup.add(participate)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=mess__id, text=f"""<b>‼️‼️‼️  РУЛЕТКА  ‼️‼️‼️\n\n🌆  Город: {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['city']}  🌆\n\n💰  Призовые места  💰\n\n{mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['prize']}\n\n\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n\n\n1 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['1']}\n2 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['2']}\n3 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['3']}\n4 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['4']}\n5 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['5']}\n6 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['6']}\n7 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['7']}\n8 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['8']}\n9 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['9']}\n10 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['10']}\n11 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['11']}\n12 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['12']}\n13 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['13']}\n14 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['14']}\n15 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['15']}\n16 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['16']}\n17 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['17']}\n18 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['18']}\n19 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['19']}\n20 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['20']}\n</b>""", parse_mode='html', reply_markup=markup)
                else:
                    m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Данное место занято либо вы уже находитесь в списке учащихся!</b>""", parse_mode='html')
                    sleep(5)
                    bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
            else:
                m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не выполнили условия для участия в рулетке!</b>""", parse_mode='html')
                sleep(5)
                bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        else:
            m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не участвуете в рулетке!</b>""", parse_mode='html')
            sleep(5)
            bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        bot.answer_callback_query(call.id)

    elif call.data == "one9":
        check_user = users.count_documents({"username": f'{call.from_user.username}'})
        check_conditions = users.find_one({"username": f'{call.from_user.username}'})['check_conditions']
        check_user_rul = users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']
        mess_rul = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['9']
        if check_user:
            if check_conditions == 1:
                if check_user_rul == "-" and mess_rul == "свободное":
                    time_sleep = bot.send_message(call.message.chat.id, f"""<b>⏰ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, подождите, записываю Вас в список учащихся!\n\nПодождите: <code>3 секунды!</code></b>""", parse_mode='html', disable_web_page_preview=True).message_id
                    sleep(3)
                    users.update_one({"username": f'{call.from_user.username}'}, {"$set": {"check_user_rul": 9}})
                    mess.update_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')}, {"$set": {"9": f'@{call.from_user.username}'}})
                    mess__id = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['mess_id']
                    bot.edit_message_text(chat_id=call.message.chat.id, text=f"""<b>✅ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, Вы в списке! Ваше место: <code>{users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']}</code></b>""", message_id=time_sleep, parse_mode='html', disable_web_page_preview=True)
                    markup = types.InlineKeyboardMarkup()
                    participate = types.InlineKeyboardButton('Учавствовать', callback_data='participate')
                    markup.add(participate)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=mess__id, text=f"""<b>‼️‼️‼️  РУЛЕТКА  ‼️‼️‼️\n\n🌆  Город: {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['city']}  🌆\n\n💰  Призовые места  💰\n\n{mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['prize']}\n\n\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n\n\n1 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['1']}\n2 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['2']}\n3 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['3']}\n4 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['4']}\n5 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['5']}\n6 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['6']}\n7 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['7']}\n8 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['8']}\n9 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['9']}\n10 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['10']}\n11 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['11']}\n12 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['12']}\n13 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['13']}\n14 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['14']}\n15 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['15']}\n16 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['16']}\n17 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['17']}\n18 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['18']}\n19 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['19']}\n20 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['20']}\n</b>""", parse_mode='html', reply_markup=markup)
                else:
                    m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Данное место занято либо вы уже находитесь в списке учащихся!</b>""", parse_mode='html')
                    sleep(5)
                    bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
            else:
                m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не выполнили условия для участия в рулетке!</b>""", parse_mode='html')
                sleep(5)
                bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        else:
            m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не участвуете в рулетке!</b>""", parse_mode='html')
            sleep(5)
            bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        bot.answer_callback_query(call.id)

    elif call.data == "one10":
        check_user = users.count_documents({"username": f'{call.from_user.username}'})
        check_conditions = users.find_one({"username": f'{call.from_user.username}'})['check_conditions']
        check_user_rul = users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']
        mess_rul = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['10']
        if check_user:
            if check_conditions == 1:
                if check_user_rul == "-" and mess_rul == "свободное":
                    time_sleep = bot.send_message(call.message.chat.id, f"""<b>⏰ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, подождите, записываю Вас в список учащихся!\n\nПодождите: <code>3 секунды!</code></b>""", parse_mode='html', disable_web_page_preview=True).message_id
                    sleep(3)
                    users.update_one({"username": f'{call.from_user.username}'}, {"$set": {"check_user_rul": 10}})
                    mess.update_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')}, {"$set": {"10": f'@{call.from_user.username}'}})
                    mess__id = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['mess_id']
                    bot.edit_message_text(chat_id=call.message.chat.id, text=f"""<b>✅ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, Вы в списке! Ваше место: <code>{users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']}</code></b>""", message_id=time_sleep, parse_mode='html', disable_web_page_preview=True)
                    markup = types.InlineKeyboardMarkup()
                    participate = types.InlineKeyboardButton('Учавствовать', callback_data='participate')
                    markup.add(participate)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=mess__id, text=f"""<b>‼️‼️‼️  РУЛЕТКА  ‼️‼️‼️\n\n🌆  Город: {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['city']}  🌆\n\n💰  Призовые места  💰\n\n{mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['prize']}\n\n\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n\n\n1 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['1']}\n2 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['2']}\n3 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['3']}\n4 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['4']}\n5 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['5']}\n6 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['6']}\n7 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['7']}\n8 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['8']}\n9 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['9']}\n10 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['10']}\n11 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['11']}\n12 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['12']}\n13 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['13']}\n14 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['14']}\n15 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['15']}\n16 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['16']}\n17 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['17']}\n18 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['18']}\n19 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['19']}\n20 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['20']}\n</b>""", parse_mode='html', reply_markup=markup)
                else:
                    m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Данное место занято либо вы уже находитесь в списке учащихся!</b>""", parse_mode='html')
                    sleep(5)
                    bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
            else:
                m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не выполнили условия для участия в рулетке!</b>""", parse_mode='html')
                sleep(5)
                bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        else:
            m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не участвуете в рулетке!</b>""", parse_mode='html')
            sleep(5)
            bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        bot.answer_callback_query(call.id)

    elif call.data == "one11":
        check_user = users.count_documents({"username": f'{call.from_user.username}'})
        check_conditions = users.find_one({"username": f'{call.from_user.username}'})['check_conditions']
        check_user_rul = users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']
        mess_rul = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['11']
        if check_user:
            if check_conditions == 1:
                if check_user_rul == "-" and mess_rul == "свободное":
                    time_sleep = bot.send_message(call.message.chat.id, f"""<b>⏰ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, подождите, записываю Вас в список учащихся!\n\nПодождите: <code>3 секунды!</code></b>""", parse_mode='html', disable_web_page_preview=True).message_id
                    sleep(3)
                    users.update_one({"username": f'{call.from_user.username}'}, {"$set": {"check_user_rul": 11}})
                    mess.update_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')}, {"$set": {"11": f'@{call.from_user.username}'}})
                    mess__id = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['mess_id']
                    bot.edit_message_text(chat_id=call.message.chat.id, text=f"""<b>✅ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, Вы в списке! Ваше место: <code>{users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']}</code></b>""", message_id=time_sleep, parse_mode='html', disable_web_page_preview=True)
                    markup = types.InlineKeyboardMarkup()
                    participate = types.InlineKeyboardButton('Учавствовать', callback_data='participate')
                    markup.add(participate)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=mess__id, text=f"""<b>‼️‼️‼️  РУЛЕТКА  ‼️‼️‼️\n\n🌆  Город: {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['city']}  🌆\n\n💰  Призовые места  💰\n\n{mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['prize']}\n\n\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n\n\n1 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['1']}\n2 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['2']}\n3 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['3']}\n4 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['4']}\n5 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['5']}\n6 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['6']}\n7 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['7']}\n8 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['8']}\n9 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['9']}\n10 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['10']}\n11 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['11']}\n12 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['12']}\n13 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['13']}\n14 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['14']}\n15 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['15']}\n16 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['16']}\n17 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['17']}\n18 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['18']}\n19 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['19']}\n20 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['20']}\n</b>""", parse_mode='html', reply_markup=markup)
                else:
                    m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Данное место занято либо вы уже находитесь в списке учащихся!</b>""", parse_mode='html')
                    sleep(5)
                    bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
            else:
                m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не выполнили условия для участия в рулетке!</b>""", parse_mode='html')
                sleep(5)
                bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        else:
            m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не участвуете в рулетке!</b>""", parse_mode='html')
            sleep(5)
            bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        bot.answer_callback_query(call.id)

    elif call.data == "one12":
        check_user = users.count_documents({"username": f'{call.from_user.username}'})
        check_conditions = users.find_one({"username": f'{call.from_user.username}'})['check_conditions']
        check_user_rul = users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']
        mess_rul = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['12']
        if check_user:
            if check_conditions == 1:
                if check_user_rul == "-" and mess_rul == "свободное":
                    time_sleep = bot.send_message(call.message.chat.id, f"""<b>⏰ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, подождите, записываю Вас в список учащихся!\n\nПодождите: <code>3 секунды!</code></b>""", parse_mode='html', disable_web_page_preview=True).message_id
                    sleep(3)
                    users.update_one({"username": f'{call.from_user.username}'}, {"$set": {"check_user_rul": 12}})
                    mess.update_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')}, {"$set": {"12": f'@{call.from_user.username}'}})
                    mess__id = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['mess_id']
                    bot.edit_message_text(chat_id=call.message.chat.id, text=f"""<b>✅ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, Вы в списке! Ваше место: <code>{users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']}</code></b>""", message_id=time_sleep, parse_mode='html', disable_web_page_preview=True)
                    markup = types.InlineKeyboardMarkup()
                    participate = types.InlineKeyboardButton('Учавствовать', callback_data='participate')
                    markup.add(participate)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=mess__id, text=f"""<b>‼️‼️‼️  РУЛЕТКА  ‼️‼️‼️\n\n🌆  Город: {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['city']}  🌆\n\n💰  Призовые места  💰\n\n{mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['prize']}\n\n\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n\n\n1 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['1']}\n2 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['2']}\n3 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['3']}\n4 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['4']}\n5 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['5']}\n6 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['6']}\n7 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['7']}\n8 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['8']}\n9 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['9']}\n10 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['10']}\n11 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['11']}\n12 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['12']}\n13 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['13']}\n14 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['14']}\n15 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['15']}\n16 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['16']}\n17 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['17']}\n18 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['18']}\n19 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['19']}\n20 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['20']}\n</b>""", parse_mode='html', reply_markup=markup)
                else:
                    m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Данное место занято либо вы уже находитесь в списке учащихся!</b>""", parse_mode='html')
                    sleep(5)
                    bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
            else:
                m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не выполнили условия для участия в рулетке!</b>""", parse_mode='html')
                sleep(5)
                bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        else:
            m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не участвуете в рулетке!</b>""", parse_mode='html')
            sleep(5)
            bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        bot.answer_callback_query(call.id)

    elif call.data == "one13":
        check_user = users.count_documents({"username": f'{call.from_user.username}'})
        check_conditions = users.find_one({"username": f'{call.from_user.username}'})['check_conditions']
        check_user_rul = users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']
        mess_rul = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['13']
        if check_user:
            if check_conditions == 1:
                if check_user_rul == "-" and mess_rul == "свободное":
                    time_sleep = bot.send_message(call.message.chat.id, f"""<b>⏰ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, подождите, записываю Вас в список учащихся!\n\nПодождите: <code>3 секунды!</code></b>""", parse_mode='html', disable_web_page_preview=True).message_id
                    sleep(3)
                    users.update_one({"username": f'{call.from_user.username}'}, {"$set": {"check_user_rul": 13}})
                    mess.update_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')}, {"$set": {"13": f'@{call.from_user.username}'}})
                    mess__id = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['mess_id']
                    bot.edit_message_text(chat_id=call.message.chat.id, text=f"""<b>✅ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, Вы в списке! Ваше место: <code>{users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']}</code></b>""", message_id=time_sleep, parse_mode='html', disable_web_page_preview=True)
                    markup = types.InlineKeyboardMarkup()
                    participate = types.InlineKeyboardButton('Учавствовать', callback_data='participate')
                    markup.add(participate)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=mess__id, text=f"""<b>‼️‼️‼️  РУЛЕТКА  ‼️‼️‼️\n\n🌆  Город: {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['city']}  🌆\n\n💰  Призовые места  💰\n\n{mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['prize']}\n\n\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n\n\n1 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['1']}\n2 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['2']}\n3 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['3']}\n4 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['4']}\n5 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['5']}\n6 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['6']}\n7 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['7']}\n8 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['8']}\n9 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['9']}\n10 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['10']}\n11 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['11']}\n12 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['12']}\n13 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['13']}\n14 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['14']}\n15 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['15']}\n16 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['16']}\n17 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['17']}\n18 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['18']}\n19 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['19']}\n20 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['20']}\n</b>""", parse_mode='html', reply_markup=markup)
                else:
                    m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Данное место занято либо вы уже находитесь в списке учащихся!</b>""", parse_mode='html')
                    sleep(5)
                    bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
            else:
                m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не выполнили условия для участия в рулетке!</b>""", parse_mode='html')
                sleep(5)
                bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        else:
            m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не участвуете в рулетке!</b>""", parse_mode='html')
            sleep(5)
            bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        bot.answer_callback_query(call.id)

    elif call.data == "one14":
        check_user = users.count_documents({"username": f'{call.from_user.username}'})
        check_conditions = users.find_one({"username": f'{call.from_user.username}'})['check_conditions']
        check_user_rul = users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']
        mess_rul = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['14']
        if check_user:
            if check_conditions == 1:
                if check_user_rul == "-" and mess_rul == "свободное":
                    time_sleep = bot.send_message(call.message.chat.id, f"""<b>⏰ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, подождите, записываю Вас в список учащихся!\n\nПодождите: <code>3 секунды!</code></b>""", parse_mode='html', disable_web_page_preview=True).message_id
                    sleep(3)
                    users.update_one({"username": f'{call.from_user.username}'}, {"$set": {"check_user_rul": 14}})
                    mess.update_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')}, {"$set": {"14": f'@{call.from_user.username}'}})
                    mess__id = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['mess_id']
                    bot.edit_message_text(chat_id=call.message.chat.id, text=f"""<b>✅ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, Вы в списке! Ваше место: <code>{users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']}</code></b>""", message_id=time_sleep, parse_mode='html', disable_web_page_preview=True)
                    markup = types.InlineKeyboardMarkup()
                    participate = types.InlineKeyboardButton('Учавствовать', callback_data='participate')
                    markup.add(participate)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=mess__id, text=f"""<b>‼️‼️‼️  РУЛЕТКА  ‼️‼️‼️\n\n🌆  Город: {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['city']}  🌆\n\n💰  Призовые места  💰\n\n{mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['prize']}\n\n\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n\n\n1 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['1']}\n2 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['2']}\n3 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['3']}\n4 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['4']}\n5 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['5']}\n6 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['6']}\n7 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['7']}\n8 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['8']}\n9 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['9']}\n10 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['10']}\n11 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['11']}\n12 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['12']}\n13 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['13']}\n14 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['14']}\n15 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['15']}\n16 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['16']}\n17 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['17']}\n18 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['18']}\n19 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['19']}\n20 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['20']}\n</b>""", parse_mode='html', reply_markup=markup)
                else:
                    m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Данное место занято либо вы уже находитесь в списке учащихся!</b>""", parse_mode='html')
                    sleep(5)
                    bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
            else:
                m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не выполнили условия для участия в рулетке!</b>""", parse_mode='html')
                sleep(5)
                bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        else:
            m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не участвуете в рулетке!</b>""", parse_mode='html')
            sleep(5)
            bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        bot.answer_callback_query(call.id)

    elif call.data == "one15":
        check_user = users.count_documents({"username": f'{call.from_user.username}'})
        check_conditions = users.find_one({"username": f'{call.from_user.username}'})['check_conditions']
        check_user_rul = users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']
        mess_rul = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['15']
        if check_user:
            if check_conditions == 1:
                if check_user_rul == "-" and mess_rul == "свободное":
                    time_sleep = bot.send_message(call.message.chat.id, f"""<b>⏰ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, подождите, записываю Вас в список учащихся!\n\nПодождите: <code>3 секунды!</code></b>""", parse_mode='html', disable_web_page_preview=True).message_id
                    sleep(3)
                    users.update_one({"username": f'{call.from_user.username}'}, {"$set": {"check_user_rul": 15}})
                    mess.update_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')}, {"$set": {"15": f'@{call.from_user.username}'}})
                    mess__id = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['mess_id']
                    bot.edit_message_text(chat_id=call.message.chat.id, text=f"""<b>✅ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, Вы в списке! Ваше место: <code>{users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']}</code></b>""", message_id=time_sleep, parse_mode='html', disable_web_page_preview=True)
                    markup = types.InlineKeyboardMarkup()
                    participate = types.InlineKeyboardButton('Учавствовать', callback_data='participate')
                    markup.add(participate)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=mess__id, text=f"""<b>‼️‼️‼️  РУЛЕТКА  ‼️‼️‼️\n\n🌆  Город: {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['city']}  🌆\n\n💰  Призовые места  💰\n\n{mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['prize']}\n\n\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n\n\n1 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['1']}\n2 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['2']}\n3 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['3']}\n4 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['4']}\n5 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['5']}\n6 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['6']}\n7 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['7']}\n8 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['8']}\n9 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['9']}\n10 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['10']}\n11 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['11']}\n12 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['12']}\n13 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['13']}\n14 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['14']}\n15 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['15']}\n16 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['16']}\n17 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['17']}\n18 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['18']}\n19 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['19']}\n20 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['20']}\n</b>""", parse_mode='html', reply_markup=markup)
                else:
                    m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Данное место занято либо вы уже находитесь в списке учащихся!</b>""", parse_mode='html')
                    sleep(5)
                    bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
            else:
                m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не выполнили условия для участия в рулетке!</b>""", parse_mode='html')
                sleep(5)
                bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        else:
            m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не участвуете в рулетке!</b>""", parse_mode='html')
            sleep(5)
            bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        bot.answer_callback_query(call.id)

    elif call.data == "one16":
        check_user = users.count_documents({"username": f'{call.from_user.username}'})
        check_conditions = users.find_one({"username": f'{call.from_user.username}'})['check_conditions']
        check_user_rul = users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']
        mess_rul = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['16']
        if check_user:
            if check_conditions == 1:
                if check_user_rul == "-" and mess_rul == "свободное":
                    time_sleep = bot.send_message(call.message.chat.id, f"""<b>⏰ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, подождите, записываю Вас в список учащихся!\n\nПодождите: <code>3 секунды!</code></b>""", parse_mode='html', disable_web_page_preview=True).message_id
                    sleep(3)
                    users.update_one({"username": f'{call.from_user.username}'}, {"$set": {"check_user_rul": 16}})
                    mess.update_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')}, {"$set": {"16": f'@{call.from_user.username}'}})
                    mess__id = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['mess_id']
                    bot.edit_message_text(chat_id=call.message.chat.id, text=f"""<b>✅ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, Вы в списке! Ваше место: <code>{users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']}</code></b>""", message_id=time_sleep, parse_mode='html', disable_web_page_preview=True)
                    markup = types.InlineKeyboardMarkup()
                    participate = types.InlineKeyboardButton('Учавствовать', callback_data='participate')
                    markup.add(participate)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=mess__id, text=f"""<b>‼️‼️‼️  РУЛЕТКА  ‼️‼️‼️\n\n🌆  Город: {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['city']}  🌆\n\n💰  Призовые места  💰\n\n{mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['prize']}\n\n\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n\n\n1 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['1']}\n2 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['2']}\n3 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['3']}\n4 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['4']}\n5 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['5']}\n6 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['6']}\n7 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['7']}\n8 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['8']}\n9 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['9']}\n10 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['10']}\n11 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['11']}\n12 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['12']}\n13 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['13']}\n14 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['14']}\n15 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['15']}\n16 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['16']}\n17 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['17']}\n18 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['18']}\n19 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['19']}\n20 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['20']}\n</b>""", parse_mode='html', reply_markup=markup)
                else:
                    m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Данное место занято либо вы уже находитесь в списке учащихся!</b>""", parse_mode='html')
                    sleep(5)
                    bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
            else:
                m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не выполнили условия для участия в рулетке!</b>""", parse_mode='html')
                sleep(5)
                bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        else:
            m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не участвуете в рулетке!</b>""", parse_mode='html')
            sleep(5)
            bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        bot.answer_callback_query(call.id)

    elif call.data == "one17":
        check_user = users.count_documents({"username": f'{call.from_user.username}'})
        check_conditions = users.find_one({"username": f'{call.from_user.username}'})['check_conditions']
        check_user_rul = users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']
        mess_rul = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['17']
        if check_user:
            if check_conditions == 1:
                if check_user_rul == "-" and mess_rul == "свободное":
                    time_sleep = bot.send_message(call.message.chat.id, f"""<b>⏰ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, подождите, записываю Вас в список учащихся!\n\nПодождите: <code>3 секунды!</code></b>""", parse_mode='html', disable_web_page_preview=True).message_id
                    sleep(3)
                    users.update_one({"username": f'{call.from_user.username}'}, {"$set": {"check_user_rul": 17}})
                    mess.update_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')}, {"$set": {"17": f'@{call.from_user.username}'}})
                    mess__id = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['mess_id']
                    bot.edit_message_text(chat_id=call.message.chat.id, text=f"""<b>✅ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, Вы в списке! Ваше место: <code>{users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']}</code></b>""", message_id=time_sleep, parse_mode='html', disable_web_page_preview=True)
                    markup = types.InlineKeyboardMarkup()
                    participate = types.InlineKeyboardButton('Учавствовать', callback_data='participate')
                    markup.add(participate)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=mess__id, text=f"""<b>‼️‼️‼️  РУЛЕТКА  ‼️‼️‼️\n\n🌆  Город: {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['city']}  🌆\n\n💰  Призовые места  💰\n\n{mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['prize']}\n\n\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n\n\n1 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['1']}\n2 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['2']}\n3 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['3']}\n4 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['4']}\n5 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['5']}\n6 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['6']}\n7 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['7']}\n8 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['8']}\n9 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['9']}\n10 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['10']}\n11 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['11']}\n12 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['12']}\n13 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['13']}\n14 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['14']}\n15 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['15']}\n16 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['16']}\n17 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['17']}\n18 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['18']}\n19 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['19']}\n20 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['20']}\n</b>""", parse_mode='html', reply_markup=markup)
                else:
                    m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Данное место занято либо вы уже находитесь в списке учащихся!</b>""", parse_mode='html')
                    sleep(5)
                    bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
            else:
                m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не выполнили условия для участия в рулетке!</b>""", parse_mode='html')
                sleep(5)
                bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        else:
            m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не участвуете в рулетке!</b>""", parse_mode='html')
            sleep(5)
            bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        bot.answer_callback_query(call.id)

    elif call.data == "one18":
        check_user = users.count_documents({"username": f'{call.from_user.username}'})
        check_conditions = users.find_one({"username": f'{call.from_user.username}'})['check_conditions']
        check_user_rul = users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']
        mess_rul = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['18']
        if check_user:
            if check_conditions == 1:
                if check_user_rul == "-" and mess_rul == "свободное":
                    time_sleep = bot.send_message(call.message.chat.id, f"""<b>⏰ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, подождите, записываю Вас в список учащихся!\n\nПодождите: <code>3 секунды!</code></b>""", parse_mode='html', disable_web_page_preview=True).message_id
                    sleep(3)
                    users.update_one({"username": f'{call.from_user.username}'}, {"$set": {"check_user_rul": 18}})
                    mess.update_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')}, {"$set": {"18": f'@{call.from_user.username}'}})
                    mess__id = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['mess_id']
                    bot.edit_message_text(chat_id=call.message.chat.id, text=f"""<b>✅ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, Вы в списке! Ваше место: <code>{users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']}</code></b>""", message_id=time_sleep, parse_mode='html', disable_web_page_preview=True)
                    markup = types.InlineKeyboardMarkup()
                    participate = types.InlineKeyboardButton('Учавствовать', callback_data='participate')
                    markup.add(participate)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=mess__id, text=f"""<b>‼️‼️‼️  РУЛЕТКА  ‼️‼️‼️\n\n🌆  Город: {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['city']}  🌆\n\n💰  Призовые места  💰\n\n{mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['prize']}\n\n\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n\n\n1 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['1']}\n2 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['2']}\n3 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['3']}\n4 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['4']}\n5 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['5']}\n6 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['6']}\n7 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['7']}\n8 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['8']}\n9 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['9']}\n10 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['10']}\n11 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['11']}\n12 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['12']}\n13 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['13']}\n14 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['14']}\n15 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['15']}\n16 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['16']}\n17 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['17']}\n18 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['18']}\n19 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['19']}\n20 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['20']}\n</b>""", parse_mode='html', reply_markup=markup)
                else:
                    m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Данное место занято либо вы уже находитесь в списке учащихся!</b>""", parse_mode='html')
                    sleep(5)
                    bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
            else:
                m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не выполнили условия для участия в рулетке!</b>""", parse_mode='html')
                sleep(5)
                bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        else:
            m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не участвуете в рулетке!</b>""", parse_mode='html')
            sleep(5)
            bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        bot.answer_callback_query(call.id)

    elif call.data == "one19":
        check_user = users.count_documents({"username": f'{call.from_user.username}'})
        check_conditions = users.find_one({"username": f'{call.from_user.username}'})['check_conditions']
        check_user_rul = users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']
        mess_rul = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['19']
        if check_user:
            if check_conditions == 1:
                if check_user_rul == "-" and mess_rul == "свободное":
                    time_sleep = bot.send_message(call.message.chat.id, f"""<b>⏰ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, подождите, записываю Вас в список учащихся!\n\nПодождите: <code>3 секунды!</code></b>""", parse_mode='html', disable_web_page_preview=True).message_id
                    sleep(3)
                    users.update_one({"username": f'{call.from_user.username}'}, {"$set": {"check_user_rul": 19}})
                    mess.update_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')}, {"$set": {"19": f'@{call.from_user.username}'}})
                    mess__id = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['mess_id']
                    bot.edit_message_text(chat_id=call.message.chat.id, text=f"""<b>✅ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, Вы в списке! Ваше место: <code>{users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']}</code></b>""", message_id=time_sleep, parse_mode='html', disable_web_page_preview=True)
                    markup = types.InlineKeyboardMarkup()
                    participate = types.InlineKeyboardButton('Учавствовать', callback_data='participate')
                    markup.add(participate)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=mess__id, text=f"""<b>‼️‼️‼️  РУЛЕТКА  ‼️‼️‼️\n\n🌆  Город: {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['city']}  🌆\n\n💰  Призовые места  💰\n\n{mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['prize']}\n\n\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n\n\n1 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['1']}\n2 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['2']}\n3 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['3']}\n4 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['4']}\n5 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['5']}\n6 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['6']}\n7 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['7']}\n8 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['8']}\n9 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['9']}\n10 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['10']}\n11 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['11']}\n12 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['12']}\n13 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['13']}\n14 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['14']}\n15 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['15']}\n16 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['16']}\n17 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['17']}\n18 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['18']}\n19 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['19']}\n20 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['20']}\n</b>""", parse_mode='html', reply_markup=markup)
                else:
                    m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Данное место занято либо вы уже находитесь в списке учащихся!</b>""", parse_mode='html')
                    sleep(5)
                    bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
            else:
                m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не выполнили условия для участия в рулетке!</b>""", parse_mode='html')
                sleep(5)
                bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        else:
            m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не участвуете в рулетке!</b>""", parse_mode='html')
            sleep(5)
            bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        bot.answer_callback_query(call.id)

    elif call.data == "one20":
        check_user = users.count_documents({"username": f'{call.from_user.username}'})
        check_conditions = users.find_one({"username": f'{call.from_user.username}'})['check_conditions']
        check_user_rul = users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']
        mess_rul = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['20']
        if check_user:
            if check_conditions == 1:
                if check_user_rul == "-" and mess_rul == "свободное":
                    time_sleep = bot.send_message(call.message.chat.id, f"""<b>⏰ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, подождите, записываю Вас в список учащихся!\n\nПодождите: <code>3 секунды!</code></b>""", parse_mode='html', disable_web_page_preview=True).message_id
                    sleep(3)
                    users.update_one({"username": f'{call.from_user.username}'}, {"$set": {"check_user_rul": 20}})
                    mess.update_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')}, {"$set": {"20": f'@{call.from_user.username}'}})
                    mess__id = mess.find_one({"_id": ObjectId('6343f98db0e7d724daacb7f9')})['mess_id']
                    bot.edit_message_text(chat_id=call.message.chat.id, text=f"""<b>✅ <a href='https://t.me/{call.from_user.username}'>{call.from_user.full_name}</a>, Вы в списке! Ваше место: <code>{users.find_one({"username": f'{call.from_user.username}'})['check_user_rul']}</code></b>""", message_id=time_sleep, parse_mode='html', disable_web_page_preview=True)
                    markup = types.InlineKeyboardMarkup()
                    participate = types.InlineKeyboardButton('Учавствовать', callback_data='participate')
                    markup.add(participate)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=mess__id, text=f"""<b>‼️‼️‼️  РУЛЕТКА  ‼️‼️‼️\n\n🌆  Город: {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['city']}  🌆\n\n💰  Призовые места  💰\n\n{mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['prize']}\n\n\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n\n\n1 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['1']}\n2 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['2']}\n3 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['3']}\n4 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['4']}\n5 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['5']}\n6 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['6']}\n7 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['7']}\n8 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['8']}\n9 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['9']}\n10 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['10']}\n11 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['11']}\n12 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['12']}\n13 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['13']}\n14 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['14']}\n15 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['15']}\n16 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['16']}\n17 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['17']}\n18 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['18']}\n19 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['19']}\n20 - {mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})['20']}\n</b>""", parse_mode='html', reply_markup=markup)
                else:
                    m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Данное место занято либо вы уже находитесь в списке учащихся!</b>""", parse_mode='html')
                    sleep(5)
                    bot.delete_message(chat_id=call.message.chat.id, message_id=m_id)
            else:
                m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не выполнили условия для участия в рулетке!</b>""", parse_mode='html')
                sleep(5)
                bot.delete_message(chat_id=call.message.chat.id, message_id=m_id)
        else:
            m_id = bot.send_message(call.message.chat.id, f"""<b>❌ Доступ запрещен! Вы не участвуете в рулетке!</b>""", parse_mode='html')
            sleep(5)
            bot.delete_message(chat_id=call.message.chat.id, message_id=m_id.message_id)
        bot.answer_callback_query(call.id)

    elif call.data == "syndicoin_balance":
        text = f"""<b>
❕ Информация о SyndiCoin'ах ❕

Для чего нужны SyndiCoin'ы?
  - SyndiCoin'ы нужны для участия в рулетке

Как заработать SyndiCoin'ы?
  - SyndiCoin'ы можно заработать несколькими способами:
    <code>1 - Участие в рулетке</code>
    <code>2 - За каждое написаное Вами сообщение в данный чат</code>
    <code>3 - За решение администрации чата</code>
    <code>4 - За приглашение людей в чат</code>

Что можно сделать с SyndiCoin'ами?
  - Обменять на баланс бота

  По поводу обмена обращаться к @Kana_biz2 или @Al_x_im

</b>"""
        bot.send_message(call.message.chat.id, text=text, parse_mode='html')
        bot.answer_callback_query(call.id)


@bot.message_handler(commands=['go_prize'])
def go_prize(message):
    if message.from_user.username in admins:
        ids = bot.send_message(message.chat.id, "<b>⏰Идет генерация рандомного числа....</b>", parse_mode='html')
        sleep(3)
        a = randint(1, 20)
        b = mess.find_one({'_id': ObjectId('6343f98db0e7d724daacb7f9')})[f'{a}']
        bot.edit_message_text(chat_id=message.chat.id, text=f"<b>✅ Генерация рандомного числа закончена! Число: {a} Победитель: {b}</b>", message_id=ids.message_id, parse_mode='html')

@bot.message_handler(commands=['game_close'])
def game_close(message):
    if message.from_user.username in admins:
        a = users.drop()

@bot.message_handler(content_types=['new_chat_members'])
def new_chat_members(message):
    invited_user = message.new_chat_members[0].username        # Кого пригласили в группу
    who_invited = message.from_user.username                   # Кто пригласил

    memb = member.count_documents({"user_id": message.new_chat_members[0].id})

    if memb:
        return
    else:
        member.insert_one({"user_id": message.new_chat_members[0].id, "chat_id": message.chat.id, "username": message.new_chat_members[0].username, "fullname": message.new_chat_members[0].full_name, "cash": 10})
        bot.send_message(message.chat.id, text=f"""<b>👋 {message.new_chat_members[0].full_name}, добро пожаловать в наш чат!\n\n💰 Вам начислен бонус за вступление в чат в размере: <code>10 SyndiCoin'ов.</code>\n\n💸 Для просмотра баланса, используйте команду /syndicoin_balance</b>""", parse_mode='html')

    user = users.count_documents({"username": f"{message.from_user.username}"})
    if user:
        for i in message.new_chat_members:
            users.insert_one({f"author_invite": f"{who_invited}", "invited_user": f"{i.username}"})

    for i in message.new_chat_members:
        if member.count_documents({"user_id": message.from_user.id}):
            member_bal = member.find_one({"user_id": message.from_user.id})['cash']
            member.update_one({"user_id": message.from_user.id}, {"$set": {"cash": member_bal + 20}})
        else:
            member.insert_one({"user_id": message.from_user.id, "chat_id": message.chat.id, "username": message.from_user.username, "fullname": message.from_user.full_name, "cash": 20})



@bot.message_handler(commands=['syndicoin_balance'])
def syndicoin_balance(message):
    user = member.count_documents({'user_id': message.from_user.id})

    markup = types.InlineKeyboardMarkup()
    syndicoin_balance = types.InlineKeyboardButton('Для чего нужен этот баланс?', callback_data="syndicoin_balance")
    markup.add(syndicoin_balance)

    if user:
        bot.send_message(message.chat.id, f"""<b>👋 {message.from_user.full_name}, Ваш баланс составляет: <code>{member.find_one({"user_id": message.from_user.id})['cash']} SyndiCoin'ов</code></b>""", parse_mode='html', reply_markup=markup)
    else:
        member.insert_one({"user_id": message.from_user.id, "chat_id": message.chat.id, "username": message.from_user.username, "fullname": message.from_user.full_name, "cash": 0})
        bot.send_message(message.chat.id, f"""<b>👋 {message.from_user.full_name}, Ваш баланс составляет: <code>{member.find_one({"user_id": message.from_user.id})['cash']} SyndiCoin'ов</code></b>""", parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def cont_text(message):
    if member.count_documents({"user_id": message.from_user.id}):
        if message.text:
            member_bal = member.find_one({"user_id": message.from_user.id})['cash']
            member.update_one({"user_id": message.from_user.id}, {"$set": {"cash": member_bal + 1}})
    else:
        member.insert_one({"user_id": message.from_user.id, "chat_id": message.chat.id, "username": message.from_user.username, "fullname": message.from_user.full_name, "cash": 0})

@bot.message_handler(commands=['set_syndicoin'])
def set_syndicoins(message):
    if message.from_user.username in admins:
        


bot.polling(none_stop=True, interval=0)