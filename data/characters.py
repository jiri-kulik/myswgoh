from enum import Enum
from data.factions import Alignment, Role

class GearLevel(Enum):
    L0 = 0 # Unlocked
    L1 = 1
    L2 = 2
    L3 = 3
    L4 = 4
    L5 = 5
    L6 = 6
    L7 = 7
    L8 = 8
    L9 = 9
    L10 = 10
    L11 = 11
    L12 = 12
    L13 = 13
    R1 = 14
    R2 = 15
    R3 = 16
    R4 = 17
    R5 = 18
    R6 = 19
    R7 = 20
    R8 = 21
    R9 = 22

characters: list[dict] = []
characters.append(dict(name='Rey (JT)', alignment = Alignment.LIGHT_SIDE, role=Role.Tank,
                       isLeader=True, isGL=False, currentGear = GearLevel.L12,
                       factions=['Resistance', 'Unaligned force user']))
characters.append(dict(name='Rey', alignment = Alignment.LIGHT_SIDE, role=Role.Attacker,
                       isLeader=True, isGL=True, currentGear = GearLevel.L0,
                       factions=['Resistance', 'Unaligned force user']))