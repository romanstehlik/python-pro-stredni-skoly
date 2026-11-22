# Vstup a výstup

Dosavadní programy pracovaly především s hodnotami, které byly přímo zapsané ve zdrojovém kódu. Pokud jsme chtěli například změnit věk uživatele nebo cenu výrobku, museli jsme upravit hodnotu příslušné proměnné.

Python umožňuje získávat údaje také během běhu programu. Díky tomu může stejný program pracovat s různými hodnotami, aniž bychom museli měnit jeho zdrojový kód.

V této lekci se naučíme získávat vstup od uživatele, převádět datové typy a formátovat výstup programu.

## 1. Vstup a výstup programu

Většinu jednoduchých programů můžeme rozdělit na tři základní části:

| Část | Význam | Příklad |
|---|---|---|
| Vstup | Získání údajů potřebných pro výpočet | Zadání ceny výrobku |
| Zpracování | Provedení operací nad získanými údaji | Výpočet celkové ceny |
| Výstup | Zobrazení výsledku | Vypsání ceny nákupu |

Tento princip jsme již poznali při návrhu algoritmů.

V Pythonu budeme prozatím používat dvě základní funkce:

- `input()` – získání vstupu od uživatele prostřednictvím terminálu
- `print()` – výpis hodnot do terminálu

## 2. Funkce input()

Funkce `input()` umožňuje uživateli zadat hodnotu prostřednictvím terminálu.

Program při jejím zavolání čeká, dokud uživatel nezadá vstup a nepotvrdí jej klávesou Enter.

```python
jmeno = input("Zadej své jméno: ")

print("Ahoj,", jmeno)
```

Příklad spuštění:

```text
Zadej své jméno: Petr
Ahoj, Petr
```

**Text uvedený v závorkách funkce `input()` slouží jako výzva pro uživatele.**

Zadaná hodnota se následně uloží do proměnné `jmeno`.

### Datový typ vstupu

**Funkce `input()` vždy vrací hodnotu typu `str`, tedy textový řetězec.**

To platí i v případě, že uživatel zadá číslo.

```python
vek = input("Zadej svůj věk: ")

print(vek)
print(type(vek))
```

Pokud uživatel zadá `16`, výsledkem bude:

```text
16
<class 'str'>
```

Python tedy pracuje s textem `"16"`, nikoliv s celým číslem `16`.

Tento rozdíl je důležitý zejména při výpočtech.

## 3. Převody datových typů

Pokud potřebujeme se zadanou hodnotou počítat, musíme ji převést na odpovídající datový typ.

K tomu používáme například následující funkce:

| Funkce | Význam | Příklad |
|---|---|---|
| `int()` | Převod na celé číslo | `int("15")` → `15` |
| `float()` | Převod na desetinné číslo | `float("15.5")` → `15.5` |
| `str()` | Převod na textový řetězec | `str(15)` → `"15"` |

### Převod na celé číslo

```python
vek = input("Zadej svůj věk: ")
vek = int(vek)

print("Za rok ti bude:", vek + 1)
```

Nejprve získáme textový vstup a následně jej převedeme na celé číslo.

Oba kroky můžeme také spojit:

```python
vek = int(input("Zadej svůj věk: "))

print("Za rok ti bude:", vek + 1)
```

Python nejprve vykoná vnitřní funkci `input()` a potom předá její výsledek funkci `int()`.

### Převod na desetinné číslo

Pokud potřebujeme pracovat s desetinnými čísly, použijeme `float()`.

```python
vyska = float(input("Zadej svou výšku v metrech: "))

print("Tvoje výška:", vyska, "m")
```

Desetinná čísla zapisujeme v Pythonu s tečkou, nikoliv s čárkou.

```text
Zadej svou výšku v metrech: 1.75
Tvoje výška: 1.75 m
```

### Převod na text

Funkce `str()` převede hodnotu na textový řetězec.

```python
vek = 16

text = "Je mi " + str(vek) + " let"

print(text)
```

Bez převodu bychom nemohli pomocí operátoru `+` přímo spojit řetězec a celé číslo.

Při výpisu pomocí `print()` však tento převod obvykle nepotřebujeme:

```python
vek = 16

print("Je mi", vek, "let")
```

Funkce `print()` dokáže vypsat hodnoty různých datových typů.

## 4. Výstup pomocí print()

Funkci `print()` jsme používali již v předchozích lekcích.

