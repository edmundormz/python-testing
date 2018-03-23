import unittest
import madera


class TestMadera(unittest.TestCase):
    def test_celulosas(self):
        self.assertEqual(madera.celulosas("aserrin", 2.4, 6.3, 2.8), (42.336, 7620.48))
        self.assertEqual(madera.celulosas("astilla", 2.4, 6.3, 2.8), (42.336, 10160.64))
        self.assertEqual(madera.celulosas("bombones", 0, 0, 0), "Producto incorrecto")