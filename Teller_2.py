import logging
import sqlite3

from telegram.ext import Application, MessageHandler, filters, ConversationHandler
from config import BOT_TOKEN
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from random import choice
from datetime import datetime

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

reply_keyboard_2 = [['/1', '/2', '/3']]
markup_1 = ReplyKeyboardMarkup(reply_keyboard_2, one_time_keyboard=True)

reply_keyboard_3 = [['/Blue', '/Red', '/Green']]
markup_2 = ReplyKeyboardMarkup(reply_keyboard_3, one_time_keyboard=True)

data = ''
datt = ''
sex = ''
last = ''
chinese_zodiac = ''

Amulets_Fire = ['Fire_1.png', 'Fire_2.png', 'Fire_3.png']
Amulets_Water = ['Water_1.png', 'Water_2.png', 'Water_3.png']
Amulets_Ground = ['Ground_1.png', 'Ground_2.png', 'Ground_3.png']
Amulets_Wind = ['Wind_1.png', 'Wind_2.png', 'Wind_3.png']

con = sqlite3.connect('Gadalka.db')

cur = con.cursor()


async def start_command(update, context):
    global sex, last, datt

    rezult0 = cur.execute(f"""SELECT user FROM Users""").fetchall()
    if str(update.message.from_user.first_name) + ' ' + str(update.message.from_user.last_name) in rezult0[0]:
        datt = str(datetime.now())[:-7]
        result1 = cur.execute(f"""INSERT INTO Users(user,data) VALUES('{str(update.message.from_user.first_name)
                                                                        + ' ' + str(update.message.from_user.last_name)}', '{datt}')""").fetchall()
        con.commit()

        await update.message.reply_text(
            f"С возвращением, {str(update.message.from_user.first_name) + ' ' + str(update.message.from_user.last_name)}!😘\n "
            f"Тебе так понравился мой прогноз? А в прочем, неважно:\n"
            f"тебе вновь выпала уникальная\n"
            "возможность пообщаться с ведущим специалистом в\n"
            "области родологии, магистром астрологии, заслуженной\n"
            "предсказательницей и могущественной потомственной\n"
            "гадалкой Зинаидой Степановной, в народе - Бабой Зиной.🔮\n"
            "Чтобы узнать свое самое вероятное будущее, а также\n"
            "уберечь себя от происков сил тьмы, внимательно следуй\n"
            "моим указаниям. На все вопросы отвечай предельно честно,\n"
            "иначе даже самые сильные мои заговоры не подействуют!🪄")
        await update.message.reply_text('Ты мужчина👨 или женщина👩?')

        return 0
    else:
        datt = str(datetime.now())[:-7]
        result1 = cur.execute(f"""INSERT INTO Users(user,data) VALUES( 
                '{str(update.message.from_user.first_name) + ' ' + str(update.message.from_user.last_name)}', '{datt}')""").fetchall()
        con.commit()

        await update.message.reply_text(
            "Здравствуй мил человек, тебе выпала уникальная\n"
            "возможность пообщаться с ведущим специалистом в\n"
            "области родологии, магистром астрологии, заслуженной\n"
            "предсказательницей и могущественной потомственной\n"
            "гадалкой Зинаидой Степановной, в народе - Бабой Зиной.🔮\n"
            "Чтобы узнать свое самое вероятное будущее, а также\n"
            "уберечь себя от происков сил тьмы, внимательно следуй\n"
            "моим указаниям. На все вопросы отвечай предельно честно,\n"
            "иначе даже самые сильные мои заговоры не подействуют!🪄")
        await update.message.reply_text('Ты мужчина👨 или женщина👩?')

        return 0


async def sexx(update, context):
    global sex

    if 'Муж' in update.message.text or 'Жен' in update.message.text or \
            'муж' in update.message.text or 'жен' in update.message.text:
        sex = str(update.message.text)
        # file.write(f'sex:{sex}\n')

        await update.message.reply_text(
            f"Отлично🙂, теперь введи свою дату рождения (например, 13.12.1978):)"
        )
        return 5
    else:

        await update.message.reply_text("Не обманывай меня😡! Такого пола нет! Введи свой пол,\n"
                                        " а иначе я не смогу дать тебе точное предсказание!")
        return 0


