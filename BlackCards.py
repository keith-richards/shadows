from random import shuffle

class BlackCard(object):
    def __init__(self, name, actionA=None, actionB=None):
        self.name = name
        self.actionA = actionA
        self.actionB = actionB

    def __eq__(self, other):
        return self.name == other.name

class BlackCardsDeck(object):
    def __init__(self, game):
        self._game = game
        self._deck = [
            BlackCard("Morgan", lambda: self._game.add_siege_engine(2)),
            BlackCard("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            BlackCard("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            BlackCard("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            BlackCard("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            BlackCard("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            BlackCard("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            BlackCard("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            BlackCard("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            BlackCard("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            BlackCard("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            BlackCard("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            BlackCard("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            BlackCard("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            BlackCard("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
            BlackCard("Excalibur", lambda: self._game.move_excalibur_toward_defeat()),
        ]
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
