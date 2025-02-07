"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Jan Zeman
email: zemanspeakwrite@gmail.com
discord: janzeman07
"""

# Vytvoříme slovník registrovaných uživatelů, kde je jméno klíč a heslo hodnota
registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Texty k analýze
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]   



# 1) Ověření přihlašovacích údajů

# pomocí podmínky if ověříme uživatelské jméno
# metoda lower způsobí, že nezáleží na velkých a malých písmenech
# vstup se vyhodnotí v malých písmenech i při zadání velkých
# pomocí fce input žádáme o zadání uživatelského jména 
# pokud uživatel zadá neplatné jméno program se ukončí
# při zadání správného uživatelského jména se jméno uloží 
# do proměnné username a program pokračuje dál
username = input("Enter your username: ")

if username.lower() not in registered_users:
    print("Invalid username")
    exit()

# Program žádá zadání hesla
password = input("Enter your password: ")

# Ověření hesla
# pokud heslo nesouhlasí program se ukončí, pokud se shoduje
# přivítá uživatele a nabídne 3 texty k analýze
if registered_users[username.lower()] != password:
    print("Invalid password")
    exit()

print(f"Welcome to the app, {username}!")
print("We have 3 texts to be analyzed.")


# 2) Výběr textu

# probíhá pomocí rezervovaných slov try a except
# pokud uživatel zadá jiné číslo než je v nabídce
# program vypíše hlášku neplatná volba a ukončí se
# pokud uživatel zadá jiný vstup než integer pomocí 
# except se ošetří výjimka, program vypíše hlášku
# neplatný vstup a ukončí se
# platný vstup se uloží do proměnné text_choice
try:
    text_choice = int(input("Enter a number btw. 1 and 3 to select: "))
    if text_choice not in [1, 2, 3]:
        print("Invalid choice")
        exit()
except ValueError:
    print("Invalid input")
    exit()

# protože python indexuje od nuly musíme od uživatelem vybraného
# čísla odečíst 1
selected_text = TEXTS[text_choice - 1]

# pomocí metody split rozdělíme text na seznam slov podle oddělovače
# tedy pomocí mezery a uložíme do proměnné words
words = selected_text.split()


# 3) Porovnávání textu

# pomocí fce len spočítáme počet objektů v seznamu words 
# a uložíme do proměnné word_count 
word_count = len(words)

# pomocí cyklu for procházíme slova 
# metoda istitle zjistí, zda slovo začíná velkým písmenem
# a zbytek slova je psán malými písmeny a ignoruje ostatní znaky jako čísla nebo interpunkce 
# pokud se podmínka vyhodnotí jako True pomocí fce sum přičteme 1 a
# tak spočítáme počet takových slov, které se uloží do proměnné title_case_words_count
title_case_words_count = sum(1 for word in words if word.istitle())

# metoda issuper zjistí zda je celé slovo psané velkými písmeny
# pomocí logického operátoru and připojíme metodu isalpha, která
# zjišťuje zda jsou ve slově pouze písmena
# pokud je podmínka vyhodnocena jako True, uložíme
# do proměnné uppercase_words_count
uppercase_words_count = sum(1 for word in words if word.isupper() and word.isalpha())

# metoda islower zjistí, zda je slovo psáno malými písmeny
# při splnění podmínky uložíme do proměnné lowercase_count
lowercase_count = sum(1 for word in words if word.islower())

# metoda isdigit zjistí zda konkrétní část textu obsahuje pouze číslice
# pomocí sum spočítáme počet takových objektů a uložíme do proměnné numeric_count
# která obsahuje počet čísel v textu
numeric_count = sum(1 for word in words if word.isdigit())

# vezmeme každé číslo, převedeme ho pomocí int na celé číslo a sečteme je
# proměnná numeric_count obsahuje součet čísel, která se v textu nacházejí."
numeric_sum = sum(int(word) for word in words if word.isdigit())


# 4) Vypis výsledků jednotlivých statistik

# pro přehlednější formátování použijeme f-string
print("-" * 40)
print(f"There are {word_count} words in the selected text.")
print(f"There are {title_case_words_count} titlecase words.")
print(f"There are {uppercase_words_count} uppercase words.")
print(f"There are {lowercase_count} lowercase words.")
print(f"There are {numeric_count} numeric strings.")
print(f"The sum of all the numbers {numeric_sum}")
print("-" * 40)


# 5) Výpočet délek slov a jejich četnost

# vytvoříme prázdný slovník word_lengths
# pomocí smyčky for procházíme seznam words
# metoda strip odstraní znaky uvedené v argumentu
# v našem případě tečky a čárky na konci slov 
# ve slovníku word_lengths je klíčem délka slova
# a hodnotou je počet slov dané délky v textu
# pokud je délka slova větší než nula, uložíme ho do 
# slovníku
# důležité je použití fce get, která zajišťuje, že pokud klíč 
# ještě není ve slovníku, nevyhodnotí to python jako chybu
# pokud délka slova (length) ještě ve slovníku neexistuje, get() vrátí výchozí hodnotu 0, 
# takže se přičte první výskyt slova této délky
word_lengths = {}
for word in words:
    length = len(word.strip(".,"))
    if length > 0:
        word_lengths[length] = word_lengths.get(length, 0) + 1

# Vytvoříme a vypíšeme sloupcový graf
# vypíšeme hlavičku pro: délku slova (LEN)
#                        výskyt znázorněný graficky pomocí * (OCCURENCES)  
#                        celkový počet slov dané délky v textu y (NR.)
print("LEN|  OCCURENCES  |NR.")

# pomocí opakovaného výpisu pomlčky graficky oddělíme hlavičku od dat
print("-" * 40)

# smyčka for prochází slovník a metoda items vrátí
# ze slovníku dvojici klíč, hodnota
# fce sorted vrátí nový seřazený seznam 
# tyto dvojice seřadí podle prvního prvku (délky slova)
# {length:>3} délka slova bude zarovnána doprava na šířku 3 znaků.
# vytvoří řetězec hvězdiček, kde každá hvězdička představuje jedno slovo dané délky
# tak, že znak hvězdičky vynásobíme počtem (count)  
# {count} ukazuje počet výskytů slov této délky pomocí čísel
for length, count in sorted(word_lengths.items()):
    print(f"{length:>3}|{'*' * count:<13}|{count}")
