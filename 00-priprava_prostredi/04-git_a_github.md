# Git a GitHub

## 1. Co je Git?

**Git** je distribuovaný verzovací systém, který umožňuje sledovat změny v souborech projektu.

Při programování jej používáme především k:

- Uchovávání historie změn
- Návratu ke starším verzím souborů
- Sdílení a synchronizaci projektů
- Spolupráci více vývojářů

Git umožňuje zaznamenat stav projektu v určitém okamžiku. Takový záznam označujeme jako **commit**.

### Git a GitHub

Git a GitHub nejsou totéž.

| Nástroj | Význam |
|---|---|
| Git | Verzovací systém pracující s historií souborů |
| GitHub | Online služba pro ukládání a správu Git repozitářů |

Git lze používat i bez GitHubu a připojení k internetu.

GitHub umožňuje ukládat vzdálené kopie projektů a sdílet je s dalšími uživateli.

## 2. Instalace Gitu

Git je dostupný pro Windows, Linux i macOS.

### Windows

1. Otevřete [git-scm.com/downloads](https://git-scm.com/downloads).
2. Stáhněte instalační soubor pro Windows.
3. Dokončete instalaci podle pokynů.
4. Otevřete nové okno PowerShellu.

Instalaci ověřte:

```powershell
git --version
```

### Linux

Na Ubuntu a Debianu lze Git nainstalovat příkazy:

```bash
sudo apt update
sudo apt install git
```

Instalaci ověřte:

```bash
git --version
```

### macOS

Git lze získat například prostřednictvím vývojářských nástrojů Apple.

V terminálu spusťte:

```bash
xcode-select --install
```

Po dokončení instalace ověřte:

```bash
git --version
```

## 3. Nastavení uživatele

Git ke commitům zaznamenává jméno a e-mail autora.

Před prvním použitím nastavíme základní identifikační údaje:

```powershell
git config --global user.name "Jmeno Prijmeni"
git config --global user.email "email@example.com"
```

Uvedené hodnoty nahraďte vlastními údaji.

Nastavení ověříte příkazy:

```powershell
git config --global user.name
git config --global user.email
```

Parametr `--global` znamená, že nastavení platí pro všechny repozitáře daného uživatelského účtu v počítači.

Pokud chceme nastavení změnit pouze pro konkrétní repozitář, použijeme příkazy bez parametru `--global`.

**Soukromí:** E-mail použitý v commitech může být viditelný v jejich historii. GitHub umožňuje používat také soukromou adresu typu `noreply`.

Více informací: [Nastavení soukromí e-mailové adresy na GitHubu](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

## 4. Co je repozitář?

**Repozitář** je projekt spravovaný verzovacím systémem Git.

Obsahuje soubory projektu a informace o jejich historii.

Rozlišujeme:

| Typ | Význam |
|---|---|
| Lokální repozitář | Kopie projektu uložená v počítači |
| Vzdálený repozitář | Kopie projektu uložená na serveru, například GitHubu |

Změny nejprve zaznamenáváme do lokálního repozitáře. Následně je můžeme odeslat do vzdáleného repozitáře.

## 5. Vytvoření repozitáře na GitHubu

Pro práci s GitHubem potřebujeme vlastní uživatelský účet.

Pokud účet ještě nemáte, vytvořte jej na [github.com](https://github.com/) a dokončete požadované ověření.

Následně vytvoříme první repozitář:

1. Přihlaste se na GitHub.
2. Zvolte **New repository**.
3. Zadejte název `python-projekty`.
4. Nastavte viditelnost **Private**.
5. Zaškrtněte vytvoření souboru `README.md`.
6. Vyberte šablonu `.gitignore` pro **Python**.
7. Potvrďte vytvoření repozitáře.

Soukromý repozitář není veřejně přístupný. Přístup k němu lze udělit vybraným uživatelům.

## 6. Klonování repozitáře

Pro stažení existujícího Git repozitáře do počítače slouží příkaz `git clone`.

Na stránce repozitáře na GitHubu otevřete nabídku **Code** a zkopírujte adresu HTTPS.

Adresa bude mít podobný tvar:

```text
https://github.com/UZIVATEL/python-projekty.git
```

V terminálu přejděte do adresáře, ve kterém chcete projekt uložit.

Spusťte:

```powershell
git clone https://github.com/UZIVATEL/python-projekty.git
```

Část `UZIVATEL` nahraďte svým uživatelským jménem nebo použijte zkopírovanou adresu.

Příkaz vytvoří nový adresář `python-projekty` s obsahem repozitáře.

**Pozor:** V cílovém umístění nesmí již existovat neprázdný adresář se stejným názvem.

Přejděte do vytvořeného adresáře:

```powershell
cd python-projekty
```

Ověřte stav repozitáře:

```powershell
git status
```

Pokud je vše v pořádku, Git oznámí, že pracovní adresář neobsahuje nezaznamenané změny.

Projekt následně otevřete ve VS Code pomocí **File → Open Folder**.

## 7. Práce se změnami

Git rozlišuje několik stavů souborů.

| Stav | Význam |
|---|---|
| Working directory | Aktuální soubory projektu |
| Staging area | Změny připravené pro další commit |
| Repository | Historie již zaznamenaných commitů |

### Přidání prvního programu

Do repozitáře `python-projekty` zkopírujte soubor `main.py`, který jste vytvořili v lekci [Visual Studio Code](./02-visual_studio_code.md).

Výsledná struktura projektu:

```text
python-projekty/
├── .gitignore
├── README.md
└── main.py
```

Git nyní rozpozná nový soubor, který zatím není součástí historie repozitáře.

### Zjištění stavu

Příkaz:

```powershell
git status
```

zobrazí informace o změněných, nových a připravených souborech.

### Zobrazení změn

Příkaz:

```powershell
git diff
```

zobrazí dosud nepřipravené změny ve sledovaných souborech.

### Připravení změn

Konkrétní soubor připravíme příkazem:

```powershell
git add main.py
```

Všechny změny v aktuálním adresáři a jeho podadresářích lze připravit příkazem:

```powershell
git add .
```

Před zaznamenáním změn je vhodné pomocí `git status` zkontrolovat, které soubory budou součástí commitu.

### Vytvoření commitu

Připravené změny zaznamenáme příkazem:

```powershell
git commit -m "Pridani prvniho programu"
```

**Commit** představuje uložený stav změn projektu v historii Gitu.

Parametr `-m` umožňuje zadat stručnou zprávu popisující provedenou změnu.

## 8. Synchronizace s GitHubem

### Odeslání změn

Commity vytvořené v počítači odešleme do vzdáleného repozitáře příkazem:

```powershell
git push
```

### Stažení změn

Pro stažení a začlenění nových změn ze vzdáleného repozitáře použijeme:

```powershell
git pull
```

Při běžné práci s jedním projektem na více počítačích je vhodné před zahájením úprav stáhnout aktuální změny.

### Historie commitů

Historii projektu zobrazíme příkazem:

```powershell
git log --oneline
```

Každý řádek představuje jeden commit.

## 9. Soubor .gitignore

Soubor `.gitignore` určuje soubory a adresáře, které Git nemá nově zahrnovat do sledování.

V Python projektech se používá například pro:

- Dočasné soubory
- Mezipaměť Pythonu
- Virtuální prostředí
- Lokální konfigurační soubory

V repozitáři jsme již při jeho vytváření zvolili šablonu `.gitignore` pro Python.

Je důležité vědět, že `.gitignore` automaticky neodstraní z historie soubory, které už Git sleduje.

### Bezpečnost

Do repozitáře neukládejte hesla, přístupové tokeny, soukromé klíče ani jiné citlivé údaje.

Soubor `.gitignore` pomáhá vynechávat vybrané soubory, ale není náhradou za bezpečné zacházení s přihlašovacími údaji.

Zvláště na sdíleném počítači dbejte na to, pod jakým účtem jste přihlášeni k GitHubu.

## 10. Časté problémy

| Problém | Možná příčina |
|---|---|
| `git` není rozpoznán | Git není nainstalovaný nebo není dostupný v `PATH` |
| `not a git repository` | Terminál se nenachází uvnitř Git repozitáře |
| `nothing to commit` | Git nemá žádné připravené změny k zaznamenání |
| `Authentication failed` | Problém s ověřením účtu GitHub |
| `failed to push some refs` | Vzdálený repozitář obsahuje změny, které nejsou v lokální kopii |

Při chybě je vhodné přečíst celé chybové hlášení. Často přímo popisuje příčinu problému.

Při práci s GitHubem prostřednictvím HTTPS lze použít přihlašování pomocí správce přihlašovacích údajů Gitu.

## 11. Ověření znalostí

1. Jaký je rozdíl mezi Gitem a GitHubem?
2. Co je repozitář?
3. Jaký je rozdíl mezi lokálním a vzdáleným repozitářem?
4. K čemu slouží commit?
5. Jaký je rozdíl mezi `git add` a `git commit`?
6. Jaký je rozdíl mezi `git push` a `git pull`?
7. K čemu slouží soubor `.gitignore`?

## 12. Přehled základních příkazů Gitu

| Příkaz | Význam |
|---|---|
| `git --version` | Zobrazí nainstalovanou verzi Gitu |
| `git config --global user.name "Jmeno"` | Nastaví jméno autora |
| `git config --global user.email "email"` | Nastaví e-mail autora |
| `git init` | Vytvoří nový lokální Git repozitář v aktuálním adresáři |
| `git clone URL` | Vytvoří lokální kopii vzdáleného repozitáře |
| `git status` | Zobrazí stav pracovního adresáře |
| `git diff` | Zobrazí nepřipravené změny sledovaných souborů |
| `git add soubor` | Připraví konkrétní soubor |
| `git add .` | Připraví změny v aktuálním adresáři a jeho podadresářích |
| `git commit -m "Zprava"` | Vytvoří commit |
| `git push` | Odešle commity do vzdáleného repozitáře |
| `git pull` | Stáhne a začlení vzdálené změny |
| `git log --oneline` | Zobrazí stručnou historii commitů |
| `git remote -v` | Zobrazí nastavené vzdálené repozitáře |

### Běžný pracovní postup

Před zahájením práce:

```powershell
git pull
```

Po dokončení úprav:

```powershell
git status
git add .
git commit -m "Popis zmen"
git push
```

Tento postup budeme používat také v dalších částech kurzu.

---

**Další lekce:** [Ověření prostředí](./05-overeni_prostredi.md)

**Dokumentace:** [Git](https://git-scm.com/doc) | [GitHub Docs](https://docs.github.com/)