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
        card = self.cards.get_card_by_name("Morgan")
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
