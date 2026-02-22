from FunPayAPI import Account, Runner, types, enums
import os

TOKEN = os.getenv("FP_TOKEN")
if TOKEN is None:
    print("token not set")
    exit()


acc = Account(TOKEN).get()

games = {}

games[1884] = ("Party Animals", {"fields[platform]": "PC", "fields[type]": "Standard Edition"}, [1.08, 1.50, 2.00, 2.50, 3.00, 4.00, 5.00, 8.00, 15.00, 20.00, 24.00, 26.00])
games[383] = ("Forza Horizon 5", {"server_id": "5593", "fields[type]": "Аренда"}, [2.00, 4.00, 6.00, 7.00, 8.00, 9.00, 12.00, 18.00, 25.00, 30.00, 40.00, 50.00])
games[3879] = ("MIMESIS", {}, [1.17, 1.50, 1.70, 2.00, 2.30, 2.60, 4.00, 6.00, 10.00, 13.00, 14.00, 16.00])
games[2988] = ("Grounded", {"server_id": "11872", "fields[platform]": "PC"}, [1.10, 2.00, 3.00, 4.00, 5.00, 6.00, 10.00, 13.00, 17.00, 20.00, 23.00, 30.00])
#games[1450] = [("Outlast", {"server_id": "8897", "fields[platform]": "(PC) Steam", "fields[type]": "Аренда"}, [1.10, 3.00, 5.00, 6.00, 7.00, 8.00, 9.00, 12.00, 14.00, 16.00, 20.00, 21.00]), ("The Outlast Trials", {"server_id": "8899", "fields[platform]": "(PC) Steam", "fields[type]": "Аренда"}, [1.10, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 10.00, 13.00, 14.00, 20.00, 28.00])]
games[3204] = ("Assassin's Creed Shadows", {"fields[platform]": "PC"}, [3.00, 4.00, 5.00, 6.00, 7.00, 7.50, 10.00, 18.00, 34.00, 52.00, 67.00, 90.00])
games[3222] = ("Escape the Backrooms", {"server_id": "11212", "fields[platform]": "PC"}, [2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 9.00, 10.00, 18.00, 26.00, 28.00, 30.00])
games[2888] = ("7 Days to Die", {"fields[platform]": "PC", "fields[type]": "Standard Edition"}, [1.10, 4.00, 5.00, 7.00, 8.00, 9.00, 10.00, 11.00, 12.00, 13.00, 14.00, 15.00])
games[1352] = ("The Last of Us Part I", {"server_id": "9838", "fields[platform]": "PC", "fields[steamegs]": "Steam", "fields[type]": "Standard Edition"}, [4.00, 8.00, 12.00, 15.00, 18.00, 20.00, 30.00, 40.00, 60.00, 80.00, 85.00, 90.00])
games[872] = ("Elden Ring", {"server_id": "7027", "fields[type]": "Аренда"}, [4.00, 8.00, 12.00, 15.00, 18.00, 20.00, 30.00, 40.00, 70.00, 100.00, 120.00, 140.00])
games[2876] = ("Factorio", {}, [1.03, 3.00, 5.00, 7.00, 8.00, 10.00, 18.00, 20.00, 40.00, 52.00, 67.00, 85.00])
games[1598] = ("Euro Truck Simulator 2", {"fields[type]": "Аренда"}, [1.12, 1.30, 1.50, 1.70, 2.00, 2.50, 3.00, 5.00, 6.00, 7.00, 7.20, 8.00])
games[2998] = ("Sniper Elite 5", {"server_id": "10995", "fields[platform]": "PC"}, [1.08, 2.00, 3.00, 4.00, 5.00, 6.00, 14.00, 25.00, 40.00, 50.00, 60.00, 70.00])
games[1925] = ("Spider-Man Remastered", {"server_id": "11174", "fields[platform]": "PC"}, [4.50, 6.00, 8.00, 10.00, 12.00, 15.00, 30.00, 52.00, 67.00, 88.00, 95.00, 99.00])
games[2185] = ("Helldivers 2", {"server_id": "9714", "fields[game]": "Helldivers 2", "fields[type]": "Standard Edition", "fields[offer]": "Аренда"}, [3.00, 6.00, 8.00, 8.50, 9.00, 10.00, 15.00, 21.00, 30.00, 52.00, 67.00, 95.00])
games[1393] = ("Dead Island 2", {"fields[platform]": "PC", "fields[type]": "Аренда"}, [2.00, 4.00, 6.00, 8.00, 9.00, 10.00, 13.00, 23.00, 40.00, 52.00, 67.00, 69.00])
games[3067] = ("Sid Meier's Civilization 7", {"fields[platform]": "PC"}, [9.00, 16.00, 19.00, 25.00, 28.00, 29.00, 52.00, 67.00, 100.00, 150.00, 180.00, 210.00])
games[3169] = ("R.E.P.O.", {"fields[type]": "Аренда"}, [1.13, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 13.00, 15.00, 17.00, 20.00, 25.00])
games[2620] = ("Undertale", {"fields[platform]": "PC"}, [2.00, 2.30, 2.50, 3.00, 4.00, 5.00, 9.00, 13.00, 15.00, 20.00, 25.00, 35.00])
games[2166] = ("Palworld", {"server_id": "9936", "fields[type]": "Аренда"}, [1.08, 1.20, 1.40, 1.60, 1.80, 4.00, 16.00, 18.00, 25.00, 35.00, 42.00, 52.00])
games[2693] = ("SnowRunner", {"fields[platform]": "PC", "fields[type]": "Standard Edition"}, [10.00, 13.00, 15.00, 17.00, 19.00, 22.00, 25.00, 28.00, 30.00, 35.00, 42.00, 52.00])
games[3554] = ("Subnautica", {"server_id": "11797", "fields[platform]": "PC"}, [1.50, 2.00, 3.00, 4.00, 5.00, 6.00, 18.00, 28.00, 35.00, 42.00, 52.00, 69.00])
games[2893] = ("Project Zomboid", {"fields[type]": "Standard Edition"}, [1.08, 1.20, 1.50, 1.70, 2.00, 2.50, 4.00, 6.00, 10.00, 15.00, 17.00, 20.00])
games[786] = ("Chivalry 2", {"server_id": "5157"}, [1.50, 3.00, 4.00, 5.00, 5.50, 6.00, 15.00, 25.00, 35.00, 42.00, 52.00, 69.00])
games[573] = ("Garry's Mod", {"fields[method]": "Аренда"}, [1.12, 1.50, 2.00, 3.00, 3.50, 4.00, 8.00, 16.00, 27.00, 30.00, 52.00, 69.00])
games[2506] = ("Chained Together", {"fields[type]": "Аренда"}, [1.08, 1.30, 1.50, 2.00, 2.20, 2.50, 4.00, 6.00, 8.00, 10.00, 14.00, 17.00])
games[1964] = ("Watch Dogs: Legion", {"server_id": "9678", "fields[platform]": "PC"}, [4.00, 5.00, 6.00, 8.00, 10.00, 12.00, 20.00, 35.00, 42.00, 52.00, 67.00, 90.00])
games[1891] = ("No Man's Sky", {}, [1.08, 3.00, 5.00, 7.00, 8.00, 9.00, 10.00, 15.00, 17.00, 20.00, 25.00, 30.00])
games[1345] = ("Resident Evil 4", {"fields[platform]": "PC", "fields[type]": "Аренда"}, [3.00, 5.00, 7.00, 9.00, 10.00, 11.00, 16.00, 27.00, 42.00, 52.00, 57.00, 69.00])

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
    game_lots = games[subcategory_id]
    if not isinstance(game_lots, list):
        game_lots = [game_lots]
    for game in game_lots:
        if not isinstance(game, tuple):
            print(game, "is not a tuple")
        if len(game) == 2:
            name, fields = game
            prices = None
        elif len(game) == 3:
            name, fields, prices = game
            if len(prices) != len(times):
                print("not enough prices for game", name)
                return
        else:
            return
        calc = acc.calc(types.SubCategoryTypes.COMMON, subcategory_id)
        for i, t in enumerate(times):
            lot = types.LotFields(0, {}, acc.get_subcategory(types.SubCategoryTypes.COMMON, subcategory_id))
            lot.active = False
            lot.amount = 111
            lot.currency = types.Currency.RUB
            lot.description_en = lot_desc_en
            lot.description_ru = lot_desc_ru
            lot.title_en = lot_name_en.replace('%t', t.split(':')[1]).replace('%n', name)
            lot.title_ru = lot_name_ru.replace('%t', t.split(':')[0]).replace('%n', name)
            lot.price = (prices[i] if prices else 1500) / calc.commission_coefficient
            lot.fields.update(fields)
            print("Создаём", lot.title_ru, "за", prices[i] if prices else 1500)
            acc.save_lot(lot)

for id in games:
    #print(id, acc.calc(types.SubCategoryTypes.COMMON, id).commission_coefficient)
    fill_category(id)
