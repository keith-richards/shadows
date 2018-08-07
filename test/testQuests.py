import sys
sys.path.append("../")
import unittest

import shadows
from shadows.Game import *
from shadows.Knight import *
from shadows.CoatOfArms import *
from shadows.Quests import *
from shadows.Cards import *

class TestBlackKnightQuest(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.quest = self.game._black_knight_quest
        self.arthur = Knight(CoatOfArms.ARTHUR)
        self.game.add_knight(self.arthur)
        self.game.add_knight_to_black_knight(self.arthur)

    def test_can_add_pair_a(self):
        self.assertTrue(self.quest._can_add_pair_a(1))
        self.assertTrue(self.quest._can_add_pair_a(2))
        self.assertTrue(self.quest._can_add_pair_a(3))
        self.assertTrue(self.quest._can_add_pair_a(4))
        self.assertTrue(self.quest._can_add_pair_a(5))
        # self.assertTrue(self.quest.add_fight_card(5))
        # todo

class TestExcaliburQuest(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.quest = self.game._excalibur_quest
        self.arthur = Knight(CoatOfArms.ARTHUR)
        self.game.add_knight(self.arthur)
        self.game.add_knight_to_excalibur(self.arthur)

    def test_lose(self):
        self.quest.lose()
        self.assertFalse(self.quest.active)

    def test_win(self):
        self.quest.win()
        self.assertFalse(self.quest.active)

    def test_can_add_knight(self):
        self.assertTrue(self.quest.can_add_knight())
        self.quest.add_knight(self.arthur)
        self.assertTrue(self.quest.can_add_knight())
        self.quest.add_knight(self.arthur)
        self.assertTrue(self.quest.can_add_knight())
        self.quest.add_knight(self.arthur)
        self.assertTrue(self.quest.can_add_knight())
        self.quest.add_knight(self.arthur)
        self.assertTrue(self.quest.can_add_knight())
        self.quest.add_knight(self.arthur)
        self.assertFalse(self.quest.can_add_knight())

    def test_add_knight(self):
        self.assertEqual(len(self.quest._present_knights), 1)

    def test_quest_lost(self):
        self.quest.move_toward_defeat()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.quest.move_toward_defeat()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.quest.move_toward_defeat()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.quest.move_toward_defeat()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.quest.move_toward_defeat()
        self.assertTrue(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.assertFalse(self.quest.active)
        self.assertEqual(self.game._num_black_swords, 2)
        self.assertEqual(self.arthur._current_life, 3)

    def test_quest_won(self):
        self.quest.move_toward_win()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.quest.move_toward_win()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.quest.move_toward_win()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.quest.move_toward_win()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.quest.move_toward_win()
        self.assertFalse(self.quest.quest_lost())
        self.assertTrue(self.quest.quest_won())
        self.assertFalse(self.quest.active)
        self.assertEqual(self.game._num_white_swords, 2)
        self.assertEqual(self.arthur._current_life, 5)

    def test_won_multi(self):
        self.quest.move_toward_win(5)
        self.assertFalse(self.quest.quest_lost())
        self.assertTrue(self.quest.quest_won())
        self.assertFalse(self.quest.active)


class TestSaxonQuest(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.quest = self.game._saxon_quest
        self.arthur = Knight(CoatOfArms.ARTHUR)
        self.game.add_knight(self.arthur)
        self.game.add_knight_to_saxon(self.arthur)

    def test_lose(self):
        self.quest.lose()
        self.assertTrue(self.quest.active)

    def test_win(self):
        self.quest.win()
        self.assertTrue(self.quest.active)
        self.assertEqual(self.game._num_siege_engines, 0)
        self.assertEqual(self.game._num_white_swords, 1)

    def test_can_add_knight(self):
        self.assertTrue(self.quest.can_add_knight())
        self.quest.add_knight(self.arthur)
        self.assertTrue(self.quest.can_add_knight())
        self.quest.add_knight(self.arthur)
        self.assertTrue(self.quest.can_add_knight())
        self.quest.add_knight(self.arthur)
        self.assertTrue(self.quest.can_add_knight())
        self.quest.add_knight(self.arthur)
        self.assertTrue(self.quest.can_add_knight())
        self.quest.add_knight(self.arthur)
        self.assertFalse(self.quest.can_add_knight())

    def test_add_knight(self):
        self.assertEqual(len(self.quest._present_knights), 1)

    def test_quest_lost(self):
        self.quest.add_saxon()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.quest.add_saxon()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.quest.add_saxon()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.quest.add_saxon()
        self.assertTrue(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.assertTrue(self.quest.active)
        self.assertEqual(self.game._num_black_swords, 1)
        self.assertEqual(self.game._num_siege_engines, 2)
        self.assertEqual(self.arthur._current_life, 3)

    def test_reset(self):
        self.quest.reset()
        self.assertTrue(self.quest.active)

class TestPictQuest(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.quest = self.game._pict_quest
        self.arthur = Knight(CoatOfArms.ARTHUR)
        self.game.add_knight(self.arthur)
        self.game.add_knight_to_pict(self.arthur)

    def test_lose(self):
        self.quest.lose()
        self.assertTrue(self.quest.active)

    def test_win(self):
        self.quest.win()
        self.assertTrue(self.quest.active)
        self.assertEqual(self.game._num_siege_engines, 0)
        self.assertEqual(self.game._num_white_swords, 1)

    def test_can_add_knight(self):
        self.assertTrue(self.quest.can_add_knight())
        self.quest.add_knight(self.arthur)
        self.assertTrue(self.quest.can_add_knight())
        self.quest.add_knight(self.arthur)
        self.assertTrue(self.quest.can_add_knight())
        self.quest.add_knight(self.arthur)
        self.assertTrue(self.quest.can_add_knight())
        self.quest.add_knight(self.arthur)
        self.assertTrue(self.quest.can_add_knight())
        self.quest.add_knight(self.arthur)
        self.assertFalse(self.quest.can_add_knight())

    def test_add_knight(self):
        self.assertEqual(len(self.quest._present_knights), 1)

    def test_quest_lost(self):
        self.quest.add_pict()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.quest.add_pict()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.quest.add_pict()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.quest.add_pict()
        self.assertTrue(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.assertTrue(self.quest.active)
        self.assertEqual(self.game._num_black_swords, 1)
        self.assertEqual(self.game._num_siege_engines, 2)
        self.assertEqual(self.arthur._current_life, 3)

    def test_reset(self):
        self.quest.reset()
        self.assertTrue(self.quest.active)

class TestHolyGrailQuest(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.quest = self.game._holy_grail_quest
        self.arthur = Knight(CoatOfArms.ARTHUR)
        self.game.add_knight(self.arthur)
        self.game.add_knight_to_holy_grail(self.arthur)

    def test_lose(self):
        self.quest.lose()
        self.assertFalse(self.quest.active)

    def test_win(self):
        self.quest.win()
        self.assertFalse(self.quest.active)

    def test_can_add_knight(self):
        self.assertTrue(self.quest.can_add_knight())
        self.quest.add_knight(self.arthur)
        self.assertTrue(self.quest.can_add_knight())
        self.quest.add_knight(self.arthur)
        self.assertTrue(self.quest.can_add_knight())
        self.quest.add_knight(self.arthur)
        self.assertTrue(self.quest.can_add_knight())
        self.quest.add_knight(self.arthur)
        self.assertTrue(self.quest.can_add_knight())
        self.quest.add_knight(self.arthur)
        self.assertFalse(self.quest.can_add_knight())

    def test_number_despair(self):
        self.quest.add_despair()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.assertEqual(self.quest._grail_cards, 0)
        self.assertEqual(self.quest._despair_cards, 1)

    def test_number_desolation(self):
        self.quest.add_desolation()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.assertEqual(self.quest._grail_cards, 0)
        self.assertEqual(self.quest._despair_cards, 1)
        self.quest.add_grail()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.assertEqual(self.quest._grail_cards, 1)
        self.assertEqual(self.quest._despair_cards, 1)
        self.quest.add_desolation()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.assertEqual(self.quest._grail_cards, 0)
        self.assertEqual(self.quest._despair_cards, 2)

    def test_mixed_crossover(self):
        self.quest.add_desolation()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.assertEqual(self.quest._grail_cards, 0)
        self.assertEqual(self.quest._despair_cards, 1)
        self.quest.add_grail()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.assertEqual(self.quest._grail_cards, 1)
        self.assertEqual(self.quest._despair_cards, 1)

    def test_number_grail(self):
        self.quest.add_grail()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.assertEqual(self.quest._grail_cards, 1)
        self.assertEqual(self.quest._despair_cards, 0)

    def test_lost(self):
        self.quest.add_despair()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.quest.add_despair()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.quest.add_despair()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.quest.add_despair()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.quest.add_despair()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.quest.add_despair()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.quest.add_despair()
        self.assertTrue(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.assertFalse(self.quest.active)
        self.assertEqual(self.game._num_black_swords, 3)
        self.assertEqual(self.arthur._current_life, 3)

    def test_won(self):
        self.quest.add_grail()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.quest.add_grail()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.quest.add_grail()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.quest.add_grail()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.quest.add_grail()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.quest.add_grail()
        self.assertFalse(self.quest.quest_lost())
        self.assertFalse(self.quest.quest_won())
        self.quest.add_grail()
        self.assertFalse(self.quest.quest_lost())
        self.assertTrue(self.quest.quest_won())
        self.assertFalse(self.quest.active)
        self.assertEqual(self.game._num_white_swords, 3)
        self.assertEqual(self.arthur._current_life, 5)
