# Projekt – Parkovací automat

## Zadání

Navrhněte algoritmus jednoduchého parkovacího automatu, který vypočítá cenu parkování a zpracuje platbu zákazníka.

Cílem je využít **sekvenci, větvení a opakování**. Program v Pythonu zatím nevytvářejte.

## Požadavky

Parkovací automat musí splňovat následující pravidla:

1. Zákazník zadá délku parkování v celých hodinách.
2. Jedna hodina parkování stojí **30 Kč**.
3. Automat vypočítá celkovou cenu.
4. Zákazník zadá vloženou částku.
5. Automat vyhodnotí platbu:

   - **Přesná částka:** Potvrdí zaplacení.
   - **Přeplatek:** Vypočítá a vrátí rozdíl.
   - **Nedoplatek:** Vypočítá chybějící částku a umožní její doplacení.

Při doplacení se nově vložená částka přičte k dosud zaplacené částce. Kontrola platby se opakuje, dokud zákazník nezaplatí dostatečnou částku.

Pokud zákazník zadá neplatnou délku parkování (nula nebo záporné číslo), automat musí požádat o nové zadání.

Předpokládejte zadávání celých čísel a kladných plateb.

## Vypracování

### 1. Analýza problému

Určete vstupy, zpracování a výstupy algoritmu.

### 2. Slovní zápis

Navrhněte postup algoritmu pomocí očíslovaných kroků.

### 3. Pseudokód

Převeďte navržený postup do pseudokódu. Použijte vhodné konstrukce pro rozhodování a opakování.

### 4. Vývojový diagram

Vytvořte vývojový diagram odpovídající pseudokódu.

### 5. Testování

Ověřte algoritmus alespoň na následujících případech:

| Délka parkování | Vložená částka | Očekávané chování |
|---:|---:|---|
| 2 hodiny | 60 Kč | Potvrzení platby |
| 3 hodiny | 100 Kč | Vrácení 10 Kč |
| 1 hodina | 20 Kč | Požadavek na doplacení 10 Kč |
| 0 hodin | — | Odmítnutí neplatné délky |

U nedostatečné platby ověřte také situaci, kdy zákazník doplácí ve více krocích.

## Výstup projektu

Řešení zpracujte do vlastních souborů:

- `projekt.txt` – analýza, slovní zápis, pseudokód a testování
- `diagram.png` nebo `diagram.pdf` – vývojový diagram

**Kritéria úspěšného řešení:**

- Algoritmus splňuje všechny požadavky
- Jednotlivé kroky jsou jednoznačné
- Výpočty a rozhodování jsou správné
- Algoritmus správně využívá opakování
- Pseudokód odpovídá vývojovému diagramu

---

**Studijní materiál:** [Algoritmy a algoritmické myšlení](./README.md)

**Cvičení:** [Cvičení](./cviceni.md)

**Další lekce:** [První program](../02-prvni_program/)