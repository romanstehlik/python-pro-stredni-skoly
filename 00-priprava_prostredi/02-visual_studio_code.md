# Visual Studio Code

## 1. Co je Visual Studio Code?

**Visual Studio Code (VS Code)** je bezplatný editor zdrojového kódu vyvíjený společností Microsoft.

Umožňuje vytvářet, upravovat a spravovat zdrojové soubory v různých programovacích jazycích. Jeho možnosti lze rozšiřovat pomocí doplňků označovaných jako **Extensions**.

Pro programování v Pythonu budeme používat tři základní součásti:

| Nástroj | Funkce |
|---|---|
| Python | Interpreter, který vykonává programy |
| Visual Studio Code | Editor pro psaní a úpravu zdrojového kódu |
| Rozšíření Python | Podpora jazyka Python ve VS Code |

VS Code samotný Python programy nevykonává. Ke spuštění využívá nainstalovaný interpreter Pythonu.

## 2. Instalace VS Code

Visual Studio Code je dostupný pro Windows, Linux a macOS.

1. Otevřete [code.visualstudio.com](https://code.visualstudio.com/).
2. Stáhněte verzi odpovídající operačnímu systému.
3. Dokončete instalaci podle pokynů.
4. Otevřete Visual Studio Code.

### Rozšíření Python

Pro práci s Pythonem nainstalujeme příslušné rozšíření.

1. Otevřete panel **Extensions** pomocí klávesové zkratky `Ctrl+Shift+X`.
2. Do vyhledávání zadejte `Python`.
3. Vyberte rozšíření **Python** od Microsoftu.
4. Klikněte na **Install**.

Na macOS použijte zkratku `Cmd+Shift+X`.

Rozšíření poskytuje podporu Pythonu, například práci s interpretem a diagnostiku chyb.

## 3. Pracovní prostředí VS Code

Prostředí VS Code se skládá z několika základních částí:

| Část | Funkce |
|---|---|
| Explorer | Zobrazení a správa souborů projektu |
| Editor | Psaní a úprava zdrojového kódu |
| Terminal | Spouštění programů a příkazů |
| Extensions | Správa nainstalovaných rozšíření |
| Problems | Přehled nalezených problémů v kódu |

### Práce s projektem

Programy je vhodné organizovat do samostatných adresářů.

Ve VS Code lze celý adresář otevřít pomocí **File → Open Folder**.

Díky tomu jsou dostupné všechny soubory projektu a integrovaný terminál se zpravidla otevře v odpovídajícím pracovním adresáři.

## 4. Výběr interpretru

Pokud je v počítači nainstalováno více verzí Pythonu, je potřeba určit, kterou má VS Code používat.

1. Otevřete nabídku příkazů pomocí `Ctrl+Shift+P`.
2. Vyhledejte **Python: Select Interpreter**.
3. Vyberte požadovanou instalaci Pythonu 3.

Na macOS se nabídka příkazů otevírá pomocí `Cmd+Shift+P`.

Vybraný interpreter se používá při spouštění a dalších funkcích rozšíření Python.

**Poznámka:** Výběr interpretru ve VS Code nemusí změnit verzi Pythonu dostupnou prostřednictvím příkazu `python` v běžném terminálu.

## 5. Nastavení editoru

VS Code obsahuje funkce usnadňující psaní zdrojového kódu, například automatické doplňování, zobrazování návrhů a integrovanou nápovědu.

Pro začátečníky doporučujeme automatické doplňování omezit, aby si nejprve osvojili základní syntaxi Pythonu.

Zachováme však zvýrazňování syntaxe, upozornění na chyby a automatické uzavírání závorek a uvozovek.

### Úprava settings.json

1. Otevřete nabídku příkazů pomocí `Ctrl+Shift+P`.
2. Vyhledejte **Preferences: Open User Settings (JSON)**.
3. Do konfiguračního souboru přidejte následující nastavení.

```jsonc
{
    // Automatické doplňování
    "editor.quickSuggestions": false,               // Automatické návrhy při psaní
    "editor.suggestOnTriggerCharacters": false,     // Návrhy vyvolané speciálními znaky
    "editor.inlineSuggest.enabled": false,          // Návrhy přímo v řádku
    "editor.wordBasedSuggestions": "off",           // Návrhy slov z otevřených souborů
    "editor.tabCompletion": "off",                  // Doplňování pomocí klávesy Tab
    "editor.snippetSuggestions": "none",            // Návrhy připravených úryvků kódu

    // Automatické uzavírání
    "editor.autoClosingBrackets": "always",         // Automatické uzavírání závorek
    "editor.autoClosingQuotes": "always",           // Automatické uzavírání uvozovek

    // AI
    "chat.disableAIFeatures": true                  // Vypnutí vestavěných AI funkcí VS Code
}
```

Pokud soubor `settings.json` již obsahuje jiná nastavení, není potřeba je mazat. Nové položky stačí doplnit a správně oddělit čárkami.

Nastavení omezuje vybrané funkce editoru a vestavěnou AI asistenci. Samostatně nainstalovaná rozšíření třetích stran mohou vyžadovat vlastní konfiguraci.

Automatické doplňování lze později znovu povolit.

## 6. První Python soubor

Vytvoříme jednoduchý projekt, na kterém si vyzkoušíme práci s editorem.

1. Vytvořte adresář `prvni-program`.
2. Otevřete jej ve VS Code pomocí **File → Open Folder**.
3. V panelu Explorer vytvořte soubor `main.py`.
4. Zapište následující program:

```python
print("Hello World!")
```

5. Soubor uložte pomocí `Ctrl+S`.

Na macOS použijte `Cmd+S`.

Program lze spustit tlačítkem **Run Python File** v pravé horní části editoru.

Výstup:

```text
Hello World!
```

Výsledná struktura projektu:

```text
prvni-program/
└── main.py
```

Spouštění programů prostřednictvím terminálu bude vysvětleno v následující lekci.

---

**Další lekce:** [Práce s terminálem](./03-prace_s_terminalem.md)

**Dokumentace:** [Python ve VS Code](https://code.visualstudio.com/docs/python/python-tutorial)