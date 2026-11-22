# Operátory a výrazy

V předchozí lekci jsme se naučili používat proměnné a základní datové typy. Nyní se zaměříme na operace, které můžeme s hodnotami provádět.

Operátory umožňují provádět matematické výpočty, porovnávat hodnoty a vytvářet logické výrazy.

## 1. Operátory a výrazy

**Operátor** je symbol nebo klíčové slovo, které určuje operaci prováděnou nad hodnotami.

Například:

```python
10 + 5
```

Operátor `+` provádí sčítání hodnot `10` a `5`.

Hodnoty, nad kterými se operace provádí, označujeme jako **operandy**.

**Výraz** je část programu, kterou Python vyhodnotí a získá její výslednou hodnotu.

```python
10 + 5
```

Výsledkem tohoto výrazu je hodnota `15`.

Výrazy můžeme používat při přiřazování:

```python
soucet = 10 + 5
print(soucet)
```

Výstup:

```text
15
```

Výraz se nejprve vyhodnotí a následně se jeho výsledek přiřadí k názvu proměnné.

## 2. Aritmetické operátory

**Aritmetické operátory** slouží k provádění matematických výpočtů.

| Operátor | Význam | Příklad | Výsledek |
|:---:|---|---|---|
| `+` | Sčítání | `10 + 5` | `15` |
| `-` | Odčítání | `10 - 5` | `5` |
| `*` | Násobení | `10 * 5` | `50` |
| `/` | Dělení | `10 / 5` | `2.0` |
| `//` | Celočíselné dělení | `10 // 3` | `3` |
| `%` | Zbytek po dělení | `10 % 3` | `1` |
| `**` | Umocňování | `2 ** 3` | `8` |

### Základní výpočty

Operátory můžeme používat přímo s hodnotami nebo s proměnnými.

```python
cena = 250
pocet = 3

celkova_cena = cena * pocet

print(celkova_cena)
```

Výstup:

```text
750
```

### Dělení

V Pythonu rozlišujeme několik operací souvisejících s dělením.

**Běžné dělení `/`**

```python
print(10 / 2)
```

Výstup:

```text
5.0
```

Běžné dělení vrací hodnotu typu `float`, i když je výsledek matematicky celé číslo.

**Celočíselné dělení `//`**

```python
print(10 // 3)
```

Výstup:

```text
3
```

Operátor `//` provádí dělení se zaokrouhlením výsledku dolů.

U záporných čísel proto nemusí být výsledek stejný jako prosté odstranění desetinné části.

```python
print(-10 // 3)  # -4
```

**Zbytek po dělení `%`**

```python
print(10 % 3)
```

Výstup:

```text
1
```

Operátor `%` se často používá například při zjišťování, zda je celé číslo sudé.

```python
print(8 % 2)  # 0
print(9 % 2)  # 1
```

Celé číslo je sudé, pokud je jeho zbytek po dělení dvěma roven nule.

### Umocňování

Pro umocňování používáme operátor `**`.

```python
print(2 ** 3)  # 8
print(5 ** 2)  # 25
```

První příklad představuje třetí mocninu čísla 2, druhý druhou mocninu čísla 5.

### Operátory a textové řetězce

Některé operátory můžeme používat také s textovými řetězci.

Operátor `+` spojuje řetězce:

```python
print("Hello" + "World")
```

Výstup:

```text
HelloWorld
```

Operátor `*` umožňuje opakovat řetězec určitý početkrát:

```python
print("Ahoj" * 3)
```

Výstup:

```text
AhojAhojAhoj
```

Stejný operátor tedy může mít u různých datových typů odlišné chování.

## 3. Priorita operátorů

Pokud výraz obsahuje více operátorů, Python je vyhodnocuje podle jejich **priority**.

Například:

```python
print(10 + 5 * 2)
```

Výstup:

```text
20
```

Násobení má vyšší prioritu než sčítání, proto se provede jako první.

### Základní pořadí operací

| Priorita | Operace |
|:---:|---|
| 1 | Závorky `()` |
| 2 | Umocňování `**` |
| 3 | Násobení a dělení `*`, `/`, `//`, `%` |
| 4 | Sčítání a odčítání `+`, `-` |

Tabulka představuje zjednodušený přehled běžných aritmetických výrazů. U výrazů se znaménkem záleží také na přesném zápisu.

