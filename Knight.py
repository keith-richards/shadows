from shadows.CoatOfArms import *

class Knight(object):
    def __init__(self, coat):
        self._coat_of_arms = coat 
        self._current_life = 4
        self._max_life = 6
        self._special_power = SpecialPowers[self._coat_of_arms]
        self.name = coat
        self.loyal = True

    def alive(self):
        return self._current_life > 0

    def loose_life_point(self, num=1):
        self._current_life -= num

    def gain_life_point(self, num=1):
        self._current_life += num
        
    def __repr__(self):
        return self.name
