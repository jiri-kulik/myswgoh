from enum import Enum, auto

class Alignment(Enum):
    LIGHT_SIDE = 1
    DARK_SIDE = 2

class Role(Enum):
    Attacker = auto()
    Support = auto()
    Tank = auto()

factions: list[str] = ['Resistance', 'Jedi', 'Droid', 'Unaligned force user', 'Empire', 'Sith']