async def zzz(update, context):
    global data, zodiac, y
    if str(update.message.text).count('.') == 2 and 1 <= int(str(update.message.text.split('.')[1])) <= 12\
            and 1 <= int(str(update.message.text.split('.')[0])) <= 31:
        data = str(update.message.text)
        data_lst = data.split('.')
        day, month, y = data_lst[0], data_lst[1], data_lst[2]

        if day[0] == '0':
            day = day[1]
        if month[0] == '0':
            month = month[1]

        if (int(month) == 12 and int(day) >= 23) or (int(month) == 1 and int(day) <= 20):
            zodiac = 'Козерог♑'

        elif (int(month) == 1 and int(int(day) >= 21)) or (int(month) == 2 and int(day) <= 19):
            zodiac = 'Водолей♒'

        elif (int(month) == 2 and int(int(day) >= 20)) or (int(month) == 3 and int(day) <= 20):
            zodiac = 'Рыбы♓'

        elif (int(month) == 3 and int(day) >= 21) or (int(month) == 4 and int(day) <= 20):
            zodiac = 'Овен♈'

        elif (int(month) == 4 and int(day) >= 21) or (int(month) == 5 and int(day) <= 21):
            zodiac = 'Телец♉'

        elif (int(month) == 5 and int(int(day) >= 22)) or (int(month) == 6 and int(day) <= 21):
            zodiac = 'Близнецы♊'

        elif (int(month) == 6 and int(day) >= 22) or (int(month) == 7 and int(day) <= 22):
            zodiac = 'Рак♋'

        elif (int(month) == 7 and int(int(day) >= 23)) or (int(month) == 8 and int(day) <= 21):
            zodiac = 'Лев♌'

        elif (int(month) == 8 and int(int(day) >= 22)) or (int(month) == 9 and int(day) <= 23):
            zodiac = 'Дева♍'

        elif (int(month) == 9 and int(day) >= 24) or (int(month) == 10 and int(day) <= 23):
            zodiac = 'Весы♎'

        elif (int(month) == 10 and int(int(day) >= 24)) or (int(month) == 11 and int(day) <= 22):
            zodiac = 'Скорпион♏'

        elif (int(month) == 11 and int(int(day) >= 23)) or (int(month) == 12 and int(day) <= 22):
            zodiac = 'Стрелец♐'

        await update.message.reply_text(
            f"Итак...🤔 судя по всему, по гороскопу ты - {zodiac}!")
        await update.message.reply_text(
            f"Такие люди очень уравновешенные, успешные и талантливые, и это хорошая новость!😁 Но есть и плохая...😨\n"
            f"Кажется, что ты находишься в не самом благоприятном финансовом положении, но это неточные данные.\n"
            f"Поэтому сейчас я проведу еще ряд проверок. Отправь свой любимый смайлик для анализа твоего "
            f"финансового "
            f"положения по психическому "
            f"состоянию")
        return 6
    else:
        await update.message.reply_text("Ты ввел некорректную дату!🤬 Если хочешь\n"
                                        "узнать свою судьбу, введи еще раз:")
        return 5


async def emotional(update, context):
    global data, zodiac, y

    y = str(y)
    y = list(y)
    c = sum(map(int, y))

    if c % 10 == 0 or c % 10 == 4 or c % 10 == 8:
        await update.message.reply_text(
            f"Мой анализ показал, что ты позитивный человек, готовый на всё. Это действительно круто!!!👍\n"
            f"Однако альфа Большого Пса пророчит тебе не самое приятное будущее. Еще немного, и ты попадешь в "
            f"финансовую дыру!!!💸💰❌",

        )

    elif c % 10 == 1 or c % 10 == 5 or c % 10 == 9:
        await update.message.reply_text(
            f"Звёзды говорят, что ты трудолюбивый человек, всегда готовый прийти на помощь, что не может не "
            f"радовать!!!👍\n "
            f"Но с ними не согласна бета Ориона. Судя по всему, в твоей жизни наступает Очень Черная Полоса!!!🕳️🏃",

        )

    elif c % 10 == 2 or c % 10 == 6:
        await update.message.reply_text(
            f"Карты гласят, что у тебя большой потенциал, ты с вероятностью 84.67% станешь знаменитостью (а с "
            f"вероятностью 15.33% - резистором). "
            f"Поздравляю!!!👍\n "
            f"Но созвездие Южного Треугольника пророчит тебе неблагоприятный исход в финансовом плане!💸💰❌",

        )

    else:
        await update.message.reply_text(
            f"Самый точный прогноз показывает, что у тебя добрая душа и потрясающие ораторские способности. Ты "
            f"гений!!!👍\n "
            f"Однако, к сожалению, не все звезды согласны с этим прогнозом. Созвездие Малого Коня говорит о "
            f"возможности твоего попадания в финансовую дыру!!!💸💰❌",

        )
    await update.message.reply_text(
        f"Теперь отправь нелюбимый смайлик, чтобы я могла подвести итог о твоем положении",
    )

    return 1