Operátory se stejnou prioritou se většinou vyhodnocují zleva doprava. *Výjimkou je například umocňování, které se při řetězení vyhodnocuje zprava doleva.*

### Použití závorek

Závorkami můžeme změnit pořadí vyhodnocování.

```python
print(10 + 5 * 2)    # 20
print((10 + 5) * 2)  # 30
```

Závorky doporučujeme používat také tehdy, když díky nim bude výraz přehlednější.

## 4. Přiřazovací operátory

Pro přiřazení hodnoty používáme operátor `=`.

```python
skore = 10
```

Python umožňuje používat také **složené přiřazovací operátory**, které kombinují výpočet s přiřazením.

Například:

```python
skore = skore + 5
```

Můžeme zapsat zkráceně:

```python
skore += 5
```

Oba zápisy v tomto případě zvýší skóre o 5.

### Přehled přiřazovacích operátorů

| Operátor | Příklad | Odpovídající výpočet |
|:---:|---|---|
| `+=` | `x += 5` | `x = x + 5` |
| `-=` | `x -= 5` | `x = x - 5` |
| `*=` | `x *= 5` | `x = x * 5` |
| `/=` | `x /= 5` | `x = x / 5` |
| `//=` | `x //= 5` | `x = x // 5` |
| `%=` | `x %= 5` | `x = x % 5` |
| `**=` | `x **= 2` | `x = x ** 2` |

Příklad:

```python
skore = 100

skore += 50
skore -= 20

print(skore)
```

Výstup:

```text
130
```

Složené přiřazovací operátory zjednodušují zápis při opakované úpravě hodnot proměnných.

## 5. Porovnávací operátory

**Porovnávací operátory** slouží k porovnávání hodnot.

Výsledkem porovnání je pravdivostní hodnota typu `bool`, tedy `True` nebo `False`.

| Operátor | Význam | Příklad | Výsledek |
|:---:|---|---|---|
| `==` | Rovná se | `5 == 5` | `True` |
| `!=` | Nerovná se | `5 != 3` | `True` |
| `>` | Větší než | `5 > 3` | `True` |
| `<` | Menší než | `5 < 3` | `False` |
| `>=` | Větší nebo rovno | `5 >= 5` | `True` |
| `<=` | Menší nebo rovno | `5 <= 3` | `False` |

### Porovnávání hodnot

```python
a = 10
b = 5

print(a > b)
print(a == b)
print(a != b)
```

Výstup:

```text
True
False
True
```

### Přiřazení a porovnání

Je důležité rozlišovat operátory `=` a `==`.

**Přiřazení hodnoty:**

```python
x = 10
```

Operátor `=` přiřazuje hodnotu k názvu proměnné.

**Porovnání hodnot:**

```python
print(x == 10)
```

Výstup:

```text
True
```

Operátor `==` porovnává dvě hodnoty a vrací výsledek typu `bool`.

Tyto operátory nelze zaměňovat.

### Porovnávání různých datových typů

Při porovnávání musíme zohlednit datové typy hodnot.

```python
print(15 == "15")
```

Výstup:

```text
False
```

Číslo `15` a textový řetězec `"15"` představují hodnoty různých typů.

Některá porovnání různých typů nejsou povolena:

```python
print(15 > "10")
```

Tento příkaz způsobí chybu `TypeError`.

## 6. Logické operátory

**Logické operátory** umožňují kombinovat několik podmínek a pracovat s pravdivostními hodnotami.

V Pythonu používáme tři základní logické operátory:

| Operátor | Význam |
|---|---|
| `and` | Logické A |
| `or` | Logické NEBO |
| `not` | Logická negace |

### Operátor and

Výraz s operátorem `and` je pravdivý pouze tehdy, když jsou obě podmínky pravdivé.

```python
vek = 20
ma_prukaz = True

print(vek >= 18 and ma_prukaz)
```

Výstup:

```text
True
```

### Operátor or

Výraz s operátorem `or` je pravdivý, pokud je pravdivá alespoň jedna z podmínek.

```python
je_vikend = False
je_svatek = True

print(je_vikend or je_svatek)
```

Výstup:

```text
True
```

### Operátor not

Operátor `not` obrací pravdivostní hodnotu výrazu.

