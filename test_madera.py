import unittest

import madera


class TestCelulosas(unittest.TestCase):
    def test_celulosas_aserrin(self):
        self.assertEqual(madera.celulosas("aserrin", 2.4, 6.3, 2.8),
                         (42.336, 7620.48))

    def test_celulosas_astilla(self):
        self.assertEqual(madera.celulosas("astilla", 2.4, 6.3, 2.8),
                         (42.336, 10160.64))

    def test_celulosas_invalido(self):
        self.assertEqual(madera.celulosas("bombones", 0, 0, 0),
                         "Producto incorrecto")


class TestTroncos(unittest.TestCase):
    def test_troncos_no_pieces(self):
        self.assertEqual(madera.troncos(50, 2.44), 0.479)

    def test_troncos_two_pieces(self):
        self.assertEqual(madera.troncos(50, 2.44, 2), 0.958)


class TestAserrio(unittest.TestCase):
    def test_aserrio_1a(self):
        self.assertEqual(madera.aserrio(4, 0.75, 8, 1),
                         "4 x 0.75 x 8 1a, $30.0")

    def test_aserrio_2a(self):
        self.assertEqual(madera.aserrio(4, 0.75, 8, 2),
                         "4 x 0.75 x 8 2a, $24.0")

    def test_aserrio_3a(self):
        self.assertEqual(madera.aserrio(4, 0.75, 8, 3),
                         "4 x 0.75 x 8 3a, $20.0")


class TestRaja(unittest.TestCase):
    def test_raja_1_alto(self):
        self.assertEqual(madera.raja(2.4, 6.3, [2.3]),
                         (34.776, 7233.41))

    def test_raja_3_altos(self):
        self.assertEqual(madera.raja(2.4, 6.3, [2.3, 2.6, 2]),
                         (34.776, 7233.41))