Umožňuje vypsat text, hodnoty proměnných i výsledky výrazů.

```python
jmeno = "Petr"
vek = 16

print("Jméno:", jmeno)
print("Věk:", vek)
print("Za rok:", vek + 1)
```

### Výpis více hodnot

Jednotlivé hodnoty můžeme oddělit čárkami.

```python
jmeno = "Petr"
vek = 16

print("Student", jmeno, "má", vek, "let")
```

Funkce `print()` mezi hodnoty standardně vkládá mezery.

### Parametr sep

Parametr `sep` určuje, jakým znakem nebo textem budou jednotlivé hodnoty odděleny.

```python
print("Python", "Java", "C++", sep=", ")
print(2026, 11, 22, sep="-")
```

Výstup:

```text
Python, Java, C++
2026-11-22
```

Pokud parametr `sep` neuvedeme, použije se mezera.

### Parametr end

Funkce `print()` standardně ukončuje výpis přechodem na nový řádek.

Pomocí parametru `end` můžeme toto chování změnit.

```python
print("Ahoj", end=" ")
print("světe!")
```

Výstup:

```text
Ahoj světe!
```

Parametr `end` určuje, co se vypíše na konci daného příkazu.

## 5. Formátování výstupu pomocí f-stringů

Při vytváření delších výpisů může být oddělování textu a proměnných čárkami nepřehledné.

Python proto nabízí **formátované řetězce**, označované jako *f-stringy*.

Před úvodní uvozovky řetězce zapíšeme písmeno `f`. Hodnoty proměnných nebo výrazy potom vkládáme do složených závorek `{}`.

```python
jmeno = "Petr"
vek = 16

print(f"Jmenuji se {jmeno} a je mi {vek} let")
```

Výstup:

```text
Jmenuji se Petr a je mi 16 let
```

Do složených závorek můžeme vložit také výraz:

```python
vek = 16

print(f"Za rok mi bude {vek + 1} let")
```

### Formátování čísel

Pomocí f-stringů můžeme ovlivnit způsob zobrazení čísel, například počet desetinných míst nebo použitou číselnou soustavu.

Za proměnnou nebo výraz ve složených závorkách zapíšeme dvojtečku `:` a požadovaný formát.

#### Desetinná čísla

```python
cena = 149.9876

print(f"Cena: {cena:.2f} Kč")  # 149.99 Kč
print(f"Cena: {cena:.1f} Kč")  # 150.0 Kč
print(f"Cena: {cena:.0f} Kč")  # 150 Kč
```

Zápis `.2f` znamená zobrazení čísla na dvě desetinná místa.

Python při formátování hodnotu zaokrouhlí pro účely výpisu. Původní hodnota proměnné se nezmění.

#### Číselné soustavy

Celá čísla můžeme zobrazovat také v různých číselných soustavách.

```python
cislo = 42

print(f"Desítková: {cislo:d}")       # 42
print(f"Dvojková: {cislo:b}")        # 101010
print(f"Osmičková: {cislo:o}")       # 52
print(f"Šestnáctková: {cislo:x}")    # 2a
```

| Formát | Číselná soustava | Základ |
|---|---|:---:|
| `d` | Desítková (decimální) | 10 |
| `b` | Dvojková (binární) | 2 |
| `o` | Osmičková (oktální) | 8 |
| `x` | Šestnáctková (hexadecimální) | 16 |
| `X` | Šestnáctková s velkými písmeny | 16 |

Při práci s binárními čísly můžeme určit také minimální šířku výpisu a doplnění nulami zleva.

```python
cislo = 5

print(f"{cislo:b}")      # 101
print(f"{cislo:08b}")    # 00000101
print(f"{cislo:016b}")   # 0000000000000101
```

Zápis `08b` znamená zobrazení čísla ve dvojkové soustavě s minimální šířkou 8 znaků, přičemž chybějící pozice se doplní nulami zleva.

Takový zápis je užitečný například při práci s osmibitovými hodnotami.

#### Další možnosti formátování

Python podporuje i další způsoby formátování čísel.

```python
cislo = 0.756
velke_cislo = 1234567

print(f"{cislo:.1%}")           # 75.6 %
print(f"{velke_cislo:,}")       # 1,234,567
print(f"{velke_cislo:_}")       # 1_234_567
```

**Formátování ovlivňuje pouze výsledný textový výstup, nikoliv hodnotu nebo datový typ proměnné.**

## 6. Speciální znaky v řetězcích

