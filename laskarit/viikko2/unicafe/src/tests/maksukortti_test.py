import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_lataa_rahaa_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 15.0)

    def test_saldo_vahenee_oikein_jos_rahaa_tarpeeksi(self):
        self.assertEqual(self.maksukortti.ota_rahaa(200), True)

    def test_saldo_ei_vahene_jos_rahaa_ei_tarpeeksi(self):
        self.assertEqual(self.maksukortti.ota_rahaa(2000), False)

    def test_kortin_saldo_pyoristetaan_oikein(self):
        kortti = Maksukortti(100.9)

        self.assertEqual(str(kortti), "Kortilla on rahaa 1.01 euroa")