from FunPayAPI import Account, Runner, types, enums

TOKEN = ""

acc = Account(TOKEN).get()

games = """
Satisfactory:2792
REMATCH:3472
EA SPORTS FC 25:2786
Sons of the Forest:1795
Split Fiction:3176
Assetto Corsa:2198
Dying Light:868
Little Nightmares:3549
BeamNG.drive:1997
Ready or Not:1756
Phasmophobia:2952
RV There Yet:3854
PEAK:3520
It Takes Two:750
"""[1:-1]

games = {int(s[1]): s[0] for s in [l.split(':') for l in games.split('\n')]}

times = """
1 ЧАС:1 HOUR
2 ЧАСА:2 HOURS
3 ЧАСА:3 HOURS
4 ЧАСА:4 HOURS
5 ЧАСОВ:5 HOURS
6 ЧАСОВ:6 HOURS
12 ЧАСОВ:12 HOURS
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
    name = games[subcategory_id]
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
        acc.save_lot(lot)

for id in games:
    pass
    #fill_category(id)
