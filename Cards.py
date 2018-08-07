from random import shuffle

class Card(object):
    def __init__(self, name, actionA=None, actionB=None, value=None):
        self.name = name
        self.actionA = actionA
        self.actionB = actionB
        self.value = value

    def __eq__(self, other):
        return self.name == other.name and self.value == other.value

class CardDeck(object):
    def __init__(self, game):
        self._game = game
        self._discard = []

    def shuffle_all(self):
        self._deck.extend(self._discard)
        shuffle(self._deck)
        self._discard = []

    def get_card_by_name(self, card_name):
        for c in self._deck:
            if c.name == card_name:
                return c

    def get_discarded_card_by_name(self, card_name):
        for c in self._discard:

            if c.name == card_name:
                return c

    def get_next_card(self):
        if not self._deck:
            self.shuffle_all()
        return self._deck[0]

    def discard_card(self, card):
        for c in self._deck:
            if c.name == card.name:
                self._deck.remove(c)
                self._discard.append(c)
                return

class WhiteCardsDeck(CardDeck):
    def __init__(self, game):
        super().__init__(game)
        self._deck = [
            Card("Fight_5", value=5)
        ]

class BlackCardsDeck(CardDeck):
    def __init__(self, game):
        super().__init__(game)
        self._deck = [
            Card("Vivien", lambda: self._game.disallow_merlins()),
            Card("MistsOfAvalon", lambda: self._game.lost_quests_add_extra_black()),
            Card("Morgan_4", lambda: self._game.add_siege_engine(2)),

            Card("Pict", lambda: self._game.add_pict()),
            Card("Pict", lambda: self._game.add_pict()),
            Card("Pict", lambda: self._game.add_pict()),
            Card("Pict", lambda: self._game.add_pict()),
            Card("Saxon", lambda: self._game.add_saxon()),
            Card("Saxon", lambda: self._game.add_saxon()),
            Card("Saxon", lambda: self._game.add_saxon()),
            Card("Saxon", lambda: self._game.add_saxon()),
            Card("Mercenaries", lambda: self._game.add_pict(), lambda: self._game.add_saxon()),
            Card("Mercenaries", lambda: self._game.add_pict(), lambda: self._game.add_saxon()),
            Card("Mercenaries", lambda: self._game.add_pict(), lambda: self._game.add_saxon()),
            Card("Mercenaries", lambda: self._game.add_pict(), lambda: self._game.add_saxon()),
            Card("Despair", lambda: self._game.add_despair()),
            Card("Despair", lambda: self._game.add_despair()),
            Card("Despair", lambda: self._game.add_despair()),
            Card("Despair", lambda: self._game.add_despair()),
            Card("Despair", lambda: self._game.add_despair()),
            Card("Despair", lambda: self._game.add_despair()),
            Card("Despair", lambda: self._game.add_despair()),
            Card("Despair", lambda: self._game.add_despair()),
            Card("Despair", lambda: self._game.add_despair()),
            Card("Despair", lambda: self._game.add_despair()),
            Card("Despair", lambda: self._game.add_despair()),
            Card("Despair", lambda: self._game.add_despair()),
            Card("Despair", lambda: self._game.add_despair()),
            Card("Despair", lambda: self._game.add_despair()),
            Card("Despair", lambda: self._game.add_despair()),
            Card("Desolation", lambda: self._game.add_desolation()),
            Card("Desolation", lambda: self._game.add_desolation()),
            Card("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            Card("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            Card("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            Card("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            Card("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            Card("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            Card("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            Card("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            Card("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            Card("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            Card("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            Card("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            Card("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            Card("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            Card("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
        ]
