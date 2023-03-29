import unittest
from Ej import Torres

class TestTorresDeHanoi(unittest.TestCase):
    def test_constructor(self):
        juego = Torres(3)
        self.assertEqual(juego.n, 3)
        self.assertEqual(juego.torre1, [3, 2, 1])
        self.assertEqual(juego.torre2, [])
        self.assertEqual(juego.torre3, [])
    
    def test_mover_disco(self):
        juego = Torres(3)
        juego.mover_disco(juego.torre1, juego.torre2)
        self.assertEqual(juego.torre1, [3, 2])
        self.assertEqual(juego.torre2, [1])
    
    def test_resolver(self):
        juego = Torres(3)
        juego.resolver()
        self.assertEqual(juego.torre1, [])
        self.assertEqual(juego.torre2, [])
        self.assertEqual(juego.torre3, [3, 2, 1])
    
if __name__ == '__main__':
    unittest.main()
