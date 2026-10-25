import unittest

from numeroromano import converte


class TestNumeroRomano(unittest.TestCase):
    def test_I(self):
        self.assertEqual(converte('I'), 1)

    def test_V(self):
        self.assertEqual(converte('V'), 5)

    def test_II(self):
        self.assertEqual(converte('II'), 2)

    def test_XXII(self):
        self.assertEqual(converte('XXII'), 22)

    def test_IX(self):
        self.assertEqual(converte('IX'), 9)

    def test_XXIV(self):
        self.assertEqual(converte('XXIV'), 24)

    def test_demais_simbolos(self):
        for romano, inteiro in [('X', 10), ('L', 50), ('C', 100),
                                ('D', 500), ('M', 1000)]:
            with self.subTest(romano=romano):
                self.assertEqual(converte(romano), inteiro)

    def test_demais_subtracoes(self):
        for romano, inteiro in [('IV', 4), ('XL', 40), ('XC', 90),
                                ('CD', 400), ('CM', 900)]:
            with self.subTest(romano=romano):
                self.assertEqual(converte(romano), inteiro)

    def test_numeros_compostos(self):
        for romano, inteiro in [('XV', 15), ('XXVIII', 28),
                                ('MCMXCIV', 1994), ('MMMCMXCIX', 3999)]:
            with self.subTest(romano=romano):
                self.assertEqual(converte(romano), inteiro)


if __name__ == '__main__':
    unittest.main()
