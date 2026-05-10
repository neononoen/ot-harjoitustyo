# Lankavarasto, ot-harjoitustyö
Sovelluksen tarkoitus on toimia digitaalisena neulelankojen varastona, jonne käyttäjä pystyy lisäämään lankoja sekä hakea varastossa jo olevia lankoja.

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/neononoen/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/neononoen/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/neononoen/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/neononoen/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

[Käyttöohje](https://github.com/neononoen/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)

[Testaus](https://github.com/neononoen/ot-harjoitustyo/blob/main/dokumentaatio/testaus.md)

## Releaset

[Viikko 5](https://github.com/neononoen/ot-harjoitustyo/releases/tag/viikko5)

[Viikko 6](https://github.com/neononoen/ot-harjoitustyo/releases/tag/viikko6)

[Loppupalautus](https://github.com/neononoen/ot-harjoitustyo/releases/tag/loppupalautus)

## Sovelluksen asennus

1. Riippuvuuksien asentaminen

```bash
poetry install
```

2. Tietokannan alustus

```bash
poetry run invoke build
```

3. Sovelluksen käynnistäminen

```bash
poetry run invoke start
```

## Sovelluksen käynnistäminen

Sovelluksen voi käynnistää komennolla

```bash
poetry run invoke start
```

## Testaus

Sovelluksen testit voi suorittaa komennolla

```bash
poetry run invoke test
```

## Testikattavuus

Testikattavuusraportin saa komennolla

```bash
poetry run invoke coverage-report
```

## Pylint

Pylint-tarkistuksen voi suorittaa komennolla

```bash
poetry run invoke lint
```