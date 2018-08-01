

class CoatOfArms(object):
    ARTHUR         = "King Arthur"
    GALAHAD        = "Sir Galahad"
    GAWAIN         = "Sir Gawain"
    KAY            = "Sir Kay"
    PERCIVAL       = "Sir Percival"
    PALAMEDES      = "Sir Palamedes"
    TRISTAN        = "Sir Tristan"
    _arms_list = [ ARTHUR, GALAHAD, GAWAIN, KAY, PERCIVAL, PALAMEDES, TRISTAN ]

class SpecialPower(object):
    TRADE          = "Once per turn you may exchange 1 White card, face down, with another Knight of your choice"
    FREE_SPECIAL   = "During the Heroic Action phase of his turn, Sir Galahad may play one Special White card of his choice as a free Action."
    WHITE_CARDS_3  = "When at the Round Table, if he chooses to draw White cards as his Heroic Action, Sir Gawain draws 3 cards instead of 2."
    FIGHT_PLUS_ONE = "If Sir Kay is on a Quest when a combat ends, he may opt to play an additional White Fight card of his choice, after the Black cards in play have been revealed."
    PEEK           = "During his Progression of Evil phase, Sir Percival may look at the Black card on top of the Draw pile, before deciding which Evil Action he chooses."
    LIFE_PLUS_ONE  = "For each victorious Quest he is on when the Quest ends, Sir Palamedes gains an additional Life point, above and beyond any that may be granted by the Quest's Victory Spoils."
    FREE_MOVE      = "Whenever Sir Tristan departs from the Round Table, he does so at no Action cost."
    _powers_map = {
        CoatOfArms.ARTHUR     : TRADE,
        CoatOfArms.GALAHAD    : FREE_SPECIAL,
        CoatOfArms.GAWAIN     : WHITE_CARDS_3,
        CoatOfArms.KAY        : FIGHT_PLUS_ONE,
        CoatOfArms.PERCIVAL   : PEEK,
        CoatOfArms.PALAMEDES  : LIFE_PLUS_ONE,
        CoatOfArms.TRISTAN    : FREE_MOVE,
        }

    def __getitem__(self, val):
        return self._powers_map[val]

SpecialPowers = SpecialPower()
