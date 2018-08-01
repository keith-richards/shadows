import unittest

import shadows
from shadows.Game import *
from shadows.Knight import *
from shadows.CoatOfArms import *

class TestTurnOrderGameState(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.arthur = Knight(CoatOfArms.ARTHUR)
        self.tristan = Knight(CoatOfArms.TRISTAN)
        self.galahad = Knight(CoatOfArms.GALAHAD)
        self.game.add_knight(self.arthur)
        self.game.add_knight(self.tristan)
        self.game.add_knight(self.galahad)

    def test_turn_order(self):
        self.assertEqual(self.game.get_current_player(), self.arthur)
        self.game.set_next_player()
        self.assertEqual(self.game.get_current_player(), self.tristan)
        self.game.set_next_player()
        self.assertEqual(self.game.get_current_player(), self.galahad)
        self.game.set_next_player()
        self.assertEqual(self.game.get_current_player(), self.arthur)

    def test_turn_order_died(self):
        self.assertEqual(self.game.get_current_player(), self.arthur)
        self.game.set_next_player()
        self.assertEqual(self.game.get_current_player(), self.tristan)
        self.game.set_next_player()
        self.game.knight_loose_life_point(self.galahad)
        self.game.knight_loose_life_point(self.galahad)
        self.game.knight_loose_life_point(self.galahad)
        self.game.knight_loose_life_point(self.galahad)
        self.assertFalse(self.game.get_current_player().alive())
        self.assertFalse(self.galahad.alive())        
        self.assertEqual(self.game.get_current_player(), self.galahad)
        self.game.set_next_player()
        self.assertEqual(self.game.get_current_player(), self.arthur)
        self.game.set_next_player()        
        self.assertEqual(self.game.get_current_player(), self.tristan)
        self.game.set_next_player()        
        self.assertEqual(self.game.get_current_player(), self.arthur)
