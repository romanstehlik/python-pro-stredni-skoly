# Práce s terminálem

## 1. Co je terminál?

**Terminál** představuje textové rozhraní, prostřednictvím kterého lze zadávat příkazy operačnímu systému.

Při programování jej používáme především ke spouštění programů, práci se soubory a ovládání nástrojů, například Pythonu nebo Gitu.

Visual Studio Code obsahuje integrovaný terminál, který lze otevřít prostřednictvím nabídky **Terminal → New Terminal**.

Ve Windows budeme používat především prostředí **PowerShell**. Na Linuxu a macOS se běžně používají například Bash nebo Zsh.

## 2. Spouštění Python programů

Programy v Pythonu se obvykle ukládají do souborů s příponou `.py`.

V předchozí lekci jsme vytvořili soubor `main.py`:

```python
print("Hello World!")
```

Program lze spustit z integrovaného terminálu VS Code.

### Windows

```powershell
python main.py
```

### Linux a macOS

```bash
python3 main.py
```

Výstup:

```text
Hello World!
```

Příkaz spustí interpreter Pythonu a předá mu soubor `main.py` k vykonání.

Před spuštěním programu je důležité uložit provedené změny. Interpreter pracuje s obsahem souboru uloženým na disku.

## 3. Práce s adresáři

Terminál pracuje vždy v určitém umístění, které označujeme jako **aktuální pracovní adresář**.

Pokud spustíme příkaz:

```powershell
python main.py
```

Python se pokusí otevřít soubor `main.py` v aktuálním pracovním adresáři.

Pokud se soubor nachází v jiném adresáři, je potřeba do něj přejít nebo zadat správnou cestu.

### Základní příkazy

| Příkaz | Význam |
|---|---|
| `pwd` | Zobrazení aktuálního adresáře |
| `dir` | Výpis obsahu adresáře ve Windows |
| `ls` | Výpis obsahu adresáře na Linuxu a macOS |
| `cd nazev` | Přechod do určeného adresáře |
| `cd ..` | Přechod do nadřazeného adresáře |
| `mkdir nazev` | Vytvoření nového adresáře |
| `code .` | Otevření aktuálního adresáře ve VS Code |

### Vytváření souborů a adresářů

Pomocí terminálu můžeme vytvářet nové adresáře a soubory bez použití grafického rozhraní.

Následující příkazy jsou určené pro Windows PowerShell:

```powershell
mkdir pokus
cd pokus
New-Item main.py
code .
```

Jednotlivé příkazy postupně vytvoří adresář `pokus`, přejdou do něj, vytvoří prázdný soubor `main.py` a otevřou aktuální adresář ve VS Code.

Příkaz `code .` funguje pouze v případě, že je VS Code dostupný prostřednictvím systémové proměnné `PATH`.

### Praktický příklad

V předchozí lekci jsme vytvořili adresář `prvni-program`, který obsahuje `main.py`.

Nejprve zjistíme aktuální adresář:

```powershell
pwd
```

Potom zobrazíme dostupné soubory:

```powershell
dir
```

Pokud se již nacházíme v adresáři `prvni-program`, můžeme program rovnou spustit:

```powershell
python main.py
```

Pokud jsme v jeho nadřazeném adresáři, nejprve do něj přejdeme:

```powershell
cd prvni-program
python main.py
```

Příkaz `cd` mění aktuální pracovní adresář.

### Absolutní a relativní cesty

**Absolutní cesta** určuje úplné umístění souboru nebo adresáře.

Například:

```text
C:\Users\student\Documents\prvni-program
```

**Relativní cesta** určuje umístění vzhledem k aktuálnímu pracovnímu adresáři.

Například:

```text
prvni-program\main.py
```

Při práci s terminálem je proto důležité vědět, ve kterém adresáři se právě nacházíme.

## 4. Otevírání projektů ve VS Code

Adresář projektu lze otevřít několika způsoby:

- **File → Open Folder** – otevření adresáře prostřednictvím VS Code
- **Open with Code** – otevření adresáře z nabídky Průzkumníka souborů, pokud je tato možnost dostupná
- **`code .`** – otevření aktuálního adresáře prostřednictvím terminálu

Příkaz:

```powershell
code .
```

otevře aktuální adresář ve VS Code, pokud je příkaz `code` dostupný v prostředí systému.

Znalost tohoto příkazu není pro další části kurzu nezbytná.

## 5. Časté problémy

| Problém | Možná příčina |
|---|---|
| `python` není rozpoznán | Python není dostupný prostřednictvím příkazu `python` |
| `can't open file` | Soubor nebyl nalezen v zadaném umístění |
| Program vypisuje starý výsledek | Změny v souboru nebyly uloženy |
| `code` není rozpoznán | Příkaz VS Code není dostupný v systémové proměnné `PATH` |

Pokud Python nemůže najít soubor, nejprve ověřte aktuální adresář:

```powershell
pwd
```

Potom zobrazte jeho obsah:

```powershell
dir
```

Překontrolujte název souboru včetně přípony `.py`.

## 6. Procvičení

1. V projektu `prvni-program` vytvořte soubor `pozdrav.py`.
2. Napište program, který vypíše libovolný text.
3. Program spusťte prostřednictvím integrovaného terminálu.
4. Změňte vypisovaný text, soubor uložte a program spusťte znovu.
5. Pomocí příkazu `pwd` zjistěte aktuální pracovní adresář.
6. Zobrazte obsah adresáře a ověřte, že obsahuje vytvořený soubor.
7. Přejděte do nadřazeného adresáře pomocí `cd ..` a potom se vraťte zpět.

---

**Další lekce:** [Git a GitHub](./04-git_a_github.md)