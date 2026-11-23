# PROJEKT - Jednoduchá kalkulačka
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