Některé znaky mají uvnitř textových řetězců zvláštní význam.

Zapisují se pomocí zpětného lomítka `\` a označují se jako **únikové sekvence**.

| Zápis | Význam |
|---|---|
| `\n` | Nový řádek |
| `\t` | Tabulátor |
| `\"` | Uvozovka uvnitř řetězce |
| `\\` | Zpětné lomítko |

Příklad:

```python
print("První řádek\nDruhý řádek")
print("Jméno:\tPetr")
print("Řekl: \"Ahoj!\"")
```

Výstup:

```text
První řádek
Druhý řádek
Jméno:  Petr
Řekl: "Ahoj!"
```

Únikové sekvence nám umožňují lépe uspořádat textový výstup.

## 7. Časté chyby při práci se vstupem

Při získávání údajů od uživatele je důležité počítat s tím, že zadané hodnoty nemusí odpovídat očekávanému datovému typu.

### Sčítání textových řetězců

```python
a = input("První číslo: ")
b = input("Druhé číslo: ")

print(a + b)
```

Pokud uživatel zadá čísla `10` a `5`, program vypíše:

```text
105
```

Důvodem je, že obě hodnoty jsou řetězce a operátor `+` je spojí.

Správný postup:

```python
a = int(input("První číslo: "))
b = int(input("Druhé číslo: "))

print(a + b)
```

Výsledkem bude číslo `15`.

### Chyba ValueError

Při převodu textu na číslo může nastat chyba `ValueError`.

```python
vek = int(input("Zadej svůj věk: "))
```

Pokud uživatel zadá například `Petr`, převod se nezdaří.

```text
ValueError: invalid literal for int() with base 10: 'Petr'
```

Funkce `int()` totiž nedokáže převést libovolný text na celé číslo.

Podobná chyba nastane také při zadání desetinného čísla `15.5` do funkce `int()`.


### Převod na bool

Při práci s logickými hodnotami může být použití funkce `bool()` překvapivé.

```python
print(bool("True"))    # True
print(bool("False"))   # True
print(bool(""))        # False
```

Funkce `bool()` nepřevádí text `"True"` nebo `"False"` podle jeho významu.

U neprázdných řetězců vrací `True`, zatímco u prázdného řetězce vrací `False`.

Proto následující zápis není vhodný pro načítání odpovědi ano/ne:

```python
souhlas = bool(input("Souhlasíš? "))
```

Správné zpracování různých uživatelských odpovědí si ukážeme při práci s podmínkami.

## 8. Kompletní příklad – Výpočet ceny nákupu

Následující program propojuje vstup, převody datových typů, výpočty a formátovaný výstup.

```python
nazev = input("Název výrobku: ")
cena = float(input("Cena za kus: "))
pocet = int(input("Počet kusů: "))

celkova_cena = cena * pocet

print()
print("===== NÁKUP =====")
print(f"Výrobek: {nazev}")
print(f"Cena za kus: {cena:.2f} Kč")
print(f"Počet kusů: {pocet}")
print(f"Celková cena: {celkova_cena:.2f} Kč")
```

Příklad spuštění:

```text
Název výrobku: Sešit
Cena za kus: 35.5
Počet kusů: 6

===== NÁKUP =====
Výrobek: Sešit
Cena za kus: 35.50 Kč
Počet kusů: 6
Celková cena: 213.00 Kč
```

Program nyní může pracovat s různými výrobky, cenami a počty kusů bez nutnosti upravovat zdrojový kód.

## 9. Ověření znalostí

1. Jaký je rozdíl mezi vstupem a výstupem programu?
2. K čemu slouží funkce `input()`?
3. Jaký datový typ vrací funkce `input()`?
4. Proč je nutné při některých výpočtech převádět vstup pomocí `int()` nebo `float()`?
5. Jaký je rozdíl mezi funkcemi `int()` a `float()`?
6. K čemu slouží parametry `sep` a `end` funkce `print()`?
7. Co je f-string a jak se zapisuje?
8. Jak zobrazíme desetinné číslo na dvě desetinná místa?
9. K čemu slouží speciální znaky `\n` a `\t`?
10. Kdy může vzniknout chyba `ValueError`?
11. Proč `bool("False")` vrací hodnotu `True`?

---

**Předchozí lekce:** [Operátory a výrazy](../04-operatory_a_vyrazy/)

**Další lekce:** [Podmínky](../06-podminky/)