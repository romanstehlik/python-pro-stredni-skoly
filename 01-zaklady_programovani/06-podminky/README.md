# Podmínky

Dosavadní programy vykonávaly příkazy postupně, zpravidla od prvního řádku k poslednímu. Tento způsob vykonávání označujeme jako **sekvenci**.

V praxi však často potřebujeme, aby program vykonal různé příkazy podle aktuální situace. Například ověřil věk uživatele, rozhodl o nároku na slevu nebo zkontroloval správnost zadaných údajů.

Takové rozhodování označujeme jako **větvení programu**.

V Pythonu k němu používáme podmíněné příkazy `if`, `elif` a `else`.

## 1. Podmíněný příkaz if

Příkaz `if` umožňuje vykonat určitou část programu pouze tehdy, pokud je splněna zadaná podmínka.

Základní zápis:

```python
if podminka:
    prikaz
```

Podmínka se vyhodnotí jako pravdivá (`True`) nebo nepravdivá (`False`).

Pokud je pravdivá, vykoná se odsazený blok příkazů. Pokud je nepravdivá, program tento blok přeskočí a pokračuje za ním.

### Příklad – Kontrola věku

```python
vek = 20

if vek >= 18:
    print("Jsi plnoletý")

print("Konec programu")
```

Výstup:

```text
Jsi plnoletý
Konec programu
```

Pokud změníme hodnotu proměnné `vek` na `15`, první výpis se neprovede.

Program však stále vypíše `Konec programu`, protože tento příkaz není součástí podmíněného bloku.

### Podmínka jako logický výraz

Za `if` zapisujeme výraz, jehož výsledek Python vyhodnotí jako pravdivý nebo nepravdivý.

```python
vek = 16

print(vek >= 18)  # False

if vek >= 18:
    print("Přístup povolen")
```

Porovnávací a logické operátory jsme probírali v lekci [04 – Operátory a výrazy](../04-operatory_a_vyrazy/).

## 2. Odsazování bloků

Python používá **odsazování k určení bloků kódu**.

Na rozdíl od některých jiných programovacích jazyků nepoužívá pro vymezení bloků složené závorky.

```python
vek = 20

if vek >= 18:
    print("Jsi plnoletý")
    print("Můžeš pokračovat")

print("Tento příkaz je mimo podmínku")
```

Oba odsazené příkazy patří do bloku `if`.

Poslední příkaz již odsazený není, a proto se vykoná bez ohledu na výsledek podmínky.

### Pravidla zápisu

- Za podmínkou musí následovat dvojtečka `:`.
- Příkazy uvnitř bloku musí být odsazené.
- Na stejné úrovni bloku musí mít příkazy stejné odsazení.
- Doporučené odsazení v Pythonu jsou **4 mezery**.

Nesprávné odsazení může způsobit chybu `IndentationError`.

```python
# Nesprávný zápis
if vek >= 18:
print("Jsi plnoletý")
```

Tento zápis způsobí `IndentationError`, protože příkaz uvnitř bloku není odsazený.

Odsazování není pouze otázkou vzhledu kódu. Přímo ovlivňuje jeho fungování.

## 3. Jednoduché větvení

Jednoduché větvení umožňuje programu rozhodnout, zda vykoná určitou část kódu.

Rozlišujeme neúplné a úplné větvení.

### Neúplné větvení – if

Používáme jej, pokud chceme provést určité příkazy pouze při splnění podmínky.

```python
vek = 20

if vek >= 18:
    print("Jsi plnoletý")
```

Pokud podmínka není splněna, program odsazený blok přeskočí.

### Úplné větvení – if, else

Úplné větvení nabízí dvě možnosti. Program vykoná právě jednu z nich.

```python
vek = 16

if vek >= 18:
    print("Jsi plnoletý")
else:
    print("Nejsi plnoletý")
```

Větev `else` se vykoná pouze v případě, že podmínka `if` není splněna.

### Příklad – Sudé a liché číslo

```python
cislo = int(input("Zadej celé číslo: "))

if cislo % 2 == 0:
    print("Číslo je sudé")
else:
    print("Číslo je liché")
```

Operátor `%` vrací zbytek po dělení.

Pokud je zbytek po dělení dvěma roven nule, číslo je sudé.

## 4. Vícenásobné větvení

Pokud potřebujeme rozhodovat mezi více možnostmi, používáme `elif`.

Příkaz `elif` představuje další podmínku, která se kontroluje pouze tehdy, pokud předchozí podmínky nebyly splněny.

```python
znamka = int(input("Zadej známku: "))

if znamka == 1:
    print("Výborný")
elif znamka == 2:
    print("Chvalitebný")
elif znamka == 3:
    print("Dobrý")
elif znamka == 4:
    print("Dostatečný")
elif znamka == 5:
    print("Nedostatečný")
else:
    print("Neplatná známka")
```

Python vyhodnocuje jednotlivé podmínky postupně shora dolů.

