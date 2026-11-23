# CVIČENÍ - Podmínky
# Vypracuj jednotlivé úkoly podle zadání
# Používej if, elif, else a logické operátory
# Vstupní hodnoty získávej pomocí input(), pokud není uvedeno jinak
# Programy testuj také s hraničními hodnotami



# ÚKOL 1 - Kladné, záporné nebo nulové číslo
# Načti od uživatele celé číslo
# Pomocí if, elif a else urči, zda je:
#   Kladné
#   Záporné
#   Nulové
# Vypiš odpovídající zprávu



# ÚKOL 2 - Sudé nebo liché číslo
# Načti od uživatele celé číslo
# Pomocí operátoru % urči, zda je sudé nebo liché
# Použij úplné větvení if/else
# Otestuj program také se zápornými čísly a nulou



# ÚKOL 3 - Hodnocení testu
# Načti počet bodů v rozsahu 0 až 100
# Podle výsledku vypiš hodnocení:
#   90–100 bodů: Výborný
#   75–89 bodů: Velmi dobrý
#   50–74 bodů: Splněno
#   0–49 bodů: Nesplněno
# Pokud uživatel zadá hodnotu mimo rozsah 0–100, vypiš informaci o neplatném počtu bodů
# Otestuj všechny hranice jednotlivých intervalů



# ÚKOL 4 - Největší ze tří čísel
# Načti tři celá čísla
# Urči a vypiš největší z nich
# Používej porovnávací a logické operátory
# Nepoužívej funkci max()
# Otestuj také situaci, kdy jsou některá čísla stejná



# ÚKOL 5 - Přístup do systému
# Načti od uživatele:
#   Věk
#   Informaci, zda má povolení (ano/ne)
#   Informaci, zda má zákaz (ano/ne)
# Přístup je povolen, pokud:
#   Uživatel je plnoletý nebo má povolení
#   A zároveň nemá zákaz
# Použij složenou podmínku s operátory and, or, not
# Vypiš, zda je přístup povolen nebo zamítnut
# Vyzkoušej různé kombinace vstupních hodnot



# ÚKOL 6 - Vnořené podmínky
# Načti věk uživatele a informaci, zda má vstupenku (ano/ne)
# Pokud je uživatel plnoletý:
#   Zkontroluj, zda má vstupenku
#   Pokud ano, povol vstup
#   Pokud ne, vypiš informaci o chybějící vstupence
# Pokud uživatel není plnoletý:
#   Vypiš informaci o nesplněné věkové podmínce
# Použij vnořené podmínky



# ÚKOL 7 - Složená a vnořená podmínka
# Vytvoř dvě varianty programu pro kontrolu vstupu
# Vstup je povolen, pokud:
#   Uživatel má alespoň 18 let
#   A zároveň má vstupenku
#
# Varianta A - Použij jednu složenou podmínku s and
# Varianta B - Použij vnořené podmínky
#
# Obě varianty musí při stejných vstupech rozhodnout stejně



# ÚKOL 8 - Odhadni výstup
# Nejdříve odhadni, co program vypíše
# Potom kód odkomentuj a svůj odhad ověř
# Vysvětli, proč se některé větve nevykonají

# x = 15
# if x > 0:
#     print("A")
# elif x > 10:
#     print("B")
# else:
#     print("C")
#
# if x > 0:
#     print("D")
#
# if x > 10:
#     print("E")



# ÚKOL 9 - Oprava logických chyb
# Následující programy obsahují logické chyby
# Najdi je a oprav tak, aby odpovídaly zadání

# A - Program má povolit vstup pouze lidem ve věku 18 nebo 21 let

# vek = 16
#
# if vek == 18 or 21:
#     print("Vstup povolen")
# else:
#     print("Vstup zamítnut")


# B - Program má rozlišovat dospělé a seniory
# Senior je člověk od 65 let

# vek = 70
#
# if vek >= 18:
#     print("Dospělý")
# elif vek >= 65:
#     print("Senior")
# else:
#     print("Nezletilý")



# BONUS - Přestupný rok
# Načti od uživatele letopočet
# Urči, zda se jedná o přestupný rok
#
# Rok je přestupný, pokud:
#   Je dělitelný 4
#   A zároveň není dělitelný 100
#   Nebo je dělitelný 400
# Použij složenou podmínku
# Ověř program například pro roky:
#   2024 - přestupný
#   2025 - nepřestupný
#   1900 - nepřestupný
#   2000 - přestupný# PROJEKT - Jednoduchá kalkulačka
# CÍL: Vytvoř program, který provádí základní matematické operace
# Použij vstup od uživatele, operátory a podmíněné příkazy


# ZADÁNÍ

# 1. VSTUP
# Načti od uživatele:
#   První číslo
#   Matematický operátor (+, -, *, /)
#   Druhé číslo
# Čísla načítej jako float
# Operátor ponech jako řetězec


# 2. VÝPOČET
# Pomocí if, elif a else urči, kterou operaci program provede:
#   +  Sčítání
#   -  Odčítání
#   *  Násobení
#   /  Dělení
# Výsledek výpočtu ulož do proměnné vysledek


# 3. KONTROLA CHYB
# Program musí rozpoznat:
#   Neplatný operátor
#   Pokus o dělení nulou
# V obou případech vypiš odpovídající chybovou zprávu
# Neprováděj výpočet, který není možné správně dokončit
# Nepoužívej zatím try/except


# 4. VÝSTUP
# Pomocí f-stringu vypiš výsledek ve formátu:
#   10 + 5 = 15
# Výsledek vypiš pouze tehdy, pokud byl výpočet úspěšný
# Výsledek může obsahovat desetinná místa
# Není nutné odstraňovat nepotřebné nuly


# PŘÍKLADY SPUŠTĚNÍ
# Zadej první číslo: 10
# Zadej operátor (+, -, *, /): *
# Zadej druhé číslo: 5
# Výsledek: 10 * 5 = 50
#
# Zadej první číslo: 10
# Zadej operátor (+, -, *, /): /
# Zadej druhé číslo: 0
# Chyba: Nulou nelze dělit
#
# Zadej první číslo: 10
# Zadej operátor (+, -, *, /): %
# Zadej druhé číslo: 5
# Chyba: Neplatný operátor


# POŽADAVKY
# Používej výstižné názvy proměnných ve stylu snake_case
# Pro výběr operace použij if, elif a else
# Ošetři dělení nulou
# Ošetři neplatný operátor
# Výsledek vypisuj pomocí f-stringu
# Program musí správně fungovat pro kladná i záporná čísla


# TESTOVÁNÍ
# Ověř program alespoň pro následující případy:
#   10 + 5       → 15
#   10 - 5       → 5
#   10 * 5       → 50
#   10 / 4       → 2.5
#   -10 + 5      → -5
#   10 / 0       → Chyba
#   10 % 5       → Neplatný operátor
# Zkontroluj, že se při chybě nevypisuje žádný výsledek


# BONUS
# 1. Rozšiř kalkulačku o další operace:
#    //  Celočíselné dělení
#    %   Zbytek po dělení
#    **  Umocňování
#
# 2. Uprav výpis tak, aby se desetinná čísla
#    zobrazovala nejvýše na dvě desetinná místa
#
# 3. Přidej možnost výpočtu druhé odmocniny
#    Uživatel zadá operátor sqrt
#    Pro tuto operaci program požaduje pouze jedno číslo
#    Uprav podle toho načítání vstupních hodnot
#    Záporné číslo musí program odmítnout
#    Zjisti, jak odmocninu vypočítat pomocí operátoru **


# VLASTNÍ ŘEŠENÍ: