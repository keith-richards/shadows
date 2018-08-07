import sys
sys.path.append("../")
import unittest

import shadows
from shadows.Game import *
from shadows.Knight import *
from shadows.CoatOfArms import *

class TestKnight(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.arthur = Knight(CoatOfArms.ARTHUR)
        self.tristan = Knight(CoatOfArms.TRISTAN)
        self.galahad = Knight(CoatOfArms.GALAHAD)
        self.game.add_knight(self.arthur)
        self.game.add_knight(self.tristan)
        self.game.add_knight(self.galahad)

    def test_lose_life_point(self):
        self.arthur.lose_life_point()
        self.assertTrue(self.arthur.alive())
        self.arthur.lose_life_point()
        self.assertTrue(self.arthur.alive())
        self.arthur.lose_life_point()
        self.assertTrue(self.arthur.alive())
        self.arthur.lose_life_point()
        self.assertFalse(self.arthur.alive())
        self.assertEqual(self.arthur._current_life, 0)
        self.arthur.lose_life_point()
        self.assertEqual(self.arthur._current_life, 0)

    def test_gain_life_point(self):
        self.arthur.gain_life_point()
        self.assertTrue(self.arthur.alive())
        self.arthur.gain_life_point()
        self.assertTrue(self.arthur.alive())
        self.arthur.gain_life_point()
        self.assertTrue(self.arthur.alive())
        self.arthur.gain_life_point()
        self.assertTrue(self.arthur.alive())
        self.assertEqual(self.arthur._current_life, 6)
