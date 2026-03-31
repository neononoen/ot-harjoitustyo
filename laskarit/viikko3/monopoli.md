```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Pelaaja "1" -- "*" Raha
    Ruutu "1" -- "1" Ruututyyppi
    Ruututyyppi -- Aloitusruutu
    Ruututyyppi -- Vankila
    Ruututyyppi -- SattumaJaYhteismaa
    Ruututyyppi -- AsematJaLaitokset
    Ruututyyppi -- Katu
    class Katu{
        nimi
    }
    Pelaaja "1" -- "*" Katu
    Katu "1" -- "0..4" Talo
    Katu "1" -- 0, 1" Hotelli
    Ruutu "1" -- "1" Toiminto
    SattumaJaYhteismaa "1" -- "1" Kortti
    Kortti "1" -- "1" Toiminto
    Monopolipeli "1" -- "1" Aloitusruutu
    Monopolipeli "1" -- "1" Vankila
```