# Proměnné a datové typy

V předchozí lekci jsme se naučili vypisovat hodnoty pomocí funkce `print()`. Dosud jsme však pracovali především s hodnotami zapsanými přímo ve zdrojovém kódu.

V této lekci se naučíme ukládat hodnoty do proměnných, pracovat s nimi a rozlišovat základní datové typy.

## 1. Co je proměnná?

**Proměnná** je název, ke kterému můžeme přiřadit určitou hodnotu.

Proměnné umožňují uchovávat údaje a opakovaně je používat v programu.

Například:

```python
jmeno = "Petr"
vek = 15
```

Vytvořili jsme dvě proměnné:

- `jmeno` – obsahuje textovou hodnotu `"Petr"`
- `vek` – obsahuje číselnou hodnotu `15`

Pro přiřazení hodnoty používáme operátor `=`.

### Výpis hodnot proměnných

Hodnoty proměnných můžeme vypisovat pomocí funkce `print()`.

```python
jmeno = "Petr"
vek = 15

print(jmeno)
print(vek)
```

Výstup:

```text
Petr
15
```

Při použití názvu proměnné Python pracuje s hodnotou, která je k němu aktuálně přiřazena.

### Proměnná a text

Je důležité rozlišovat název proměnné a textový řetězec.

```python
jmeno = "Petr"

print(jmeno)
print("jmeno")
```

Výstup:

```text
Petr
jmeno
```

V prvním případě Python použije hodnotu proměnné `jmeno`.

Ve druhém případě vypíše text `"jmeno"`, protože je uzavřený v uvozovkách.

## 2. Přiřazování hodnot

Přiřazení zapisujeme pomocí operátoru `=`.

```python
skore = 10
```

Na levé straně je název proměnné, na pravé straně přiřazovaná hodnota.

Přiřazení není totéž co matematická rovnost (k tomu si řekneme víc později).

### Změna hodnoty proměnné

Ke stejnému názvu můžeme později přiřadit jinou hodnotu.

```python
skore = 10
print(skore)

skore = 20
print(skore)
```

Výstup:

```text
10
20
```

Při druhém přiřazení se název `skore` začne vztahovat k nové hodnotě.

### Použití předchozí hodnoty

Na pravé straně přiřazení můžeme použít dosavadní hodnotu proměnné.

```python
skore = 10
skore = skore + 5

print(skore)
```

Výstup:

```text
15
```

Python nejprve vyhodnotí pravou stranu:

```text
10 + 5 = 15
```

Teprve potom výsledek přiřadí k názvu `skore`.

Zápis:

```python
skore = skore + 5
```

tedy znamená, že se hodnota `skore` zvýší o 5.

### Přiřazení mezi proměnnými

Hodnotu jedné proměnné můžeme přiřadit také jiné proměnné.

```python
x = 10
y = x

print(x)
print(y)
```

Výstup:

```text
10
10
```

Uvažujme nyní následující program:

```python
x = 10
y = x

x = 20

print(x)
print(y)
```

Výstup:

```text
20
10
```

Při přiřazení `y = x` se k názvu `y` přiřadila aktuální hodnota `10`.

Pozdější změna přiřazení `x` proto hodnotu dostupnou pod názvem `y` neovlivní.

U složitějších datových typů se později setkáme i se situacemi, kdy dvě proměnné odkazují na stejný měnitelný objekt.

## 3. Pravidla pojmenovávání proměnných

Názvy proměnných musí dodržovat určitá pravidla.

### Povolené názvy

Název proměnné:

- Může obsahovat písmena, číslice a podtržítka
- Nesmí začínat číslicí
- Nesmí obsahovat mezery
- Nesmí být vyhrazeným slovem Pythonu
- Rozlišuje velká a malá písmena

Příklady správných názvů:

```python
jmeno = "Petr"
vek = 15
pocet_studentu = 24
cena_za_kus = 35
```

Příklady nesprávných názvů:

```python
1student = "Petr"
pocet studentu = 24
cena-za-kus = 35
if = 10
```
Všechny řádky způsobí chybu syntaxe.

### Velká a malá písmena

Python rozlišuje velká a malá písmena.

```python
vek = 15
Vek = 20

print(vek)
print(Vek)
```

Výstup:

```text
15
20
```

