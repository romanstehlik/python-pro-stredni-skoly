# Úvod do Pythonu a instalace

## 1. Co je Python?

**Python** je vysokoúrovňový, univerzální programovací jazyk, který se vyznačuje přehlednou syntaxí a důrazem na čitelnost zdrojového kódu.

Používá se v mnoha oblastech informačních technologií, například při:

- Vývoji desktopových a webových aplikací
- Automatizaci opakujících se úloh
- Analýze a zpracování dat
- Strojovém učení a umělé inteligenci
- Tvorbě skriptů a systémových nástrojů

### Základní vlastnosti Pythonu

| Vlastnost | Význam |
|---|---|
| Vysokoúrovňový jazyk | Umožňuje zapisovat programy pomocí konstrukcí blízkých lidskému způsobu uvažování |
| Univerzální jazyk | Lze jej používat pro různé druhy aplikací |
| Interpretovaný jazyk | Programy se běžně spouštějí prostřednictvím interpretu |
| Dynamicky typovaný jazyk | Datové typy hodnot se kontrolují při běhu programu |
| Multiparadigmatický jazyk | Podporuje více způsobů programování |

S jednotlivými vlastnostmi se podrobněji seznámíme v dalších částech kurzu.

## 2. Jak Python funguje?

Programy v Pythonu se zapisují do textových souborů s příponou `.py`.

Tyto soubory obsahují **zdrojový kód**, tedy příkazy zapsané podle pravidel programovacího jazyka.

Pro spuštění programu potřebujeme **interpreter Pythonu**, který zdrojový kód zpracovává a vykonává.

Například soubor `main.py` může obsahovat:

```python
print("Hello World!")
```

Po spuštění program vypíše:

```text
Hello World!
```

Python zpravidla vykonává jednotlivé příkazy v pořadí, v jakém jsou v programu uvedeny. Toto pořadí lze později měnit pomocí podmínek, cyklů a dalších programových konstrukcí.

Při běžném používání Pythonu není nutné před každým spuštěním samostatně překládat celý program do spustitelného souboru.

## 3. Instalace Pythonu

Python je dostupný pro Windows, Linux i macOS.

### Windows

1. Otevřete [python.org/downloads](https://www.python.org/downloads/).
2. Stáhněte aktuální stabilní verzi Pythonu 3 pro Windows.
3. Spusťte instalační soubor a dokončete instalaci podle pokynů.
4. Otevřete nové okno PowerShellu.

Funkčnost instalace ověřte příkazem:

```powershell
python --version
```

Příklad výstupu:

```text
Python 3.x.y
```

Čísla označují nainstalovanou verzi Pythonu.

### Linux

Na řadě linuxových distribucí je Python 3 již nainstalovaný.

Dostupnost ověříte příkazem:

```bash
python3 --version
```

Pokud Python není nainstalovaný, můžete jej získat prostřednictvím správce balíčků své distribuce.

Například na Ubuntu a Debianu:

```bash
sudo apt update
sudo apt install python3
```

### macOS

1. Otevřete [python.org/downloads](https://www.python.org/downloads/).
2. Stáhněte aktuální stabilní verzi Pythonu 3 pro macOS.
3. Dokončete instalaci podle pokynů.
4. Otevřete aplikaci Terminal.

Funkčnost instalace ověřte:

```bash
python3 --version
```

## 4. Časté problémy

### Příkaz python není rozpoznán

Pokud PowerShell nerozpozná příkaz `python`, může být příčinou nesprávná instalace nebo konfigurace systémové proměnné `PATH`.

**PATH** je proměnná prostředí obsahující seznam adresářů, ve kterých operační systém hledá spustitelné programy.

Po instalaci Pythonu může být potřeba terminál zavřít a znovu otevřít.

Pokud příkaz stále nefunguje, zkontrolujte instalaci Pythonu a jeho dostupnost v systémové proměnné `PATH`.

### Spouští se jiná verze Pythonu

V počítači může být nainstalováno více verzí Pythonu.

Ve Windows lze zkontrolovat dostupná umístění:

```powershell
where.exe python
```

Operační systém může najít více instalací. Pro správné spouštění programů je důležité vědět, který interpreter používáme.

## 5. Ověření znalostí

1. Co je Python a v jakých oblastech se používá?
2. Jaký je rozdíl mezi zdrojovým kódem a interpreterem?
3. Co znamená přípona `.py`?
4. Jak lze ověřit nainstalovanou verzi Pythonu?
5. K čemu slouží systémová proměnná `PATH`?

---

**Další lekce:** [Visual Studio Code](./02-visual_studio_code.md)

**Dokumentace:** [Oficiální dokumentace Pythonu](https://docs.python.org/3/)