Jakmile narazí na první pravdivou podmínku, vykoná odpovídající blok a ostatní větve přeskočí.

### Pořadí podmínek

Na pořadí podmínek záleží.

```python
body = 95

if body >= 50:
    print("Splněno")
elif body >= 90:
    print("Výborný výsledek")
```

Přestože má student 95 bodů, program vypíše pouze `Splněno`.

První podmínka je totiž pravdivá, takže druhá se již nevyhodnotí.

Správné pořadí:

```python
if body >= 90:
    print("Výborný výsledek")
elif body >= 50:
    print("Splněno")
else:
    print("Nesplněno")
```

### Rozdíl mezi několika if a elif

Následující dva zápisy nejsou vždy ekvivalentní.

**Samostatné podmínky:**

```python
cislo = 15

if cislo > 0:
    print("Kladné číslo")

if cislo > 10:
    print("Číslo je větší než 10")
```

Výstup:

```text
Kladné číslo
Číslo je větší než 10
```

Obě podmínky se vyhodnocují nezávisle.

**Vícenásobné větvení:**

```python
cislo = 15

if cislo > 0:
    print("Kladné číslo")
elif cislo > 10:
    print("Číslo je větší než 10")
```

Výstup:

```text
Kladné číslo
```

Jakmile je splněna první podmínka, další větve se již nekontrolují.

To je jeden z nejdůležitějších rozdílů mezi samostatnými podmínkami a vícenásobným větvením.

## 5. Složené podmínky

Složená podmínka vzniká kombinováním více jednoduchých podmínek pomocí logických operátorů.

| Operátor | Význam |
|---|---|
| `and` | Oba propojené výrazy musí být pravdivé |
| `or` | Alespoň jeden z propojených výrazů musí být pravdivý |
| `not` | Neguje pravdivostní hodnotu výrazu |

### Operátor and

```python
vek = 20
ma_vstupenku = True

if vek >= 18 and ma_vstupenku:
    print("Vstup povolen")
else:
    print("Vstup zamítnut")
```

Vstup je povolen pouze tehdy, pokud je uživatel plnoletý a zároveň má vstupenku.

### Operátor or

```python
je_student = True
je_senior = False

if je_student or je_senior:
    print("Nárok na slevu")
else:
    print("Bez slevy")
```

Stačí splnit jednu z podmínek.

### Operátor not

```python
ma_zakaz = False

if not ma_zakaz:
    print("Přístup povolen")
```

### Kombinování více operátorů

```python
vek = 17
ma_souhlas = True
ma_zakaz = False

if (vek >= 18 or ma_souhlas) and not ma_zakaz:
    print("Přístup povolen")
else:
    print("Přístup zamítnut")
```

Program povolí přístup, pokud je uživatel plnoletý nebo má souhlas a zároveň nemá zákaz.

Závorky pomáhají určit pořadí vyhodnocování a zvyšují čitelnost složených podmínek.

## 6. Vnořené podmínky

Vnořená podmínka je podmíněný příkaz umístěný uvnitř jiného podmíněného bloku.

Používáme ji tehdy, pokud další rozhodování závisí na výsledku předchozí podmínky.

```python
vek = int(input("Zadej svůj věk: "))
ma_vstupenku = input("Máš vstupenku? (ano/ne): ")

if vek >= 18:
    if ma_vstupenku == "ano":
        print("Vstup povolen")
    else:
        print("Nemáš vstupenku")
else:
    print("Nesplňuješ věkovou podmínku")
```

Program nejprve ověřuje věk.

Pouze pokud je uživatel plnoletý, pokračuje kontrolou vstupenky.

### Složená vs. vnořená podmínka

Stejný požadavek lze někdy vyjádřit složenou i vnořenou podmínkou.

**Složená podmínka:**

```python
if vek >= 18 and ma_vstupenku == "ano":
    print("Vstup povolen")
```

**Vnořená podmínka:**

```python
if vek >= 18:
    if ma_vstupenku == "ano":
        print("Vstup povolen")
```

V obou případech se zpráva vypíše pouze tehdy, pokud jsou splněny obě podmínky.

Rozdíl spočívá především ve struktuře programu:

- **Složená podmínka** spojuje několik logických výrazů do jednoho rozhodnutí.
- **Vnořená podmínka** provádí další rozhodování uvnitř již vybrané větve.

Vnořování je vhodné především tehdy, pokud jednotlivé větve obsahují další příkazy nebo potřebujeme rozlišovat více důvodů, proč podmínka nebyla splněna.

### Přehled podmínek a větvení

| Konstrukce | Charakteristika |
|---|---|
| Jednoduchá podmínka | Jeden logický výraz |
| Složená podmínka | Více výrazů propojených logickými operátory |
| Neúplné větvení | `if` bez `else` |
| Úplné větvení | `if` a `else` |
| Vícenásobné větvení | `if`, `elif`, případně `else` |
| Vnořené podmínky | Podmíněný příkaz uvnitř jiného podmíněného bloku |

