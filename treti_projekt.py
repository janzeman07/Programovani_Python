"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Jan Zeman
email: zemanspeakwrite@gmail.com
discord: janzeman07

Instrukce pro uživatele:

1. Před spuštěním skriptu je nutné nainstalovat tyto moduly:
    - requests: pro práci s HTTP požadavky.
    - beautifulsoup4: pro parsování HTML.

    Do příkazové řádky (cmd nebo PowerShell) zadejte:
        pip install requests beautifulsoup4

2. Skript se spustí, když do příkazové řádky zadáte příkaz:
    python projekt_3.py <URL> <výstupní_soubor.csv>

     <URL> nahraďte adresou webové stránky, ze které chcete extrahovat data (například: "https://www.volby.cz").
    - <výstupní_soubor.csv> nahraďte názvem souboru, do kterého chcete uložit extrahovaná data (například: "volebni_vysledky.csv").

    Příklad:
        python projekt_3.py "https://www.volby.cz" "volebni_vysledky.csv"

3. Skript stáhne HTML obsah stránky, extrahuje data a uloží je do CSV souboru, který bude umístěn ve stejném adresáři jako skript.

Pokud skript nefuguje kontaktujte mě prosím pomocí emailu: zemanspeakwrite@gmail.com
"""
# Import modulů:

# Modul sys pracuje s příkazovou řádkou a jejími argumenty (sys.arvg)
# a umožňuje získat vstupní parametry, které uživatel zadá po spuštění skriptu.

import sys

# Modul requests stahuje data z webových stránek pomocí HTTP požadavků.
# Pomocí něj načteme HTML kód stránky s volebními výsledky.

import requests

# Z modulu bs4 importujeme třídu BeautifulSoup.
# Použijeme ho k parsování HTML a získání dat ze stažené webové stránky.

from bs4 import BeautifulSoup

# Pomocí modulu csv pracujeme se soubory ve formátu CSV
# a ukládáme nebo čteme data v tomto formátu.
# připravuje prostředí pro web scraping.

import csv

# Funkce pro kontrolu argumentů.
# Funkce check_arguments() ověřuje správný počet argumentů zadaných uživatelem.
# Metoda sys.argv je seznam argumentů příkazové řádky
# Sys.argv[0] je název skriptu, sys.argv[1] je URL webové stránky a sys.argv[2] je jméno výstupního souboru
# Pokud není počet argumentů roven třem (název skriptu, URL web. stránky, vstupní soubor) skript upozorní uživatele jak zadat argumenty
# a ukončí skript pomocí sys.exit(1).
# Při správném počtu argumentů vrátí funkce hodnoty sys.argv[1] a sys.argv[2].

def check_arguments():
    if len(sys.argv) != 3:
        print("Použití: python projekt_3.py <URL> <výstupní_soubor.csv>")
        sys.exit(1)
    return sys.argv[1], sys.argv[2]

# Pomocí funkce get_page_content(url) extrahujeme HTML obsah stránky. 
# Funkce přijímá jako argument URL webové stránky, z které chceme extrahovat HTML obsah.
# Funkce requests.get(url) odesílá HTTP GET požadavek na zvolenou URL a tím načítá obsah stránky.
# Proměnná response obsahuje odpověď serveru, resp. informace jako je kód a obsah stránky.
# Pomocí podmínky if response.status_code != 200: ověřujeme stavový kód odpovědi.
# Při správném načtení vrátí status kód 200, který znamená úspěšné načtení stránky.
# Pokud vrátí jakýkoliv jiný, indikuje to chybu načtení.
# Program v tom případě informuje uživatele a metoda sys.exit(1) ukončí program s návratovým kódem 1(standartní kód chyby).
# Atribut response.text obsahuje HTML kód odpovědi serveru ve formě řetězce.

def get_page_content(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Chyba při stahování stránky")
        sys.exit(1)
    return response.text

# 
# Definujeme funkci extrakci_dat z HTML, kde je vstupní argument string obsahující HTML kód stránky.
# Proměnná soup obsahuje objekt BeautifulSoup, který je třídou modulu bs4,a který bude analyzovat HTML kód.
# První poziční argument je HTML kód, který chceme parsovat, druhý je "htlml.parser", který udává konkrétní parser jaký budeme používat.
# Proměnná rows obsahuje seznam všech objektů tabulkových řádků v HTML dokumentu.
# Metoda find all vyhledá všechny HTML prvky a uloží je do proměnné rows.
# Vytvoříme proměnnou data, do které budeme ukládat extrahovaná data.
# Iterujeme pomocí smyčky for všechny objekty kromě prvních dvou řádků, kde je hlavička.
# Proměnná cells obsahuje seznam všech prvků td buněk nalezené pomocí metody find all.
# Funkce len ověří, zda řádek obsahuje alespoň jednu buňku a nebude analyzovat prázdné řádky.
# Pomocí text získámé obsah první buňky a uložíme do proměnná code, metoda strip odstraní mezery a nové řádky.
# Další proměnné obsahují důležité údaje jako platné hlasy a registrované voliče.
# Proměnná party_votes obsahuje všechny zbývající buňky tabulky, které obsahují hlasy pro jednotlivé strany.
# Pro každou buňku cell od pátého indexu se provede text strip a vrátí seznam hlasů jednotlivých stran.
# Pomocí metody append přidáme zaznam do proměnné data.


def extract_data(html):
    soup = BeautifulSoup(html, "html.parser")
    rows = soup.find_all("tr") 
    data = []
    for row in rows[2:]: 
        cells = row.find_all("td")
        if len(cells) > 0:
            code = cells[0].text.strip()
            location = cells[1].text.strip()
            registered = cells[2].text.strip()
            envelopes = cells[3].text.strip()
            valid = cells[4].text.strip()
            party_votes = [cell.text.strip() for cell in cells[5:]]
            data.append([code, location, registered, envelopes, valid] + party_votes)
    return data

# Definujeme funkci save_to_csv, která jako argumenty přijímá název vstupního CSV souboru (filename) a seznam s volebními daty (data).
# Otevřeme soubor pomocí funkce open pro zápis 'w'(write), newline zajistí správné formátování a enconding pomocí kódování UTF-8 ukládání české diakritiky.
# With zajistí zavření souboru po opuštění bloku. 
# Vytvoříme objekt writer, který umožňuje zápis do souboru ve formátu CSV.
# Header je proměnná obsahující kód oblasti, její název, registrované voliče, obálky a platné hlasy.
# List comprehension vytvoří názvy sloupců pro politické strany na základě počtu dat v prvním řádku.
# Od prvního řádku[0] odečteme prvních 5 položek, které obsahují základní informace(kód oblasti atd.)
# Pomocí metoy writer.writerow(header) zapíšeme záhlaví jako první řádek do souboru
# Metodou writer.writerows(data) iterujeme přes seznam dat a zapisujeme každý vnořený seznam jako jeden řádek.
# Vypíšeme hlášku pro uživatele oznamující uložení souboru.

def save_to_csv(filename, data):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        header = ["code", "location", "registered", "envelopes", "valid"] + [f"party_{i}" for i in range(len(data[0]) - 5)]
        writer.writerow(header)
        writer.writerows(data)
    print(f"Data byla uložena do souboru {filename}")

# Použití if __name__ == "__main__": zajistí, že se zbytek kódu spustí pouze pokud je spuštěn přímo.
# Zavoláme funkce: funkce check_arguments(), díky níž ověříme správný počet zadaných argumentů.
# Funkce get_page_content(url) stáhne obsah stránky HTML na zadanou adresu.
# Funkce extract_data(page_content) získá data ze staženého HTML kódu.
# Funkce save_to_csv(output_file, extracted_data), uloží do CSV souboru, jehož jméno zadal uživatel extrahovaná data.

if __name__ == "__main__":
    url, output_file = check_arguments()
    page_content = get_page_content(url)
    extracted_data = extract_data(page_content)
    save_to_csv(output_file, extracted_data)
