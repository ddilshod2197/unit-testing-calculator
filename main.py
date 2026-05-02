import unittest

class Calculator:
    def toq_son(self, son):
        return son % 2 != 0

    def juft_son(self, son):
        return son % 2 == 0

    def katta(self, son1, son2):
        return son1 > son2

    def kichik(self, son1, son2):
        return son1 < son2

    def teng(self, son1, son2):
        return son1 == son2

    def toq_sonlar_jadvali(self, n):
        return [i for i in range(1, n+1) if self.toq_son(i)]

    def juft_sonlar_jadvali(self, n):
        return [i for i in range(1, n+1) if self.juft_son(i)]

    def katta_sonlar_jadvali(self, n):
        return [i for i in range(1, n+1) if self.katta(i, 10)]

    def kichik_sonlar_jadvali(self, n):
        return [i for i in range(1, n+1) if self.kichik(i, 10)]

    def teng_sonlar_jadvali(self, n):
        return [i for i in range(1, n+1) if self.teng(i, 10)]

    def toq_sonlar_jadvali_10(self, n):
        return [i for i in range(1, n+1) if self.toq_son(i) and self.katta(i, 10)]

    def juft_sonlar_jadvali_10(self, n):
        return [i for i in range(1, n+1) if self.juft_son(i) and self.katta(i, 10)]

    def katta_sonlar_jadvali_10(self, n):
        return [i for i in range(1, n+1) if self.katta(i, 10)]

    def kichik_sonlar_jadvali_10(self, n):
        return [i for i in range(1, n+1) if self.kichik(i, 10)]

    def teng_sonlar_jadvali_10(self, n):
        return [i for i in range(1, n+1) if self.teng(i, 10)]

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_toq_son(self):
        self.assertTrue(self.calc.toq_son(5))
        self.assertFalse(self.calc.toq_son(4))

    def test_juft_son(self):
        self.assertTrue(self.calc.juft_son(4))
        self.assertFalse(self.calc.juft_son(5))

    def test_katta(self):
        self.assertTrue(self.calc.katta(10, 5))
        self.assertFalse(self.calc.katta(5, 10))

    def test_kichik(self):
        self.assertTrue(self.calc.kichik(5, 10))
        self.assertFalse(self.calc.kichik(10, 5))

    def test_teng(self):
        self.assertTrue(self.calc.teng(10, 10))
        self.assertFalse(self.calc.teng(10, 5))

    def test_toq_sonlar_jadvali(self):
        self.assertEqual(self.calc.toq_sonlar_jadvali(10), [1, 3, 5, 7, 9])

    def test_juft_sonlar_jadvali(self):
        self.assertEqual(self.calc.juft_sonlar_jadvali(10), [2, 4, 6, 8, 10])

    def test_katta_sonlar_jadvali(self):
        self.assertEqual(self.calc.katta_sonlar_jadvali(10), [10])

    def test_kichik_sonlar_jadvali(self):
        self.assertEqual(self.calc.kichik_sonlar_jadvali(10), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_teng_sonlar_jadvali(self):
        self.assertEqual(self.calc.teng_sonlar_jadvali(10), [10])

    def test_toq_sonlar_jadvali_10(self):
        self.assertEqual(self.calc.toq_sonlar_jadvali_10(10), [10])

    def test_juft_sonlar_jadvali_10(self):
        self.assertEqual(self.calc.juft_sonlar_jadvali_10(10), [])

    def test_katta_sonlar_jadvali_10(self):
        self.assertEqual(self.calc.katta_sonlar_jadvali_10(10), [10])

    def test_kichik_sonlar_jadvali_10(self):
        self.assertEqual(self.calc.kichik_sonlar_jadvali_10(10), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_teng_sonlar_jadvali_10(self):
        self.assertEqual(self.calc.teng_sonlar_jadvali_10(10), [10])

if __name__ == '__main__':
    unittest.main()