async def birth_data(update, context):
    global data, chinese_zodiac

    if data.count('.') == 2:
        # file.write(f'data:{data}\n')
        year = data.split('.')[2]

        if (int(year) - 2000) % 12 == 0:
            chinese_zodiac = 'Дракон🐉'

        elif (int(year) - 2000) % 12 == 1:
            chinese_zodiac = 'Змея🐍'

        elif (int(year) - 2000) % 12 == 2:
            chinese_zodiac = 'Лошадь🐴'

        elif (int(year) - 2000) % 12 == 3:
            chinese_zodiac = 'Коза🐐'

        elif (int(year) - 2000) % 12 == 4:
            chinese_zodiac = 'Обезьяна🐒'

        elif (int(year) - 2000) % 12 == 5:
            chinese_zodiac = 'Петух🐔'

        elif (int(year) - 2000) % 12 == 6:
            chinese_zodiac = 'Собака🐶'

        elif (int(year) - 2000) % 12 == 7:
            chinese_zodiac = 'Свинья🐷'

        elif (int(year) - 2000) % 12 == 8:
            chinese_zodiac = 'Крыса🐀'

        elif (int(year) - 2000) % 12 == 9:
            chinese_zodiac = 'Бык🐮'

        elif (int(year) - 2000) % 12 == 10:
            chinese_zodiac = 'Тигр🐯'

        else:
            chinese_zodiac = 'Кролик🐰'
        # file.write(f'chinese_zodiac:{chinese_zodiac}\n')

        await update.message.reply_text(
            f"У меня для тебя печальные вести: звезды открыли мне,\n"
            f"что по восточному гороскопу ты - {chinese_zodiac}!\n"
            f"В мае 2023  года этот знак будут ожидать неудачи в финансах💸,\n"
            f"проблемы на работе💼, разлад в семье👩💔👨\n")
        await update.message.reply_text(
            f"Однако на судьбу может повлиять и твой собственный выбор🎰\n"
            f"Cейчас я разложу свои гадальные карты🃏, нажми /gadanie,\n"
            f"а затем выбери одну из них:")
        return 2

    else:

        await update.message.reply_text("Ты ввел некорректную дату! Если хочешь\n"
                                        "узнать свою судьбу, введи еще раз:")

        return 1


async def gadanie(update, context):
    await update.message.reply_text(
        f"Сосредоточься, возжелай узреть истину,\n"
        f"выбирай с умом!",
        reply_markup=markup_1
    )

    return 2


async def f(update, context):
    await update.message.reply_text(
        f"Хм... Очень интересный выбор!", reply_markup=ReplyKeyboardRemove())
    await update.message.reply_text(
        f"Это твоё окончательное решение?")

    return 2


async def s(update, context):
    await update.message.reply_text(
        f"Хм... Очень интересный выбор!", reply_markup=ReplyKeyboardRemove())
    await update.message.reply_text(
        f"Это твоё окончательное решение?")

    return 2


async def th(update, context):
    await update.message.reply_text(
        f"Хм... Очень интересный выбор!", reply_markup=ReplyKeyboardRemove())
    await update.message.reply_text(
        f"Это твоё окончательное решение?")

    return 2


