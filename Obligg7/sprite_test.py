import unittest
from random import *

from Obligg7.sprite import Sprite


class TestSprite(unittest.TestCase):

    def test_bredde_hoyde_negative_value(self):
        for _ in range(1000):
            with self.assertRaises(ValueError):
                value = randint(-100, -1)
                _ = Sprite(0, 0, value, value)

    def test_bredde_hoyde_positive_value(self):
        for _ in range(1000):
            value = randint(0, 100)
            _ = Sprite(0, 0, value, value)

    def test_x_start_y_start_any_value(self):
        for _ in range(1000):
            value = gauss(-1000, 1000)
            tmp = Sprite(value, value, 0, 0)
            self.assertEqual(value, tmp.x_start)
            self.assertEqual(value, tmp.y_start)

    def test_x_start_y_start_must_be_number(self):
        with self.assertRaises(ValueError):
            _ = Sprite("ValueError tekst 1", "ValueError tekst 2", 0, 0)

    def test_areal(self):
        for _ in range(1000):
            bredde = randint(0, 100)
            hoyde = randint(0, 100)
            temp = Sprite(0, 0, bredde, hoyde)
            self.assertEqual(bredde * hoyde, temp.areal())

    def test_er_inni_x_og_y_koordinat(self):
        for _ in range(10):
            x_start = randint(-1000, 1000)
            y_start = randint(-1000, 1000)
            temp = Sprite(x_start, y_start, 100, 100)

            # is inside
            for _ in range(1000):
                x_koordinat = randint(x_start + 1, x_start + 99)
                y_koordinat = randint(y_start + 1, y_start + 99)
                self.assertTrue(temp.er_inni(x_koordinat, y_koordinat))

            # greater is outside
            for _ in range(1000):
                x_koordinat = randint(x_start + 101, x_start + 1000)
                self.assertFalse(temp.er_inni(x_koordinat, y_start))
                y_koordinat = randint(y_start + 101, y_start + 1000)
                self.assertFalse(temp.er_inni(x_start, y_koordinat))

            # Smaller is outside
            for _ in range(1000):
                x_koordinat = randint(x_start - 1000, x_start - 1)
                self.assertFalse(temp.er_inni(x_koordinat, y_start))
                y_koordinat = randint(y_start - 1000, y_start - 1)
                self.assertFalse(temp.er_inni(x_start, y_koordinat))

    def test_flytt(self):
        for _ in range(1000):
            x_start = randint(-100, 100)
            y_start = randint(-100, 100)
            x_move = randint(-100, 100)
            y_move = randint(-100, 100)
            temp = Sprite(x_start, y_start, 20, 20)
            temp.flytt(x_move, y_move)
            self.assertEqual(temp.x_start, x_start + x_move)
            self.assertEqual(temp.y_start, y_start + y_move)


if __name__ == '__main__':
    unittest.main()
