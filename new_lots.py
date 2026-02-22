from FunPayAPI import Account, Runner, types, enums
import os

TOKEN = os.getenv("FP_TOKEN")
if TOKEN is None:
    print("token not set")
    exit()


acc = Account(TOKEN).get()

games = {}

games[1884] = ("Party Animals", {"fields[platform]": "PC", "fields[type]": "Standard Edition"})
games[383] = ("Forza Horizon 5", {"server_id": "5593", "fields[type]": "Аренда"})
games[3879] = ("MIMESIS", {})
games[2988] = ("Grounded", {"server_id": "11872", "fields[platform]": "PC"})
games[1450] = ("Outlast", {"server_id": "8897", "fields[platform]": "(PC) Steam", "fields[type]": "Аренда"})
games[3204] = ("Assassin's Creed Shadows", {"fields[platform]": "PC"})
games[3222] = ("Escape the Backrooms", {"server_id": "11212", "fields[platform]": "PC"})
games[2888] = ("7 Days to Die", {"fields[platform]": "PC", "fields[type]": "Standard Edition"})
games[1352] = ("The Last of Us Part I", {"server_id": "9838", "fields[platform]": "PC", "fields[type]": "Standard Edition"})
games[872] = ("Elden Ring", {"server_id": "7027", "fields[type]": "Аренда"})

times = """
1 ЧАС:1 HOUR
2 ЧАСА:2 HOURS
3 ЧАСА:3 HOURS
4 ЧАСА:4 HOURS
5 ЧАСОВ:5 HOURS
6 ЧАСОВ:6 HOURS
12 ЧАСОВ:12 HOURS
24 ЧАСА:24 HOURS
2 ДНЯ:2 DAYS
3 ДНЯ:3 DAYS
5 ДНЕЙ:5 DAYS
7 ДНЕЙ:7 DAYS
"""[1:-1].split('\n')

lot_name_ru = "🌸| ≽ > ⩊ < ≼ |🌸✧ АВТО-ВЫДАЧА 🌸【 АРЕНДА %t 】･ﾟ✧ online в steam【%n】✧･ﾟ"
lot_desc_ru = """𐙚˙⋆.˚ ꕤ 𖠓 ݁ ˖ ⊹ ࣪ Мгновенная авто-выдача данных 𝟐𝟒/𝟕 ࣪⊹ ˖ 𖠓 ꕤ ˚.⋆˙𐙚
₊˚ʚ ᓚᘏᗢ ɞ˚₊ Пожалуйста, оплачивайте только 𝟏 штуку в лоте ₊˚ʚ ᓚᘏᗢ ɞ˚₊
─────────────────────୨♡୧─────────────────────
Как сделать заказ? ꒰ (っ˘ω˘ς) ꒱
1. Оплатите лот на нужное количество времени 🌸🐾🌸
═ ⋆꙳·̩̩..̩̩·꙳⋆ ═ Если нужно другое время — в профиле есть от 1 часа до 7 дней, для этого
Зайдите в профиль, нажмите 𝐂𝐭𝐫𝐥 + 𝐅 и введите название игры ═ ⋆꙳·̩̩..̩̩·꙳⋆ ═
2. Вам сразу придут данные для входа в 𝐒𝐭𝐞𝐚𝐦 🌸🐾🌸
3. Напишите в чат !𝐠𝐮𝐚𝐫𝐝 для получения кода. Введите этот код в Steam 🌸🐾🌸
4. C аккаунтом всё в порядке - подтвердите выполнение 🌸🐾🌸
───୨♡୧─── Дополнительная информация ───୨♡୧───
⏱️ Время аренды начинается только после получения данных.
~ Можно играть с другом, если у него есть эта игра. (,,ᴗ ᴗ,,)
~ Ник и аватарку можно менять под себя (,,ᴗ ᴗ,,)
~ (｀へ´)💢 при непристойных никах и фото - услуга считается законченной, выполненной
───୨♡୧────────────────────────────୨♡୧───
Приятной игры! 🎐
Обращайтесь, если у вас есть пожелания, вопросы или неполадки - я всегда рада вам помочь и на связи!"""
lot_name_en = "🌸| ≽ > ⩊ < ≼ |🌸✧ AUTO-DELIVERY 🌸【 RENTAL %t 】･ﾟ✧ online steam【%n】✧･ﾟ"
lot_desc_en = """𐙚˙⋆.˚ ꕤ 𖠓 ݁ ˖ ⊹ ࣪ Instant auto-delivery 𝟐𝟒/𝟕 ࣪⊹ ˖ 𖠓 ꕤ ˚.⋆˙𐙚
₊˚ʚ ᓚᘏᗢ ɞ˚₊ Please buy only 𝟏 item pre lot ₊˚ʚ ᓚᘏᗢ ɞ˚₊
─────────────────────୨♡୧─────────────────────
How to place an order? ꒰ (っ˘ω˘ς) ꒱
1. Pay for the lot for the required amount of time 🌸🐾🌸
═ ⋆꙳·̩̩..̩̩·꙳⋆ ═ If you need a different time — there are options from 1 hour to 7 days in my profile
Go to my profile, press 𝐂𝐭𝐫𝐥 + 𝐅 and enter the game name ═ ⋆꙳·̩̩..̩̩·꙳⋆ ═
2. You will immediately receive 𝐒𝐭𝐞𝐚𝐦 login and password 🌸🐾🌸
3. Type !𝐠𝐮𝐚𝐫𝐝 into chat to get guard code. Enter it into 𝐒𝐭𝐞𝐚𝐦 🌸🐾🌸
4. If everything is fine with the account — confirm completion 🌸🐾🌸
───୨♡୧─── Additional information ───୨♡୧───
⏱️ Rental time starts only after receiving the data.
~ You can play with a friend if they have this game (,,ᴗ ᴗ,,)
~ You can change your nickname and avatar (,,ᴗ ᴗ,,)
~ (｀へ´)💢 For inappropriate nicknames and photos — the rental is considered terminated and completed
───୨♡୧────────────────────────────୨♡୧───
Enjoy the game! 🎐
Feel free to reach out if you have any wishes, questions, or issues — I'm always happy to help and available!"""

def fill_category(subcategory_id: int):
    game = games[subcategory_id]
    name, fields = game
    calc = acc.calc(types.SubCategoryTypes.COMMON, subcategory_id)
    for t in times:
        lot = types.LotFields(0, {}, acc.get_subcategory(types.SubCategoryTypes.COMMON, subcategory_id))
        lot.active = True
        lot.amount = 1
        lot.currency = types.Currency.RUB
        lot.deactivate_after_sale = True
        lot.description_en = lot_desc_en
        lot.description_ru = lot_desc_ru
        lot.title_en = lot_name_en.replace('%t', t.split(':')[1]).replace('%n', name)
        lot.title_ru = lot_name_ru.replace('%t', t.split(':')[0]).replace('%n', name)
        lot.price = 1500 / calc.commission_coefficient
        lot.fields.update(fields)
        acc.save_lot(lot)

for id in games:
    #print(id, acc.calc(types.SubCategoryTypes.COMMON, id).commission_coefficient)
    fill_category(id)