async def rez_gad(update, context):
    global data, sex, chinese_zodiac

    data_day, data_mon, data_year = data.split('.')[0], data.split('.')[1], data.split('.')[2]

    if data_mon[0] == '0':
        data_mon = data_mon[1:]
        data = '.'.join([data_day, data_mon, data_year])

    if str(sex)[0] == 'М' or str(sex)[0] == 'м':
        await update.message.reply_text(
            f"Всё куда хуже, чем я предполагала изначально!😱\n"
            f"Ты избрал 'Отравленный клинок'. Для мужчины, родившегося\n"
            f"в {data.split('.')[1]} месяце и в год животного {chinese_zodiac},\n"
            f"это может означать лишь одно - на тебе очень сильная порча!😱"
            # f"Всего доброго {chr(int('1F631', 16))}!"
        )

        await update.message.reply_text(
            f"Боюсь в этом случае защитные заговоры будут бессильны..."
            f"Хотя, есть у меня одно надежное средство!"
            f"Напиши стихию🌪️, с которой ты себе ассоциируешь:"
        )

        return 3

    elif str(sex)[0] == 'Ж' or str(sex)[0] == 'ж':
        await update.message.reply_text(
            f"Всё куда хуже, чем я предполагала изначально!😱\n"
            f"Ты избрала 'Отравленный клинок'. Для женщины, родившейся\n"
            f"в {data.split('.')[1]} месяце и в год животного {chinese_zodiac},\n"
            f"это может означать лишь одно - на тебе очень сильная порча!😱"
        )

        await update.message.reply_text(
            f"Боюсь в этом случае защитные заговоры будут бессильны...\n"
            f"Хотя, есть у меня одно надежное средство!\n"
            f"Напиши стихию🌪️, с которой ты себе ассоциируешь:"
        )
        print(data, sex, chinese_zodiac)
        return 3


async def amulet(update, context):
    global ammulet

    if str(update.message.text).capitalize() in ['Земля', 'Вода', 'Огонь', 'Воздух']:
        # file.write(f'sixiya:{str(update.message.text).capitalize()}\n')

        ammulet = update.message.text
        await update.message.reply_text(
            f"Что ж, отлично. Теперь мне все про тебя стало ясно\n"
            f"Как я и полагала, помочь тебе сможет лишь мой виртуальный оберег🪬"
        )

        await update.message.reply_text(
            f"Чтобы амулет получился по-настоящему сильным, необходимо сперва\n"
            f"зарядиться денежной энергией. Позолоти бабушке ручку! 😘"
        )

        await update.message.reply_text(
            f"Мои услуги очень ценятся, поэтому тебе придётся заплатить 1.000.000 рублей💵.\n"
            f"Но ты можешь получить скидку вплоть ло 99,9999%!🤗 Для этого выбери одну из дверей:"
        )
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(f'images/door1.png', 'rb'))
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(f'images/door2.png', 'rb'))
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(f'images/door3.png', 'rb'))
        await update.message.reply_text(
            f"Сконцентрируйся, ведь этот выбор не изменить...",
            reply_markup=markup_2
        )
        return 7

    else:
        await update.message.reply_text("Не обманывай меня!🤬 Такой стихии нет! Введи стихию,\n"
                                        " а иначе я не смогу дать тебе достойную защиту!")

        return 3


async def d1(update, context):
    await update.message.reply_text(
        f"Любопытно...", reply_markup=ReplyKeyboardRemove())
    await update.message.reply_text(
        f"Точно эта дверь?")
    return 7


async def d2(update, context):
    await update.message.reply_text(
        f"Хмм...........", reply_markup=ReplyKeyboardRemove())
    await update.message.reply_text(
        f"Не хочешь поменять свой выбор?")
    return 7


async def d3(update, context):
    await update.message.reply_text(
        f"Хм... Очень интересный выбор!", reply_markup=ReplyKeyboardRemove())
    await update.message.reply_text(
        f"Точно её?")
    return 7


async def rez_door(update, context):
    await update.message.reply_text(
        f"Не верю своим глазам!!!😨 Как тебе удалось?😱 Теперь ты обладатель скидки 99,99%!!!💯"
        f"Мои поздравления! Никому кроме тебе ещё так не везло! Твоей удаче можно только позавидовать!"
    )
    await update.message.reply_text(
        f"Только для тебя и только сейчас мой заговоренный амулет\n"
        f"Стоит всего лишь какие-то 100₽! Позолоти бабушке ручку! 😘"
    )
    await update.message.reply_text(
        f"Переведи деньги (50₽ на 5536 9140 5064 5898 и 50₽ на 2200 7007 0621 9259) и получи секретный код, по которому\n"
        f"я смогу создать для тебя уникальный заговоренный амулет\n"
    )
    return 4


