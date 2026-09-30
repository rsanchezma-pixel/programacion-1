import unittest

def sumar(a, b):
    return a + b

class PruebaSuma(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)

unittest.main()