
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
    remaining_digits = random.sample([dig for dig in "0123456789" if dig != first_digit], 3) 
    return first_digit + ''.join(remaining_digits)  

# Definujeme funkci pro vyhodnocení číslic, kdy hráč uhodnul číslo i pozici (bulls) nebo jen pozici(cows),  
# funkce má dva parametry: vygenerované číslo a hráčův tip.
# Proměnná bulls, range(4): iterací zjišťujeme pozici
# a pomocí podmínky ověřujeme zda se shoduje vygenerované číslo a tip hráče.
# Proměnná cows, iterujeme přes každou číslici v hráčově tipu a ověříme, zda se číslice shoduje s vygenerovaným číslem.
# Pomocí funkce sum spočítáme množství bulls and cows.

# Funkce pro vyhodnocení číslic, kdy hráč uhodnul číslo i pozici (bulls) nebo jen pozici (cows).  
def evaluate_guess(secret_number, guess):
    bulls = sum(1 for i in range(4) if secret_number[i] == guess[i])
    
    # Použijeme seznamy, abychom správně spočítali "cows"
    secret_list = list(secret_number)
    guess_list = list(guess)

    # Odstraníme všechny správně umístěné číslice (bulls)
    for i in range(4):
        if secret_list[i] == guess_list[i]:
            secret_list[i] = guess_list[i] = None  # Nahrazujeme správně uhodnuté číslice

    # Počet cows spočítáme tím, že procházíme zbývající číslice
    cows = 0
    for digit in guess_list:
        if digit and digit in secret_list:
            cows += 1
            secret_list[secret_list.index(digit)] = None  # Odstraníme započítanou číslici

    return bulls, cows

# Funkce pro spuštění hry
def play_game():
    secret_number = generate_number()  
    count_of_guesses = 0  

    print("Hi buddy, let's have fun!")
    print(52 * "-")
    print("Let's guess a four-digit number.")
    print("Show me how good you are at the game Bulls and Cows!")
    print(52 * "-")

    # Do proměnné start_time uložíme aktuální čas pomocí metody time z modulu time.
    start_time = time.time()  

    while True:
        guess = input("Enter a number: ").strip()

        if guess[0] == '0': 
            print("Invalid input. The first digit cannot be zero.")  
            continue  

        # Zkontrolujeme zda je zadaný vstup číslo
        if not guess.isdigit():
            print("Invalid input. Please enter only numbers.")
            continue

        # Kontrola, zda je číslo čtyřmístné a unikátní
        if len(guess) != 4 or len(set(guess)) != 4:
            print("Invalid input. Please enter a 4-digit number with unique digits.")
            continue

        count_of_guesses += 1
        bulls, cows = evaluate_guess(secret_number, guess)

        # Pokud hráč uhodne všechna čísla a pozice (bulls = 4), hra končí.
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

# Funkce pro pokračování nebo ukončení
def continue_game():
    while True:
        print("Stiskněte enter pro ukončení.")
        print("Zadejte číslo, pokud chcete pokračovat v hraní.")
        user_input = input("Enter a number: ").strip()
        
        if user_input == '':
            print("Thanks for playing! Goodbye!")
            break
        else:
            play_game()  # Znovu spustí hru

# Spuštění první hry
play_game()

# Možnost pokračování nebo ukončení
continue_game()