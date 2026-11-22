# První program v Pythonu

V předchozí lekci jsme se seznámili s algoritmy a způsoby jejich zápisu. Nyní začneme algoritmy převádět do skutečného programovacího jazyka.

V této lekci vytvoříme první Python program, naučíme se vypisovat informace do terminálu a seznámíme se se základními pravidly zápisu zdrojového kódu.

## 1. Zdrojový kód a Python program

**Zdrojový kód** představuje zápis programu v určitém programovacím jazyce.

Python programy zpravidla zapisujeme do textových souborů s příponou `.py`.

Například:

```text
main.py
```

Soubor obsahuje příkazy, které interpreter Pythonu při spuštění zpracovává a vykonává.

### První program

Vytvořte ve VS Code nový soubor `main.py` a zapište:

```python
print("Hello World!")
```

Soubor uložte a spusťte prostřednictvím integrovaného terminálu:

```powershell
python main.py
```

Na Linuxu a macOS můžete použít příkaz `python3 main.py`.

Výstup programu:

```text
Hello World!
```

Právě jsme vytvořili a spustili jednoduchý Python program.

## 2. Vykonávání příkazů

Python při běžném sekvenčním vykonávání zpracovává příkazy postupně, od začátku programu.

Například:

```python
print("První řádek")
print("Druhý řádek")
print("Třetí řádek")
```

Výstup:

```text
První řádek
Druhý řádek
Třetí řádek
```

Jednotlivé příkazy se vykonávají v pořadí, ve kterém jsou zapsané.

Pokud jejich pořadí změníme, změní se také pořadí výstupu.

Později se naučíme používat podmínky, cykly a funkce, které umožňují běh programu řídit.

## 3. Funkce print()

**`print()`** je vestavěná funkce Pythonu, která slouží k výpisu hodnot na standardní výstup, obvykle do terminálu.

### Výpis textu

Text zapisujeme do uvozovek:

```python
print("Hello World!")
print("Učím se Python")
```

Výstup:

```text
Hello World!
Učím se Python
```

Každé volání `print()` standardně ukončí výpis novým řádkem.

### Výpis více hodnot

Funkci `print()` můžeme předat více hodnot oddělených čárkami.

```python
print("Python", "je", "programovací jazyk")
```

Výstup:

```text
Python je programovací jazyk
```

*Python mezi jednotlivé hodnoty standardně vloží mezeru.*

### Prázdný řádek

Pokud funkci `print()` zavoláme bez argumentů, vypíše prázdný řádek.

```python
print("První část")
print()
print("Druhá část")
```

Výstup:

```text
První část

Druhá část
```

### Výpis čísel

Funkce `print()` umožňuje vypisovat také čísla.

```python
print(15)
print(3.14)
```

Výstup:

```text
15
3.14
```

**Všimněte si rozdílu mezi zápisem čísla a textu. Text uzavíráme do uvozovek, samotné číslo nikoliv.**

Datovým typům se budeme podrobně věnovat v následující lekci.

## 4. Textové řetězce a uvozovky

Text v Pythonu označujeme jako **řetězec** (*string*).

Řetězce můžeme zapisovat pomocí dvojitých nebo jednoduchých uvozovek.

```python
print("Hello World!")
print('Hello World!')
```

Oba příkazy vypíšou stejný text.

Uvozovky musí být správně uzavřené a musí odpovídat jejich počátečnímu typu.

### Uvozovky uvnitř textu

Pokud chceme do textu zapsat jednoduchou uvozovku, můžeme celý řetězec uzavřít do dvojitých uvozovek.

```python
print("I'm learning Python")
```

Podobně můžeme použít jednoduché uvozovky, pokud text obsahuje dvojité.

```python
print('Řekl: "Ahoj!"')
```

Pokud potřebujeme použít stejný typ uvozovek uvnitř řetězce, můžeme jej zapsat pomocí zpětného lomítka `\`.

```python
print("Řekl: \"Ahoj!\"")
```

### Speciální znaky

V řetězcích můžeme používat také některé speciální zápisy.

| Zápis | Význam |
|---|---|
| `\n` | Nový řádek |
| `\t` | Tabulátor |
| `\"` | Dvojitá uvozovka |
| `\'` | Jednoduchá uvozovka |
| `\\` | Zpětné lomítko |

Příklad:

```python
print("První řádek\nDruhý řádek")
print("Jméno:\tPetr")
```

Výstup:

```text
První řádek
Druhý řádek
Jméno:  Petr
```

Přesné odsazení tabulátorem závisí na prostředí, ve kterém se text zobrazuje.

## 5. Komentáře

**Komentář** je část zdrojového kódu, kterou Python při vykonávání programu ignoruje.