```python
je_vikend = False

print(not je_vikend)
```

Výstup:

```text
True
```

### Pravdivostní tabulky

| A | B | `A and B` | `A or B` | `not A`
|---|---|---|---|---|
| `False` | `False` | `False` | `False` | `True`
| `False` | `True` | `False` | `True` | `True`
| `True` | `False` | `False` | `True` | `False`
| `True` | `True` | `True` | `True` | `False`

### Kombinování podmínek

```python
vek = 16

print(vek >= 15 and vek < 18)
```

Výstup:

```text
True
```

Výraz ověřuje, zda je hodnota `vek` alespoň 15 a zároveň menší než 18.

Logické operátory budeme využívat především při práci s podmínkami.

### Zkrácené vyhodnocování

Python při používání operátorů `and` a `or` nemusí vždy vyhodnotit všechny části výrazu.

Například:

```python
print(False and 10 / 0 == 5)
```

Výstup:

```text
False
```

Python již z první hodnoty ví, že celý výraz s operátorem `and` nemůže být pravdivý.

Proto druhou část výrazu nevyhodnotí a nedojde k dělení nulou.

Tento princip označujeme jako **zkrácené vyhodnocování** (*short-circuit evaluation*).

*Při práci s pravdivostními hodnotami `True` a `False` vracejí operátory `and` a `or` také pravdivostní hodnoty. Při použití jiných datových typů však mohou vracet přímo některý z operandů.*

## 7. Kombinování operátorů

V jednom výrazu můžeme kombinovat různé druhy operátorů.

Například:

```python
vek = 17
ma_souhlas = True

print(vek >= 18 or ma_souhlas)
```

Výstup:

```text
True
```

Nejprve se vyhodnotí porovnání `vek >= 18`. Potom se jeho výsledek zkombinuje s hodnotou `ma_souhlas` pomocí operátoru `or`.

### Priorita logických operátorů

Logické operátory mají následující pořadí:

1. `not`
2. `and`
3. `or`

Porovnávací operátory mají vyšší prioritu než uvedené logické operátory.

**Přehlednost můžeme zvýšit použitím závorek.**

```python
a = True
b = False
c = False

print(a or b and c)      # True
print((a or b) and c)    # False
```

V prvním případě se nejprve vyhodnotí `b and c`, protože `and` má vyšší prioritu než `or`.

Ve druhém případě závorky způsobí, že se nejprve vyhodnotí `a or b`.

Závorky tedy mohou změnit výsledek logického výrazu.

## 8. Časté chyby

### Záměna = a ==

Přiřazovací operátor `=` a porovnávací operátor `==` mají odlišný význam.

```python
x = 10          # Přiřazení hodnoty
print(x == 10)  # Porovnání hodnot
```

Přiřazení mění hodnotu dostupnou pod názvem proměnné, zatímco porovnání vrací `True` nebo `False`.

### Dělení nulou

```python
print(10 / 0)
```

Dělení nulou způsobí chybu `ZeroDivisionError`.

### Nesprávné datové typy

```python
print(10 + "5")
```

Sčítání čísla a textového řetězce tímto způsobem způsobí chybu `TypeError`.

### Nesprávné pořadí operací

```python
print(10 + 5 * 2)
```

Výsledkem je `20`, nikoliv `30`.

Pokud chceme nejprve provést sčítání, použijeme závorky:

```python
print((10 + 5) * 2)
```

Výstup:

```text
30
```

## 9. Ověření znalostí

1. Co je operátor, operand a výraz?
2. Jaký je rozdíl mezi operátory `/`, `//` a `%`?
3. K čemu slouží operátor `**`?
4. Jak Python určuje pořadí matematických operací?
5. Co znamená zápis `x += 5`?
6. Jaký je rozdíl mezi `=` a `==`?
7. Jaký datový typ je výsledkem porovnávání?
8. Jak fungují operátory `and`, `or` a `not`?
9. Co znamená zkrácené vyhodnocování logických výrazů?
10. Proč mohou závorky změnit výsledek logického výrazu?
11. Jaké chyby mohou vzniknout při používání operátorů?

---

**Předchozí lekce:** [Proměnné a datové typy](../03-promenne_a_datove_typy/)

**Další lekce:** [Vstup a výstup](../05-vstup_a_vystup/)