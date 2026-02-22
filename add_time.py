from FunPayAPI import Account, Runner, types, enums
import copy

TOKEN = ""

acc = Account(TOKEN).get()

times = """24 ЧАСА:24 HOURS
2 ДНЯ:2 DAYS
3 ДНЯ:3 DAYS
5 ДНЕЙ:5 DAYS
7 ДНЕЙ:7 DAYS"""

games = {}

games[2792] = 'Satisfactory'
games[3472] = 'REMATCH'
games[2786] = 'EA SPORTS FC 25'
games[1795] = 'Sons of the Forest'
games[3176] = 'Split Fiction'
games[2198] = 'Assetto Corsa'
games[868] = 'Dying Light'
games[3549] = 'Little Nightmares'
games[1997] = 'BeamNG.drive'
games[1756] = 'Ready or Not'
games[2952] = 'Phasmophobia'
games[3854] = 'RV There Yet'
games[3520] = 'PEAK'
games[750] = 'It Takes Two'

for game in games:
    lots = acc.get_my_subcategory_lots(game)
    copy_lot = None
    for lot in lots:
        if 'АРЕНДА 1 ЧАС' in lot.title:
            copy_lot = lot
            break
    if copy_lot is None:
        continue
    copy_lot = acc.get_lot_fields(int(copy_lot.id))
    title_ru = copy_lot.title_ru.replace("1 ЧАС", "%t")
    title_en = copy_lot.title_en.replace("1 HOUR", "%t")
    copy_lot.lot_id = 0
    for time in times.split('\n'):
        time = time.split(':')
        new_lot = copy.deepcopy(copy_lot)
        new_lot.title_ru = title_ru.replace('%t', time[0])
        new_lot.title_en = title_en.replace('%t', time[1])
        acc.save_lot(new_lot)
