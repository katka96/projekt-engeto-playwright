
# Projekt: Tři automatizované testy

## Popis projektu

Projekt testuje veřejně dostupné části českého webu Engeto.cz.

Testy jsou napsané v jazyce Python pomocí frameworku Playwright
a pluginu pytest-playwright.

## Testovací scénáře

1. Ověření načtení hlavní stránky.
2. Ověření otevření přehledu kurzů.
3. Ověření otevření detailu Python Akademie.

## Použité technologie

- Python
- Playwright
- pytest
- pytest-playwright

## Instalace

python -m venv .venv
\.venv\Scripts\python.exe -m pip install -r requirements.txt
\.venv\Scripts\python.exe -m playwright install chromium

## Spuštění testů

\.venv\Scripts\python.exe -m pytest

Spuštění s viditelným prohlížečem:

\.venv\Scripts\python.exe -m pytest --headed

## Očekávaný výsledek

3 passed

