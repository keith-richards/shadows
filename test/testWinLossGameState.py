import unittest

import shadows
from shadows.Game import *
from shadows.Knight import *
from shadows.CoatOfArms import *

class TestWinLossGameState(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.arthur = Knight(CoatOfArms.ARTHUR)
        self.game.add_knight(self.arthur)

    def test_black_swords(self):
        for i in range(6):
            self.game.add_black_sword()
            self.assertFalse(self.game.game_lost())
        self.game.add_black_sword()
        self.assertTrue(self.game.game_lost())        

    def test_white_swords(self):
        for i in range(11):
            self.game.add_white_sword()
            self.assertFalse(self.game.game_won())
            self.assertFalse(self.game.game_lost())
        self.game.add_white_sword()
        self.assertTrue(self.game.game_won())
        self.assertFalse(self.game.game_lost())

    def test_swords_equal_white(self):
        for i in range(6):
            self.game.add_white_sword()
        for i in range(6):
            self.game.add_black_sword()
        self.assertFalse(self.game.game_won())
        self.assertTrue(self.game.game_lost())        

    def test_swords_equal_black(self):
        for i in range(6):
            self.game.add_black_sword()
        for i in range(6):
            self.game.add_white_sword()
        self.assertFalse(self.game.game_won())
        self.assertTrue(self.game.game_lost())        

    def test_swords_won(self):
        for i in range(7):
            self.game.add_white_sword()
            self.assertFalse(self.game.game_lost())
            self.assertFalse(self.game.game_won())
        for i in range(6):
            self.game.add_black_sword()
            self.assertFalse(self.game.game_lost())
        self.assertTrue(self.game.game_won())
        self.assertFalse(self.game.game_lost())        
        
    def test_swords_lost(self):
        for i in range(6):
            self.game.add_white_sword()
            self.assertFalse(self.game.game_lost())
            self.assertFalse(self.game.game_won())
        for i in range(7):
            self.game.add_black_sword()
        self.assertTrue(self.game.game_lost())
        self.assertFalse(self.game.game_won())        
        
    def test_game_won_lost(self):
        for i in range(3):
            self.game.knight_loose_life_point(self.arthur)
            self.assertEqual(self.game.game_won(), self.game.game_lost())
        self.game.knight_loose_life_point(self.arthur)
        self.assertNotEqual(self.game.game_won(), self.game.game_lost())
        self.assertTrue(self.game.game_lost())

    def test_dead_knight(self):
        self.game.knight_loose_life_point(self.arthur)
        self.assertFalse(self.game.game_lost())
        self.assertFalse(self.game.game_won())
        self.game.knight_loose_life_point(self.arthur)
        self.assertFalse(self.game.game_lost())
        self.assertFalse(self.game.game_won())
        self.game.knight_loose_life_point(self.arthur)
        self.assertFalse(self.game.game_won())
        self.assertFalse(self.game.game_lost())
        self.game.knight_loose_life_point(self.arthur)
        self.assertFalse(self.game.game_won())
        self.assertTrue(self.game.game_lost())

    def test_dead_knights(self):
        tristan = Knight(CoatOfArms.TRISTAN)
        self.game.add_knight(tristan)
        self.game.knight_loose_life_point(self.arthur)
        self.assertFalse(self.game.game_lost())
        self.assertFalse(self.game.game_won())
        self.game.knight_loose_life_point(self.arthur)
        self.assertFalse(self.game.game_lost())
        self.assertFalse(self.game.game_won())
        self.game.knight_loose_life_point(self.arthur)
        self.assertFalse(self.game.game_won())
        self.assertFalse(self.game.game_lost())
        self.game.knight_loose_life_point(self.arthur)
        self.assertFalse(self.game.game_won())
        self.assertFalse(self.game.game_lost())
        self.game.knight_loose_life_point(tristan)
        self.assertFalse(self.game.game_lost())
        self.assertFalse(self.game.game_won())
        self.game.knight_loose_life_point(tristan)
        self.assertFalse(self.game.game_lost())
        self.assertFalse(self.game.game_won())
        self.game.knight_loose_life_point(tristan)
        self.assertFalse(self.game.game_won())
        self.assertFalse(self.game.game_lost())
        self.game.knight_loose_life_point(tristan)
        self.assertFalse(self.game.game_won())
        self.assertTrue(self.game.game_lost())

    def test_num_seige_engines(self):
        self.game.add_siege_engine()
        self.assertFalse(self.game.game_lost())
        self.assertFalse(self.game.game_won())
        self.game.add_siege_engine()
        self.assertFalse(self.game.game_lost())
        self.assertFalse(self.game.game_won())
        self.game.add_siege_engine()
        self.assertFalse(self.game.game_lost())
        self.assertFalse(self.game.game_won())
        self.game.add_siege_engine()
        self.assertFalse(self.game.game_lost())
        self.assertFalse(self.game.game_won())
        self.game.add_siege_engine()
        self.assertFalse(self.game.game_lost())
        self.assertFalse(self.game.game_won())
        self.game.add_siege_engine()
        self.assertFalse(self.game.game_lost())
        self.assertFalse(self.game.game_won())
        self.game.add_siege_engine()
        self.assertFalse(self.game.game_lost())
        self.assertFalse(self.game.game_won())
        self.game.add_siege_engine()
        self.assertFalse(self.game.game_lost())
        self.assertFalse(self.game.game_won())
        self.game.add_siege_engine()
        self.assertFalse(self.game.game_lost())
        self.assertFalse(self.game.game_won())
        self.game.add_siege_engine()
        self.assertFalse(self.game.game_lost())
        self.assertFalse(self.game.game_won())
        self.game.add_siege_engine()
        self.assertFalse(self.game.game_lost())
        self.assertFalse(self.game.game_won())
        self.game.add_siege_engine()
        self.assertTrue(self.game.game_lost())
        self.assertFalse(self.game.game_won())
