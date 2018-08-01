from shadows.Knight import *
from shadows.ProgressEvil import *
from shadows.BlackCards import *
from shadows.Quests import *

class Game(object):
    def __init__(self):
        self._num_siege_engines = 0
        self._num_black_swords = 0
        self._num_white_swords = 0
        self._knights = {}
        self._turn_order = []
        self._black_cards = BlackCardsDeck(self)
        self._black_cards.shuffle_all()
        self._excalibur_quest = ExcaliburQuest(self)
        self._holy_grail_quest = HolyGrailQuest(self)

    def game_lost(self):
        if self._num_siege_engines >= 12:
            return True
        if self._num_black_swords >= 7:
            return True
        if self._num_black_swords + self._num_white_swords >= 12:
            if self._num_black_swords >= self._num_white_swords:
                return True
        living_knights = [k for n, k in self._knights.items() if k.alive() and k.loyal]
        if not living_knights:
            return True
        return False

    def game_won(self):
        if self.game_lost():
            return False
        if self._num_white_swords + self._num_black_swords < 12:
            return False
        return self._num_white_swords > self._num_black_swords

    def add_knight(self, knight):
        self._knights[knight.name] = knight
        self._turn_order.append(knight)

    def add_black_sword(self, num=1):
        self._num_black_swords += num

    def add_white_sword(self, num=1):
        self._num_white_swords += num

    def get_current_player(self):
        return self._turn_order[0]

    def draw_black_card(self):
        return self._black_cards.get_next_card()

    def play_black_card(self, card, actionA=True):
        if actionA:
            card.actionA()
        else:
            card.actionB()

    def discard_black_card(self, card):
        self._black_cards.discard_card(card)

    def set_next_player(self):
        new_turn_order = []
        for k in self._turn_order[1:]:
            if k.alive():
                new_turn_order.append(k)
        if self.get_current_player().alive():
            new_turn_order.append(self.get_current_player())
        self._turn_order = new_turn_order

    def progress_evil(self, evil_action, knight=None):
        if knight is None:
            knight = self.get_current_player()
        if evil_action == ProgressEvilChoice.TAKE_LIFE_POINT:
            self.knight_loose_life_point(knight)
        elif evil_action == ProgressEvilChoice.ADD_SIEGE_ENGINE:
            self.add_siege_engine()
        elif evil_action == ProgressEvilChoice.DRAW_BLACK_CARD:
            return self.draw_black_card()
        return None

    def add_siege_engine(self, num=1):
        self._num_siege_engines += num

    def knight_loose_life_point(self, knight=None, num=1):
        if knight is None:
            knight = self.get_current_player()
        self._knights[knight.name].loose_life_point(num)

    def knight_gain_life_point(self, knight=None):
        if knight is None:
            knight = self.get_current_player()
        self._knights[knight.name].gain_life_point()

    def move_excalibur_toward_defeat(self):
        self._excalibur_quest.move_toward_defeat()

    def add_despair(self):
        self._holy_grail_quest.add_despair()

    def add_desolation(self):
        self._holy_grail_quest.add_desolation()

    def add_knight_to_excalibur(self, knight=None):
        if knight == None:
            knight = self.get_current_player()
        if self._excalibur_quest.can_add_knight():
            self._excalibur_quest.add_knight(knight)

    def add_knight_to_holy_grail(self, knight=None):
        if knight == None:
            knight = self.get_current_player()
        if self._holy_grail_quest.can_add_knight():
            self._holy_grail_quest.add_knight(knight)
