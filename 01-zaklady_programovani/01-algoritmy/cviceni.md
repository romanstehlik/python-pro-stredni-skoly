# Cvičení – Algoritmy a algoritmické myšlení

Procvičte základní vlastnosti algoritmů, algoritmické konstrukce a návrh jednoduchých postupů.

**Pokyny:** Odpovědi zapisujte do vlastního souboru, například `cviceni.txt`. Vývojové diagramy vytvořte samostatně a uložte jako obrázek nebo PDF.

## Úkol 1 – Vstup, zpracování a výstup

U následujících problémů určete **vstupní údaje, zpracování a výstup**.

1. Výpočet obvodu obdélníku
2. Převod teploty ze °C na °F
3. Výpočet průměru čtyř známek

## Úkol 2 – Vlastnosti algoritmu

Posuďte následující postupy. U každého určete, zda splňuje základní vlastnosti algoritmu.

**A**
1. Zadej číslo.
2. Přičti k němu nějakou hodnotu.
3. Vypiš výsledek.

**B**
1. Nastav `x` na hodnotu 1.
2. Zvyš `x` o 1.
3. Vrať se ke kroku 2.

**C**
1. Zadej délky stran obdélníku.
2. Vynásob obě hodnoty.
3. Vypiš obsah obdélníku.

U nesprávně navržených postupů vysvětlete problém a navrhněte opravu.

## Úkol 3 – Algoritmické myšlení

**A – Dekompozice**

Rozdělte algoritmus pro výpočet celkové ceny jízdenek na jednotlivé kroky. Vstupem bude počet cestujících a cena jedné jízdenky.

**B – Abstrakce**

Určete, které údaje potřebujeme pro výpočet průměrné spotřeby automobilu v litrech na 100 km:

- Značka automobilu
- Ujetá vzdálenost
- Barva automobilu
- Spotřebované palivo
- Rok výroby

**C – Rozpoznávání vzorů**

Porovnejte postup pro výpočet obvodu čtverce, obvodu rovnostranného trojúhelníku a obvodu pravidelného pětiúhelníku. Určete společný princip a navrhněte obecný postup.

## Úkol 4 – Pseudokód

Navrhněte pseudokód pro následující algoritmy:

**A – Porovnání čísel**

Načtěte dvě čísla a vypište větší z nich. Pokud jsou stejná, vypište informaci o rovnosti.

**B – Výpis čísel**

Vypište všechna celá čísla od 1 do 10 pomocí opakování.

## Úkol 5 – Vývojové diagramy

Vytvořte vývojové diagramy následujících algoritmů:

**A – Sudé nebo liché číslo**

Načtěte celé číslo a rozhodněte, zda je sudé, nebo liché.

**B – Počítání do pěti**

Postupně vypište čísla od 1 do 5 pomocí cyklu.

Použijte odpovídající geometrické značky a označte rozhodovací větve.

## Úkol 6 – Ověřování algoritmů

**A – Ruční průchod**

Určete výstup následujícího algoritmu. Postupně zaznamenejte změny hodnoty `x`.

```text
x ← 5
x ← x + 3
x ← x * 2

VYPIŠ x
```

**B – Logická chyba**

Následující algoritmus má rozhodnout, zda student úspěšně absolvoval test. K úspěšnému absolvování potřebuje alespoň 50 bodů.

```text
NAČTI body

POKUD body > 50
    VYPIŠ "Úspěšně"
JINAK
    VYPIŠ "Neúspěšně"
```

1. Najděte případnou logickou chybu.
2. Navrhněte opravu.
3. Ověřte správnost pomocí alespoň tří testovacích hodnot.

---

**Studijní materiál:** [Algoritmy a algoritmické myšlení](./README.md)

**Samostatný projekt:** [Parkovací automat](./projekt.md)

**Další lekce:** [První program](../02-prvni_program/)