Složené podmínky a vnořené podmínky nejsou totéž. Složená podmínka kombinuje více logických výrazů, zatímco vnořená podmínka představuje další rozhodování uvnitř již vybrané větve.

## 7. Pravdivostní hodnoty a podmínky

Výraz za `if` nemusí mít přímo datový typ `bool`.

Python dokáže vyhodnotit pravdivost také u jiných datových typů.

Například:

```python
cislo = 5

if cislo:
    print("Číslo je nenulové")
```

U čísel platí, že nula je nepravdivá a nenulová hodnota je pravdivá.

Podobně se vyhodnocují řetězce:

```python
jmeno = "Petr"

if jmeno:
    print("Jméno bylo zadáno")
```

Prázdný řetězec `""` je nepravdivý, zatímco neprázdný řetězec je pravdivý.

| Hodnota | Pravdivost |
|---|---|
| `0` | `False` |
| `10` | `True` |
| `""` | `False` |
| `"Python"` | `True` |
| `False` | `False` |
| `True` | `True` |

### Příklad – Kontrola zadaného jména

```python
jmeno = input("Zadej své jméno: ")

if jmeno:
    print(f"Ahoj, {jmeno}")
else:
    print("Nezadal jsi žádné jméno")
```

Tento příklad ověřuje, zda řetězec není prázdný.

V dalších částech kurzu se naučíme vstupy kontrolovat podrobněji.

## 8. Časté chyby při práci s podmínkami

### Záměna = a ==

Operátor `=` slouží k přiřazení hodnoty.

Operátor `==` slouží k porovnání hodnot.

```python
vek = 18

if vek == 18:
    print("Je ti 18 let")
```

Následující zápis je chybný:

```python
if vek = 18:
    print("Je ti 18 let")
```

Tento zápis způsobí `SyntaxError`. V podmínce používáme pro porovnání hodnot operátor `==`.

### Nesprávné odsazení

```python
if vek >= 18:
print("Plnoletý")
```

Tento zápis způsobí `IndentationError`, protože příkaz uvnitř bloku není odsazený.

### Nesprávné pořadí podmínek

```python
vek = 20

if vek >= 15:
    print("Alespoň 15 let")
elif vek >= 18:
    print("Plnoletý")
```

Druhá větev se pro hodnotu `20` nikdy nevykoná.

### Nesprávný zápis více porovnání

```python
vek = 20

# Nesprávná logika
if vek == 18 or 20:
    print("Podmínka splněna")
```

Výraz `20` je sám o sobě pravdivý, takže je celá podmínka vždy splněna.

Správný zápis:

```python
if vek == 18 or vek == 20:
    print("Podmínka splněna")
```

Python nabízí i další způsoby zápisu, které poznáme při práci s datovými strukturami.

## 9. Kompletní příklad – Hodnocení výsledku testu

Program načte počet získaných bodů a podle výsledku vypíše hodnocení.

```python
body = int(input("Zadej počet bodů (0–100): "))

if body < 0 or body > 100:
    print("Neplatný počet bodů")
elif body >= 90:
    print("Výborný výsledek")
elif body >= 75:
    print("Velmi dobrý výsledek")
elif body >= 50:
    print("Test splněn")
else:
    print("Test nesplněn")
```

Program nejprve zkontroluje, zda je počet bodů v povoleném rozsahu.

Pokud je hodnota platná, postupně vyhodnocuje jednotlivé hranice.

Příklad spuštění:

```text
Zadej počet bodů (0–100): 82
Velmi dobrý výsledek
```

Při návrhu podobných programů je důležité ověřovat také hraniční hodnoty, například `49`, `50`, `74`, `75`, `89` a `90`.

## 10. Ověření znalostí

1. Jaký je rozdíl mezi sekvencí a větvením programu?
2. K čemu slouží příkaz `if`?
3. Jaký je rozdíl mezi neúplným a úplným větvením?
4. Kdy použijeme `elif`?
5. Proč je v Pythonu důležité odsazování?
6. Jaký je rozdíl mezi několika samostatnými příkazy `if` a konstrukcí `if/elif`?
7. Proč může pořadí podmínek ovlivnit výsledek programu?
8. Jaký je rozdíl mezi operátory `=` a `==`?
9. Co je složená podmínka?
10. Co je vnořená podmínka?
11. Jaký je rozdíl mezi složenou a vnořenou podmínkou?
12. Jak Python vyhodnocuje číslo `0` a prázdný řetězec `""`?
13. Proč je podmínka `vek == 18 or 20` nesprávně zapsaná?
14. Proč je při testování podmínek důležité ověřovat hraniční hodnoty?

---

**Předchozí lekce:** [Vstup a výstup](../05-vstup_a_vystup/)

**Další lekce:** [Cyklus while](../07-cyklus_while/)