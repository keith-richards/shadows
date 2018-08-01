import unittest

import shadows
from shadows.Game import *
from shadows.Knight import *
from shadows.CoatOfArms import *
from shadows.ProgressEvil import *

class TestProgressEvil(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.arthur = Knight(CoatOfArms.ARTHUR)
        self.tristan = Knight(CoatOfArms.TRISTAN)
        self.galahad = Knight(CoatOfArms.GALAHAD)
        self.game.add_knight(self.arthur)
        self.game.add_knight(self.tristan)
        self.game.add_knight(self.galahad)
        self.knight = self.game.get_current_player()
        
    def test_loose_life_point(self):
        self.assertIsNone(self.game.progress_evil(ProgressEvilChoice.TAKE_LIFE_POINT))
        self.assertIsNone(self.game.progress_evil(ProgressEvilChoice.TAKE_LIFE_POINT))
        self.assertIsNone(self.game.progress_evil(ProgressEvilChoice.TAKE_LIFE_POINT))
        self.assertIsNone(self.game.progress_evil(ProgressEvilChoice.TAKE_LIFE_POINT))
        self.assertFalse(self.game.get_current_player().alive())
        
    def test_siege_engine(self):
        self.assertIsNone(self.game.progress_evil(ProgressEvilChoice.ADD_SIEGE_ENGINE))
        self.assertEqual(self.game._num_siege_engines, 1)
        self.assertIsNone(self.game.progress_evil(ProgressEvilChoice.ADD_SIEGE_ENGINE))
        self.assertIsNone(self.game.progress_evil(ProgressEvilChoice.ADD_SIEGE_ENGINE))
        self.assertEqual(self.game._num_siege_engines, 3)

    def test_draw_card(self):
        self.assertIsNotNone(self.game.progress_evil(ProgressEvilChoice.DRAW_BLACK_CARD))