async def BEST_GADALKA_EVER(update, context):
    if str(update.message.text) == 'BEST_GADALKA_EVER':
        if str(ammulet).capitalize() == 'Земля':
            ch_amulet = choice(Amulets_Ground)
            await update.message.reply_text("Генерирую...")
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(f'images/{ch_amulet}', 'rb'))
            await update.message.reply_text("Это было очень непросто🤯, но я справилась\n"
                                            "Мне удалось рассеять твою неудачу и зарядить\n"
                                            "твой амулет чистой жизненной энергией\n"
                                            "Размести оберег на странице в социальной сети\n"
                                            "И твоя жизнь изменится к лучшему!🥳")

        if str(ammulet).capitalize() == 'Вода':
            ch_amulet = choice(Amulets_Water)
            await update.message.reply_text("Генерирую...")
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(f'images/{ch_amulet}', 'rb'))
            await update.message.reply_text("Это было очень непросто🤯, но я справилась\n"
                                            "Мне удалось рассеять твою неудачу и зарядить\n"
                                            "твой амулет чистой жизненной энергией\n"
                                            "Размести оберег на странице в социальной сети\n"
                                            "И твоя жизнь изменится к лучшему!🥳")

        if str(ammulet).capitalize() == 'Огонь':
            ch_amulet = choice(Amulets_Fire)
            await update.message.reply_text("Генерирую...")
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(f'images/{ch_amulet}', 'rb'))
            await update.message.reply_text("Это было очень непросто🤯, но я справилась\n"
                                            "Мне удалось рассеять твою неудачу и зарядить\n"
                                            "твой амулет чистой жизненной энергией\n"
                                            "Размести оберег на странице в социальной сети\n"
                                            "И твоя жизнь изменится к лучшему!🥳")

        if str(ammulet).capitalize() == 'Воздух':
            ch_amulet = choice(Amulets_Wind)
            await update.message.reply_text("Генерирую...")
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(f'images/{ch_amulet}', 'rb'))
            await update.message.reply_text("Это было очень непросто🤯, но я справилась\n"
                                            "Мне удалось рассеять твою неудачу и зарядить\n"
                                            "твой амулет чистой жизненной энергией\n"
                                            "Размести оберег на странице в социальной сети\n"
                                            "И твоя жизнь изменится к лучшему!🥳")
        await update.message.reply_text("На этом наш сеанс окончен\n"
                                        "Не забудь порекомендовать мои услуги\n"
                                        "своим знакомым, дабы и они смогли\n"
                                        "изменить свою жизнь к лучшему!🎉")
        await update.message.reply_text("Всего доброго 😘😘😘!")

        return ConversationHandler.END

    else:
        await update.message.reply_text("Код неверный. Не обманывай бабушку!🤬 Переведи деньги,\n"
                                        "а затем отправь корректный пароль:")

        return 4


async def stop(update, context):
    await update.message.reply_text("Всего доброго 😘😘😘!")
    return ConversationHandler.END


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("gadanie", gadanie))
    application.add_handler(CommandHandler("1", f))
    application.add_handler(CommandHandler("2", s))
    application.add_handler(CommandHandler("3", th))
    application.add_handler(CommandHandler("Blue", d1))
    application.add_handler(CommandHandler("Red", d1))
    application.add_handler(CommandHandler("Green", d3))
    conv_handler = ConversationHandler(

        entry_points=[CommandHandler('start', start_command)],

        states={
            0: [MessageHandler(filters.TEXT & ~filters.COMMAND, sexx)],
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, birth_data)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, rez_gad)],
            3: [MessageHandler(filters.TEXT & ~filters.COMMAND, amulet)],
            4: [MessageHandler(filters.TEXT & ~filters.COMMAND, BEST_GADALKA_EVER)],
            5: [MessageHandler(filters.TEXT & ~filters.COMMAND, zzz)],
            6: [MessageHandler(filters.TEXT & ~filters.COMMAND, emotional)],
            7: [MessageHandler(filters.TEXT & ~filters.COMMAND, rez_door)]

        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    application.add_handler(conv_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
