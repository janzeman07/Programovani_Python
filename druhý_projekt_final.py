# Importujeme modul random, který bude generovat náhodná čísla.

import random

# Importujeme modul time pomocí nějž měříme čas, který hráč potřebuje k uhodnutí čísla.

import time 

# Funkce pro generování náhodného čtyřciferného čísla.
# Metoda choice z modulu random vybere náhodné číslo z řetězce 123456789 a uloží ho do proměnné first_digit.
# Proměnná remaining_digits obsahuje seznam tří číslic 0-9 kromě první číslice (first_digit). 
# Metoda replace odstraní už vybranou první číslici, aby se neopakovala v dalších číslicích.
# Metoda sample vybere 3 unikátní číslice z 0-9.
# Proměnná secret_number spojí první vybranou číslici a zbývající 3.
# Metoda shuffle promíchá čísla pro větší variabilitu a zamezí předvídatelnosti čísla.

def generate_number(): 
    first_digit = random.choice("123456789")
    remaining_digits = random.sample("0123456789".replace(first_digit, ""), 3)
    secret_number = [first_digit] + remaining_digits  
    random.shuffle(secret_number)  
    return ''.join(secret_number)  

# Definujeme funkci pro vyhodnocení číslic, kdy hráč uhodnul číslo i pozici (bulls) nebo jen pozici(cows),  
# funkce má dva parametry: vygenerované číslo a hráčův tip.
# Proměnná bulls, range(4): iterací zjišťujeme pozici
# a pomocí podmínky ověřujeme zda se shoduje vygenerované číslo a tip hráče.
# Proměnná cows, iterujeme přes každou číslici v hráčově tipu a ověříme, zda se číslice shoduje s vygenerovaným číslem.
# Pomocí funkce sum spočítáme množství bulls and cows.

def evaluate_guess(secret_number, guess):
    bulls = sum(1 for i in range(4) if secret_number[i] == guess[i])
    cows = sum(1 for digit in guess if digit in secret_number) - bulls
    return bulls, cows

# Zavoláme funkci pro generování náhodného čísla a uložíme ji do proměnné secret_number.
# Proměnná count_of_guesses uchovává počet pokusů hráče, před započnutím hádání je nastavena na nula.

def play_game():
    secret_number = generate_number()  
    count_of_guesses = 0  

    print("Hi buddy, let's have fun!")
    print(47 * "-")
    print("Let's guess a four-digit number.")
    print("Show me how good you are at the game Bulls and Cows!")
    print(47 * "-")

# Do proměnné start_time uložíme aktuální čas pomocí metody time z modulu time,
# referenční rámec je unixový čas od roku 1970, na kterém je shoda
# a vrátí aktuální čas v sekundách jako desetinné číslo.
# Dokud hráč neuhodne číslo, poběží podmínka while.
# Vyzveme hráče k zadání čísla a použijeme metodu strip pro odstranění případných mezer,
# které mohl hráč zadat. Zajistíme také, že hráč nemůže zadat číslo s nulou na začátku,
# protože takové číslo je de facto trojciferné. Pokud je vstup neplatný, použijeme continue k pokračování programu.

    start_time = time.time()  

    while True:
        guess = input("Enter a number: ").strip()

        if guess[0] == '0': 
            print("Invalid input. The first digit cannot be zero.")  
            continue  


# Pomocí podmínky zkontrolujeme zda je zadaný vstup číslo a
# pokud není, program upozorní hráče na neplatný vstup.

        if not guess.isdigit():
            print("Invalid input. Please enter only numbers.")
            continue

# If a logický operátor or zjistí, zda je číslo čtyřmístné a zda se neopakuje a to
# pomocí funkce len a převodu čísla na set, kde mohou být jen unikátní prvky.
# Pokud neplatí minimálně jedna podmínka upozorníme hráče.

        if len(guess) != 4 or len(set(guess)) != 4:
            print("Invalid input. Please enter a 4-digit number with unique digits.")
            continue

# Zvyšujeme hodnotu proměnné count_of_guesses o 1 při každém pokusu.
# Voláme funkci evaluate_guess, která vrátí počet bulls a cows.

        count_of_guesses += 1
        bulls, cows = evaluate_guess(secret_number, guess)

# Pokud hráč uhodne všechna čísla a pozice (bulls = 4), hra končí.
# Do proměnné end_time uložíme čas, který byl naměřen ve chvíli, kdy má hráč 4 bulls.
# Do proměnné duration uložíme rozdíl počátečního a koncového času, resp. dobu trvání hry.
# Zaokrouhlíme na dvě desetinná místa pomocí formátování f stringu.
# Pokud hráč neuhodl všechna čísla (bulls), vypíše se počet bulls a cows.

        if bulls == 4:
            end_time = time.time() 
            duration = end_time - start_time  
            print(f"Congratulations, you've guessed all 4 digits correctly!")  
            print(f"It took you {duration:.2f} seconds.")  

            break
        else:
            print(f"{bulls} bull(s), {cows} cow(s)")
            
# Vyhodnotíme výsledky hráče podle počtu pokusů a vypíšeme hodnocení           

    if count_of_guesses <= 8:
        print("Amazing result, you're an excellent Bulls and Cows player!")
    elif count_of_guesses <= 12:
        print("Good result.")
    else:
        print("No offense, but there's room for improvement.")

# Spuštění hry
play_game()
