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

for game in games:
    lots = acc.get_my_subcategory_lots(game)
    for lot in lots:
        lot_fields = acc.get_lot_fields(int(lot.id))
        lot_fields.active = True
        print("Активируем", lot.title)
        acc.save_lot(lot_fields)