Komentáře slouží především k vysvětlení účelu kódu a usnadňují jeho čtení.

### Jednořádkový komentář

Komentář začíná znakem `#`.

```python
# Toto je komentář
print("Ahoj")
```

Komentář se při spuštění nevykoná.

### Komentář za příkazem

Komentář můžeme umístit také za příkaz.

```python
print("Ahoj")  # Výpis pozdravu
```

### Zakomentování příkazu

Pomocí znaku `#` můžeme dočasně zabránit vykonání určitého příkazu.

```python
print("První řádek")
# print("Druhý řádek")
print("Třetí řádek")
```

Výstup:

```text
První řádek
Třetí řádek
```

### Víceřádkové komentáře

Python nemá samostatnou syntaxi pro víceřádkové komentáře.

Pokud chceme zapsat komentář přes několik řádků, použijeme znak `#` na začátku každého z nich.

```python
# Tento program vypisuje
# jednoduchý pozdrav
# do terminálu

print("Ahoj")
```

Komentáře by měly vysvětlovat důležité části programu. Není potřeba komentovat každý samozřejmý příkaz.

## 6. Základní pravidla zápisu

Každý programovací jazyk má pravidla, podle kterých musí být zdrojový kód zapsán.

Tato pravidla označujeme jako **syntaxi**.

Pokud je porušíme, Python nemusí být schopný program vykonat.

### Rozlišování velkých a malých písmen

Python rozlišuje velká a malá písmena (*case-sensitive*).

Správný zápis:

```python
print("Ahoj")
```

Nesprávný zápis:

```python
Print("Ahoj")
```

`Print` není totéž co `print`. V tomto případě Python ohlásí chybu `NameError`, protože nezná název `Print`.

### Závorky a uvozovky

Při volání funkce `print()` používáme kulaté závorky.

```python
print("Ahoj")
```

Nesprávně uzavřené závorky nebo uvozovky mohou způsobit syntaktickou chybu.

### Odsazování

V Pythonu má odsazování zvláštní význam. Slouží například k označení bloků kódu uvnitř podmínek, cyklů a funkcí.

Zatím zapisujeme jednoduché příkazy bez odsazení:

```python
print("Ahoj")
print("Python")
```

Podrobná pravidla odsazování si vysvětlíme při práci s podmínkami.

### Čitelnost kódu

Přestože Python některé způsoby formátování umožňuje, doporučujeme dodržovat jednotný a přehledný styl.

Například:

```python
print("První řádek")
print("Druhý řádek")
```

Jednotlivé příkazy zapisujeme zpravidla na samostatné řádky a mezi logicky souvisejícími částmi programu můžeme ponechávat prázdné řádky.

Pravidla a doporučení pro styl Python kódu jsou popsána v dokumentu [PEP 8](https://peps.python.org/pep-0008/).

## 7. První chyby v programu

*Chyby jsou běžnou součástí programování. Důležité je naučit se rozpoznat jejich příčinu.*

### SyntaxError

K syntaktické chybě dochází například tehdy, když nedodržíme pravidla zápisu programu.

```python
print("Ahoj)
```

Řetězec nemá uzavřené uvozovky.

Python ohlásí chybu `SyntaxError`.

### NameError

Chyba `NameError` vzniká například při použití názvu, který Python nezná.

```python
Print("Ahoj")
```

Python rozlišuje `Print` a `print`, a proto program skončí chybou.

### Čtení chybových hlášení

Při výskytu chyby Python zpravidla zobrazí:

- Soubor, ve kterém chyba nastala
- Číslo řádku souvisejícího s chybou
- Typ chyby
- Popis problému

Číslo řádku je důležitým vodítkem, ale skutečná příčina může být také na některém z předchozích řádků.

Při hledání chyby si nejprve pozorně přečtěte celé chybové hlášení.

Podrobněji se ladění programů budeme věnovat v samostatné lekci.

## 8. Ověření znalostí

1. Co je zdrojový kód a jakou příponu mají Python soubory?
2. V jakém pořadí se vykonávají příkazy jednoduchého Python programu?
3. K čemu slouží funkce `print()`?
4. Jaký je rozdíl mezi `print("15")` a `print(15)`?
5. Jak lze vytvořit prázdný řádek ve výstupu?
6. Jaké uvozovky můžeme používat při zápisu textových řetězců?
7. K čemu slouží komentáře?
8. Co znamená, že Python rozlišuje velká a malá písmena?
9. Proč je důležité dodržovat syntaxi a správné odsazování?
10. Jaký je rozdíl mezi chybami `SyntaxError` a `NameError`?

---

**Předchozí lekce:** [Algoritmy a algoritmické myšlení](../01-algoritmy/)

**Další lekce:** [Proměnné a datové typy](../03-promenne_a_datove_typy/)