
class Quest(object):
    def __init__(self, game):
        self._game = game
        self._present_knights = []
        self._max_knights = 1
        self.active = True
        self._add_extra_black = False

    def add_extra_black(self):
        self._add_extra_black = True

    def can_add_knight(self):
        return len(self._present_knights) < self._max_knights

    def add_knight(self, knight):
        self._present_knights.append(knight)

    def quest_lost(self):
        if self._quest_lost():
            self.lose()
            return True
        return False

    def quest_won(self):
        if self._quest_won():
            self.win()
            return True
        return False

    def _quest_won(self):
        raise NotImplementedError()
    def _quest_lost(self):
        raise NotImplementedError()
    def win(self):
        raise NotImplementedError()
    def loose(self):
        raise NotImplementedError()

class ValueCardQuest(Quest):
    def __init__(self, game, max_fight_cards, max_black_cards):
        super().__init__(game)
        self._max_fight_cards = max_fight_cards
        self._max_black_cards = max_black_cards
        self._fight_cards = []
        self._black_cards = []

    def _quest_won(self):
        if len(self._fight_cards) == self._max_fight_cards or\
           len(self._black_cards) == self._max_black_cards:
            return sum([c.value for c in self.fight_cards]) >\
                sum([c.value for c in self.black_cards])

    def _add_black_card(self, card):
        self._black_cards.append(card)

    def _add_white_card(self, card):
        self._white_cards.append(card)

class BlackKnightQuest(ValueCardQuest):
    def __init__(self, game):
        super().__init__(game, 4, 4)
        self.pair_a = []
        self.pair_b = []

    def _can_add_pair_a(self, value):
        if len(self.pair_a) == 0:
            return True
        if len(self.pair_a) == 2:
            return False
        return value in self.pair_a

    def _can_add_pair_b(self, value):
        if len(self.pair_b) == 0:
            return True
        if len(self.pair_b) == 2:
            return False
        return value in self.pair_b

    def add_fight_card(self, card):
        if self._can_add_pair_a(card.value):
            if card.value not in self.pair_b:
                self.pair_a.append(card)
                return True
        elif self._can_add_pair_b(card.value):
            if card.value not in self.pair_a:
                self.pair_b.append(card)
                return True
        return False

class MercWarQuest(Quest):
    def __init__(self, game):
        super().__init__(game)
        self._max_knights = 6
        self._num_white_cards = 0
        self._num_bad_guys = 0

    def reset(self):
        self._present_knights = []

    def _quest_won(self):
        return self._num_white_cards == 5

    def _quest_lost(self):
        return self._num_bad_guys == 4

    def _add_bad_guy(self):
        self._num_bad_guys += 1

    def add_fight_card(self, fight_card):
        if fight_card.value and fight_card.value == self._num_white_cards + 1:
            self._num_white_cards += 1
            return True
        return False

    def win(self):
        self._game.allow_merlins()
        self._game.add_white_sword()
        for knight in self._present_knights:
            knight.gain_life_point()

    def lose(self):
        self._game.add_black_sword()
        if self._add_extra_black:
            self._game.add_black_sword()
        self._game.add_siege_engine(2)
        for knight in self._present_knights:
            knight.lose_life_point()
        self.reset()

class PictQuest(MercWarQuest):
    def __init__(self, game):
        super().__init__(game)

    def add_pict(self):
        self._add_bad_guy()

class SaxonQuest(MercWarQuest):
    def __init__(self, game):
        super().__init__(game)

    def add_saxon(self):
        self._add_bad_guy()

class HolyGrailQuest(Quest):
    def __init__(self, game):
        super().__init__(game)
        self._grail_cards = 0
        self._despair_cards = 0
        self._max_knights = 6

    def lose(self):
        self.active = False
        self._game.add_black_sword(3)
        if self._add_extra_black:
            self._game.add_black_sword()
        for knight in self._present_knights:
            knight.lose_life_point()

    def win(self):
        self._game.allow_merlins()
        self.active = False
        self._game.add_white_sword(3)
        for knight in self._present_knights:
            knight.gain_life_point()
        # TODO share cards

    def add_grail(self):
        if self._grail_cards + self._despair_cards == 7:
            self._despair_cards -= 1
        else:
            self._grail_cards += 1

    def add_despair(self):
        if not self.active:
            self._game.add_siege_engine()
            return
        if self._grail_cards + self._despair_cards == 7:
            self._grail_cards -= 1
        else:
            self._despair_cards += 1

    def add_desolation(self):
        if not self.active:
            self._game.add_siege_engine()
            return
        if self._grail_cards:
            self._grail_cards -= 1
        self._despair_cards += 1

    def _quest_won(self):
        if not self.active:
            return False
        return self._grail_cards == 7 and self._despair_cards == 0

    def _quest_lost(self):
        if not self.active:
            return False
        return self._grail_cards == 0 and self._despair_cards == 7

class ExcaliburQuest(Quest):
    def __init__(self, game):
        super().__init__(game)
        self._win_location = 5
        self._lose_location = -5
        self._current_location = 0
        self._max_knights = 6

    def lose(self):
        self.active = False
        self._game.add_black_sword(2)
        if self._add_extra_black:
            self._game.add_black_sword()
        for knight in self._present_knights:
            knight.lose_life_point()

    def win(self):
        self._game.allow_merlins()
        self.active = False
        self._game.add_white_sword(2)
        for knight in self._present_knights:
            knight.gain_life_point()
        # TODO share cards

    def move_toward_defeat(self):
        if self.active:
            self._current_location -= 1
        else:
            self._game.add_siege_engine()

    def move_toward_win(self, num=1):
        if not self.active:
            return
        self._current_location += num

    def _quest_won(self):
        if not self.active:
            return False
        return self._current_location >= self._win_location

    def _quest_lost(self):
        if not self.active:
            return False
        return self._current_location <= self._lose_location
