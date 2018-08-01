import sys
sys.path.append("../")
import unittest

import shadows
from shadows.BlackCards import *
from shadows.Game import *

class TestBlackCards(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.cards = BlackCardsDeck(self.game)
        self.arthur = Knight(CoatOfArms.ARTHUR)
        self.tristan = Knight(CoatOfArms.TRISTAN)
        self.galahad = Knight(CoatOfArms.GALAHAD)
        self.game.add_knight(self.arthur)
        self.game.add_knight(self.tristan)
        self.game.add_knight(self.galahad)

    def test_morgan(self):
        card = self.cards.get_card_by_name("Morgan_1")
        self.game.play_black_card(card)
        self.assertEqual(self.game._num_siege_engines, 2)
        self.game.discard_black_card(card)

    def test_excalibur(self):
        card = self.cards.get_card_by_name("Excalibur")
        self.game.play_black_card(card)
        self.assertFalse(self.game._excalibur_quest.quest_lost())
        self.game.play_black_card(card)
        self.assertFalse(self.game._excalibur_quest.quest_lost())
        self.game.play_black_card(card)
        self.assertFalse(self.game._excalibur_quest.quest_lost())
        self.game.play_black_card(card)
        self.assertFalse(self.game._excalibur_quest.quest_lost())
        self.game.play_black_card(card)
        self.assertTrue(self.game._excalibur_quest.quest_lost())
        self.assertEqual(self.game._num_black_swords, 2)

    def test_despair(self):
        card = self.cards.get_card_by_name("Despair")
        self.game.play_black_card(card)
        self.assertFalse(self.game._holy_grail_quest.quest_lost())
        self.assertFalse(self.game._holy_grail_quest.quest_won())
        self.game.play_black_card(card)
        self.assertFalse(self.game._holy_grail_quest.quest_lost())
        self.assertFalse(self.game._holy_grail_quest.quest_won())
        self.game.play_black_card(card)
        self.assertFalse(self.game._holy_grail_quest.quest_lost())
        self.assertFalse(self.game._holy_grail_quest.quest_won())
        self.game.play_black_card(card)
        self.assertFalse(self.game._holy_grail_quest.quest_lost())
        self.assertFalse(self.game._holy_grail_quest.quest_won())
        self.game.play_black_card(card)
        self.assertFalse(self.game._holy_grail_quest.quest_lost())
        self.assertFalse(self.game._holy_grail_quest.quest_won())
        self.game.play_black_card(card)
        self.assertFalse(self.game._holy_grail_quest.quest_lost())
        self.assertFalse(self.game._holy_grail_quest.quest_won())
        self.game.play_black_card(card)
        self.assertTrue(self.game._holy_grail_quest.quest_lost())
        self.assertFalse(self.game._holy_grail_quest.quest_won())

    def test_desolation(self):
        card = self.cards.get_card_by_name("Desolation")
        self.game.play_black_card(card)
        self.assertFalse(self.game._holy_grail_quest.quest_lost())
        self.assertFalse(self.game._holy_grail_quest.quest_won())
        self.game.play_black_card(card)
        self.assertFalse(self.game._holy_grail_quest.quest_lost())
        self.assertFalse(self.game._holy_grail_quest.quest_won())
        self.game.play_black_card(card)
        self.assertFalse(self.game._holy_grail_quest.quest_lost())
        self.assertFalse(self.game._holy_grail_quest.quest_won())
        self.game.play_black_card(card)
        self.assertFalse(self.game._holy_grail_quest.quest_lost())
        self.assertFalse(self.game._holy_grail_quest.quest_won())
        self.game.play_black_card(card)
        self.assertFalse(self.game._holy_grail_quest.quest_lost())
        self.assertFalse(self.game._holy_grail_quest.quest_won())
        self.game.play_black_card(card)
        self.assertFalse(self.game._holy_grail_quest.quest_lost())
        self.assertFalse(self.game._holy_grail_quest.quest_won())
        self.game.play_black_card(card)
        self.assertTrue(self.game._holy_grail_quest.quest_lost())
        self.assertFalse(self.game._holy_grail_quest.quest_won())

    def test_grail_despair_desolation(self):
        deso = self.cards.get_card_by_name("Desolation")
        self.game.play_black_card(deso)
        desp = self.cards.get_card_by_name("Despair")
        self.game.play_black_card(desp)
        # 2 d, 0g
        self.assertFalse(self.game._holy_grail_quest.quest_lost())
        self.assertFalse(self.game._holy_grail_quest.quest_won())
        self.game._holy_grail_quest.add_grail()
        # 2 d, 1 g
        self.assertFalse(self.game._holy_grail_quest.quest_lost())
        self.assertFalse(self.game._holy_grail_quest.quest_won())
        self.game._holy_grail_quest.add_grail()
        # 2 d, 2 g
        self.game._holy_grail_quest.add_grail()
        # 2 d, 3 g
        self.game._holy_grail_quest.add_grail()
        # 2 d, 4 g
        self.game._holy_grail_quest.add_grail()
        # 2 d, 5 g
        self.assertFalse(self.game._holy_grail_quest.quest_lost())
        self.assertFalse(self.game._holy_grail_quest.quest_won())
        self.game._holy_grail_quest.add_grail()
        # 1 d, 5 g
        self.assertFalse(self.game._holy_grail_quest.quest_lost())
        self.assertFalse(self.game._holy_grail_quest.quest_won())
        self.game._holy_grail_quest.add_grail()
        # 1 d, 6 g
        self.assertFalse(self.game._holy_grail_quest.quest_lost())
        self.assertFalse(self.game._holy_grail_quest.quest_won())
        self.game.play_black_card(deso)
        # 2 d, 5 g
        self.assertFalse(self.game._holy_grail_quest.quest_lost())
        self.assertFalse(self.game._holy_grail_quest.quest_won())
        self.game._holy_grail_quest.add_grail()
        # 1 d, 5 g
        self.assertFalse(self.game._holy_grail_quest.quest_lost())
        self.assertFalse(self.game._holy_grail_quest.quest_won())
        self.game._holy_grail_quest.add_grail()
        # 1 d, 6 g
        self.assertFalse(self.game._holy_grail_quest.quest_lost())
        self.assertFalse(self.game._holy_grail_quest.quest_won())
        self.game.play_black_card(desp)
        # 1 d, 5 g
        self.assertFalse(self.game._holy_grail_quest.quest_lost())
        self.assertFalse(self.game._holy_grail_quest.quest_won())
        self.game._holy_grail_quest.add_grail()
        # 1 d, 6 g
        self.assertFalse(self.game._holy_grail_quest.quest_lost())
        self.assertFalse(self.game._holy_grail_quest.quest_won())
        self.game._holy_grail_quest.add_grail()
        # 0 d, 6 g
        self.assertFalse(self.game._holy_grail_quest.quest_lost())
        self.assertFalse(self.game._holy_grail_quest.quest_won())
        self.game._holy_grail_quest.add_grail()
        # 0 d, 7 g
        self.assertFalse(self.game._holy_grail_quest.quest_lost())
        self.assertTrue(self.game._holy_grail_quest.quest_won())
