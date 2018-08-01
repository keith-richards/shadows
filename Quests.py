
class Quest(object):
    def __init__(self, game):
        self._game = game
        self._renewable = False
        self.active = True
        self._present_knights = []
        self._max_knights = 1

    def loose(self):
        if self._renewable:
            self.reset()
        else:
            self.active = False

    def win(self):
        if self._renewable:
            self.reset()
        else:
            self.active = False

    def can_add_knight(self):
        return len(self._present_knights) < self._max_knights

    def add_knight(self, knight):
        self._present_knights.append(knight)

    def quest_lost(self):
        if self._quest_lost():
            self.loose()
            return True
        return False

    def quest_won(self):
        if self._quest_won():
            self.win()
            return True
        return False

    def reset(self):
        raise NotImplementedError()
    def _quest_won(self):
        raise NotImplementedError()
    def _quest_lost(self):
        raise NotImplementedError()

class HolyGrailQuest(Quest):
    def __init__(self, game):
        super().__init__(game)
        self._grail_cards = 0
        self._despair_cards = 0
        self._max_knights = 6

    def loose(self):
        super().loose()
        self._game.add_black_sword(3)
        for knight in self._present_knights:
            knight.loose_life_point()

    def win(self):
        super().win()
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
        self._loose_location = -5
        self._current_location = 0
        self._max_knights = 6

    def loose(self):
        super().loose()
        self._game.add_black_sword(2)
        for knight in self._present_knights:
            knight.loose_life_point()

    def win(self):
        super().win()
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
        return self._current_location <= self._loose_location
