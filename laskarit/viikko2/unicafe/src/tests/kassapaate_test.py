import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_rahamaara_oikein_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_lounaita_myyty_alussa_nolla(self):
        lounaita_myyty = self.kassapaate.edulliset + self.kassapaate.maukkaat

        self.assertEqual(lounaita_myyty, 0)
    
    # testit edullisen lounaan käteisostolle
    def test_rahamaara_kasvaa_edullisen_lounaan_kateisostossa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_vaihtoraha_edullisen_lounaan_kateisostossa_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(vaihtoraha, 60)

    def test_myytyjen_edullisten_lounaiden_maara_kasvaa_kateisostossa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_rahamaara_ei_kasva_edullisen_lounaan_ostossa_jos_maksu_ei_ole_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_vaihtoraha_edullisen_lounaan_kateisostossa_oikein_kun_maksu_ei_riittava(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(vaihtoraha, 200)
    
    def test_myytyjen_edullisten_lounaiden_maara_ei_kasva_kateisostossa(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
    
    #testit maukkaan lounaan käteisostolle
    def test_rahamaara_kasvaa_maukkaan_lounaan_kateisostossa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_vaihtoraha_maukkaan_lounaan_kateisostossa_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(vaihtoraha, 100)

    def test_myytyjen_maukkaiden_lounaiden_maara_kasvaa_kateisostossa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_rahamaara_ei_kasva_maukkaan_lounaan_ostossa_jos_maksu_ei_ole_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_vaihtoraha_maukkaan_lounaan_kateisostossa_oikein_kun_maksu_ei_riittava(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(vaihtoraha, 200)
    
    def test_myytyjen_maukkaiden_lounaiden_maara_ei_kasva_kateisostossa(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    # testit edullisen lounaan korttiostolle
    def test_edullisen_lounaan_korttiosto_onnistuu_jos_saldo_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_edullisen_lounaan_osto_veloitetaan_kortilta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 760)

    def test_myytyjen_edullisten_lounaiden_maara_kasvaa_korttiostossa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_edullisen_lounaan_korttiosto_ei_onnistu_jos_saldo_ei_riita(self):
        kortti = Maksukortti(200)

        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)
    
    def test_edullisen_lounaan_ostoa_ei_veloiteta_kortilta_jos_saldo_ei_riita(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(kortti.saldo, 200)
    
    def test_myytyjen_edullisten_lounaiden_maara_ei_kasva_korttiostossa(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kassan_rahamaara_ei_muutu_korttiostossa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    # testit maukkaan lounaan korttiostolle
    def test_maukkaan_lounaan_korttiosto_onnistuu_jos_saldo_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_maukkaan_lounaan_osto_veloitetaan_kortilta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 600)

    def test_myytyjen_maukkaiden_lounaiden_maara_kasvaa_korttiostossa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_maukkaan_lounaan_korttiosto_ei_onnistu_jos_saldo_ei_riita(self):
        kortti = Maksukortti(200)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
    
    def test_maukkaan_lounaan_ostoa_ei_veloiteta_kortilta_jos_saldo_ei_riita(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(kortti.saldo, 200)
    
    def test_myytyjen_maukkaiden_lounaiden_maara_ei_kasva_korttiostossa(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kassan_rahamaara_ei_muutu_korttiostossa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    # testit rahan lataamiselle
    def test_rahaa_ladattaessa_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)

        self.assertEqual(self.maksukortti.saldo, 1200)
    
    def test_rahaa_ladattaessa_kassan_rahamaara_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)
    
    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)

        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_kassan_rahamaara_ei_muutu_jos_summa_negatiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassan_rahamaara_nakyy_euroina(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)