`vek` a `Vek` jsou dva různé názvy proměnných.

### Konvence snake_case

Podle doporučení [PEP 8](https://peps.python.org/pep-0008/) se pro názvy běžných proměnných používá konvence **snake_case**.

Víceslovné názvy zapisujeme malými písmeny a jednotlivá slova oddělujeme podtržítkem.

```python
cena_za_kus = 35
pocet_kusu = 6
celkova_cena = 210
```

Názvy by měly být výstižné a srozumitelné.

Například `pocet_studentu` lépe vyjadřuje význam uložené hodnoty než `x`.

Konvence nejsou totéž co pravidla syntaxe. Python například dovoluje název `pocetStudentu`, ale při běžném programování doporučujeme používat jednotný styl `snake_case`.

## 4. Co je datový typ?

**Datový typ** určuje druh hodnoty a operace, které s ní můžeme provádět.

Python rozlišuje například celá čísla, desetinná čísla, textové řetězce a pravdivostní hodnoty.

### Základní datové typy

| Datový typ | Označení | Příklad | Význam |
|---|---|---|---|
| Celé číslo | `int` | `15` | Celá čísla |
| Desetinné číslo | `float` | `15.5` | Čísla s plovoucí desetinnou čárkou |
| Textový řetězec | `str` | `"Python"` | Text |
| Pravdivostní hodnota | `bool` | `True` | Pravda nebo nepravda |

Příklad:

```python
vek = 15        # int (integer)             - celé číslo
vyska = 175.5   # float (floating-point)    - desetinné číslo
jmeno = "Petr"  # str (string)              - textový řetězec
student = True  # bool (boolean)            - pravdivostní hodnota
```
Každá z uvedených hodnot má jiný datový typ.

## 5. Celá čísla – int

Datový typ **`int`** představuje celá čísla.

```python
vek = 15
pocet_studentu = 24
teplota = -5
```
Celá čísla mohou být kladná, záporná nebo nulová.

```python
print(10)
print(-8)
print(0)
```

U celých čísel nepoužíváme desetinnou tečku.

## 6. Desetinná čísla – float

Datový typ **`float`** se používá pro čísla s plovoucí desetinnou čárkou.

```python
vyska = 175.5
cena = 29.90
teplota = -3.5
```

V Pythonu zapisujeme desetinnou část pomocí **tečky**, nikoliv čárky.

```python
print(3.14)
```

Hodnoty `15` a `15.0` mají různé datové typy, přestože matematicky představují stejné číslo.

```python
print(type(15))
print(type(15.0))
```

Výstup:

```text
<class 'int'>
<class 'float'>
```

Hodnoty typu `float` jsou v počítači ukládány s omezenou přesností. Proto některá desetinná čísla nemusí být reprezentována zcela přesně.

## 7. Textové řetězce – str

Datový typ **`str`** představuje textové řetězce.

Řetězce zapisujeme do jednoduchých nebo dvojitých uvozovek.

```python
jmeno = "Petr"
mesto = 'Havlíčkův Brod'
```

Textový řetězec může obsahovat také číslice.

```python
cislo = 15
text = "15"
```

Přestože hodnoty mohou při výpisu vypadat stejně, mají různé datové typy.

```python
print(type(cislo))
print(type(text))
```

Výstup:

```text
<class 'int'>
<class 'str'>
```

### Rozdíl mezi číslem a řetězcem

U čísel můžeme pomocí operátoru `+` provádět sčítání.

```python
print(10 + 5)
```

Výstup:

```python
15          # <class 'int'>
```

U řetězců operátor `+` spojuje jejich obsah.

```python
print("10" + "5")
```

Výstup:

```python
105         # <class 'str'>
```

Stejný operátor tedy může mít u různých datových typů odlišné chování.

Podrobněji se operátorům budeme věnovat v následující lekci.

## 8. Pravdivostní hodnoty – bool

Datový typ **`bool`** představuje pravdivostní hodnoty.

Může nabývat pouze dvou hodnot:

- `True` – pravda
- `False` – nepravda

Příklad:

```python
je_student = True
ma_ridicsky_prukaz = False

print(je_student)
print(ma_ridicsky_prukaz)
```

Výstup:

```text
True
False
```

Hodnoty `True` a `False` se zapisují s velkým počátečním písmenem a bez uvozovek.

Pokud je uzavřeme do uvozovek, vzniknou textové řetězce.

```python
print(type(True))
print(type("True"))
```

Výstup:

```text
<class 'bool'>
<class 'str'>
```

Pravdivostní hodnoty využijeme především při práci s podmínkami a logickými operátory.

## 9. Zjišťování datového typu

Pro zjištění datového typu hodnoty používáme vestavěnou funkci **`type()`**.

```python
vek = 15
jmeno = "Petr"

print(type(vek))
print(type(jmeno))
```

Výstup:

```text
<class 'int'>
<class 'str'>
```

Funkce `type()` vrací informaci o typu hodnoty. V uvedeném příkladu ji zobrazujeme pomocí `print()`.

Datový typ můžeme zjistit také přímo u konkrétní hodnoty:

```python
print(type(25))
print(type(3.14))
print(type("Python"))
print(type(False))
```
### Typové anotace

Python umožňuje u proměnných uvádět také **typové anotace** (*type hints*), které označují očekávaný datový typ.

```python
cislo: int = 15
vyska: float = 175.5
jmeno: str = "Petr"
student: bool = True
```

Typové anotace zlepšují čitelnost kódu a usnadňují jeho kontrolu. Jejich používání je dobrým zvykem zejména u rozsáhlejších programů.

**Důležité:** Python typové anotace při běžném vykonávání automaticky nevynucuje. Následující zápis je proto možný, přestože neodpovídá uvedenému typu:

```python
cislo: int = "patnáct"
```

Na nesoulad však mohou upozornit nástroje pro statickou kontrolu typů.

## 10. Dynamické typování

Python je **dynamicky typovaný programovací jazyk**.

To znamená, že datový typ je vlastností hodnoty a není potřeba jej předem deklarovat u názvu proměnné.

Například:

```python
udaj = 15
print(type(udaj))

udaj = "patnáct"
print(type(udaj))
```

Výstup:

```text
<class 'int'>
<class 'str'>
```

Nejprve se k názvu `udaj` přiřadí celé číslo, později textový řetězec.

Python umožňuje přiřadit ke stejnému názvu hodnoty různých datových typů.

To však neznamená, že lze libovolně kombinovat všechny typy hodnot.

Například:

```python
# print(10 + "5")
```

Pokus o sčítání čísla a textového řetězce tímto způsobem způsobí chybu `TypeError`.

Python nedokáže automaticky rozhodnout, zda chceme provést číselný výpočet, nebo spojit textové řetězce.

Převody mezi datovými typy se naučíme v lekci věnované vstupu a výstupu.

## 11. Časté chyby

### NameError

Chyba `NameError` může vzniknout při použití názvu proměnné, ke kterému nebyla přiřazena hodnota.

```python
print(sleva)
```
Pokud název `sleva` dosud neexistuje, Python ohlásí chybu.

### SyntaxError

Chyba `SyntaxError` vzniká při porušení pravidel zápisu Pythonu.

```python
1student = "Petr"
```

Název proměnné nesmí začínat číslicí.

### TypeError

Chyba `TypeError` může vzniknout při pokusu o provedení operace s nekompatibilními datovými typy.

```python
print(10 + "5")
```

V tomto případě nelze přímo sečíst celé číslo a textový řetězec.

**Při řešení chyb je důležité přečíst chybové hlášení a určit, na kterém řádku problém vznikl.**

## 12. Ověření znalostí

1. Co je proměnná a k čemu slouží?
2. Jaký je rozdíl mezi názvem proměnné a její hodnotou?
3. Co znamená operátor `=` při přiřazování?
4. Jaká pravidla musí splňovat názvy proměnných?
5. Co znamená konvence `snake_case`?
6. Jaký je rozdíl mezi datovými typy `int`, `float`, `str` a `bool`?
7. Jaký je rozdíl mezi hodnotami `15` a `"15"`?
8. K čemu slouží funkce `type()`?
9. Co znamená dynamické typování?
10. Proč příkaz `print(10 + "5")` způsobí chybu?

---

**Předchozí lekce:** [První program](../02-prvni_program/)

**Další lekce:** [Operátory a výrazy](../04-operatory_a_vyrazy/)