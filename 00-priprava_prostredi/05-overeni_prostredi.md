# Ověření vývojového prostředí

Tato část slouží k praktickému ověření znalostí získaných během přípravy vývojového prostředí.

Cílem je samostatně vytvořit, spustit a verzovat jednoduchý Python program.

## 1. Ověření instalace

V terminálu ověřte dostupnost Pythonu:

```powershell
python --version
```

Následně ověřte instalaci Gitu:

```powershell
git --version
```

Oba příkazy by měly zobrazit verzi příslušného nástroje.

Na Linuxu a macOS použijte pro ověření Pythonu příkaz `python3 --version`.

## 2. Otevření projektu

Otevřete soukromý GitHub repozitář `python-projekty`, který jste vytvořili v předchozí lekci.

Pokud jej ještě nemáte uložený v počítači, naklonujte jej pomocí příkazu `git clone`.

Pokud již lokální kopii máte, otevřete její adresář ve Visual Studio Code.

Ve VS Code otevřete integrovaný terminál a ověřte, že se nacházíte v adresáři repozitáře:

```powershell
git status
```

Git by měl zobrazit informace o aktuálním stavu projektu.

## 3. Vytvoření programu

V kořenovém adresáři repozitáře vytvořte nový soubor:

```text
overeni.py
```

Zapište následující program:

```python
print("Hello World!")
print("Vývojové prostředí je připraveno.")
```

Soubor uložte a spusťte prostřednictvím integrovaného terminálu VS Code:

```powershell
python overeni.py
```

Očekávaný výstup:

```text
Hello World!
Vývojové prostředí je připraveno.
```

Na Linuxu a macOS použijte příkaz `python3 overeni.py`.

## 4. Verzování projektu

Pomocí Gitu zkontrolujte stav projektu:

```powershell
git status
```

Připravte soubor `overeni.py` k zaznamenání:

```powershell
git add overeni.py
```

Vytvořte commit:

```powershell
git commit -m "Overeni prostredi"
```

Odešlete změny na GitHub:

```powershell
git push
```

Na GitHubu ověřte, že repozitář obsahuje soubor `overeni.py` a vytvořený commit.

## 5. Úprava programu

Upravte soubor `overeni.py` tak, aby vypisoval další řádek s libovolným textem.

Program znovu spusťte a ověřte výstup.

Následně:

1. Zobrazte změny pomocí `git diff`.
2. Připravte upravený soubor pomocí `git add`.
3. Vytvořte druhý commit s výstižnou zprávou.
4. Odešlete změny na GitHub.
5. Zobrazte historii pomocí `git log --oneline`.

## 6. Kontrolní seznam

- Python je nainstalovaný a funkční.
- Git je nainstalovaný a funkční.
- VS Code používá správný interpreter Pythonu.
- Program lze spustit prostřednictvím terminálu.
- Na GitHubu je vytvořený soukromý repozitář.
- Repozitář obsahuje soubory `main.py` a `overeni.py`.
- V historii jsou alespoň dva vlastní commity.
- Změny jsou synchronizované s GitHubem.

Pokud jsou všechny body splněny, vývojové prostředí je připravené pro pokračování v kurzu.

---

**Pokračování:** [01 – Základy programování](../01-zaklady_programovani/)