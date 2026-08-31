
"""Automatizované testy veřejné části webu Engeto.cz.

Projekt obsahuje tři nezávislé testovací scénáře vytvořené
pomocí frameworku Playwright a pluginu pytest-playwright.
"""

import re

from playwright.sync_api import Page, expect


HLAVNI_STRANKA = "https://engeto.cz/"
PREHLED_KURZU = "https://engeto.cz/prehled-kurzu/"


def zavrit_cookie_listu(page: Page) -> None:
    """Zavře cookie lištu, pokud se na stránce zobrazí."""
    tlacitko_cookies = page.get_by_role(
        "button",
        name="Souhlasím jen s nezbytnými",
    )

    if tlacitko_cookies.is_visible():
        tlacitko_cookies.click()


def otevrit_stranku(page: Page, url: str) -> None:
    """Otevře zadanou stránku a zavře případnou cookie lištu."""
    page.goto(url, wait_until="domcontentloaded")
    zavrit_cookie_listu(page)


def test_nacteni_hlavni_stranky(page: Page) -> None:
    """Test 1: Ověří správné načtení hlavní stránky Engeto."""

    # Arrange a Act – otevření testované stránky
    otevrit_stranku(page, HLAVNI_STRANKA)

    # Assert – kontrola adresy a hlavních prvků stránky
    expect(page).to_have_url(HLAVNI_STRANKA)

    expect(
        page.get_by_role(
            "heading",
            name="Získej náskok s tech & AI dovednostmi",
            exact=True,
        )
    ).to_be_visible()

    expect(
        page.get_by_role("link", name="Homepage")
    ).to_be_visible()


def test_otevreni_prehledu_kurzu(page: Page) -> None:
    """Test 2: Ověří navigaci z hlavní stránky do přehledu kurzů."""

    # Arrange – otevření hlavní stránky
    otevrit_stranku(page, HLAVNI_STRANKA)

    # Act – kliknutí na položku Kurzy v navigaci
    page.get_by_role(
        "link",
        name="Kurzy",
        exact=True,
    ).click()

    # Assert – kontrola adresy a nadpisu cílové stránky
    expect(page).to_have_url(
        re.compile(r"https://engeto\.cz/prehled-kurzu/?$")
    )

    expect(
        page.get_by_role(
            "heading",
            name="Kurzy programování, digitálních dovedností & AI",
            exact=True,
        )
    ).to_be_visible()


def test_otevreni_detailu_python_akademie(page: Page) -> None:
    """Test 3: Ověří otevření detailu Python Akademie."""

    # Arrange – otevření přehledu kurzů
    otevrit_stranku(page, PREHLED_KURZU)

    # Act – vyhledání a otevření karty Python Akademie
    hlavni_obsah = page.get_by_role("main")

    karta_pythonu = hlavni_obsah.get_by_role(
        "link",
        name=re.compile(r"^Python Akademie"),
    )

    expect(karta_pythonu).to_be_visible()
    karta_pythonu.click()

    # Assert – kontrola adresy a nadpisu detailu kurzu
    expect(page).to_have_url(
        re.compile(r"https://engeto\.cz/python-akademie/?$")
    )

    expect(
        page.get_by_role(
            "heading",
            name="Python Akademie",
            level=1,
            exact=True,
        )
    ).to_be_visible()

    expect(
        page.get_by_role(
            "link",
            name="Zobrazit termíny kurzu",
            exact=True,
        )
    ).to_be_visible()
