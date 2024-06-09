import streamlit as st

import data.targets

st.set_page_config(page_title='SWGOH Test')
st.title('SWGOH Test')

factions: list[str] = ['Jedi', 'Old Republic', 'Galactic Republic', 'Droid',
                       'Rebel', 'Resistance']

class Character:
    """SWGOH Character Class"""
    def __init__(self, name: str, factions_list: list[str]=[], leader: bool=False):
        if name in [ch.name for ch in characters]:
            raise ValueError(f'The character {name} already exists')
        self.name = name
        for f in factions_list:
            if f not in factions:
                raise ValueError(f'Faction {f} does not exist')
        self.factions = factions_list
        self.isLeader = leader

characters: list[Character] = []

ch: Character = Character(name='R2-D2',
                          factions_list=['Droid', 'Rebel', 'Galactic Republic',
                                         'Resistance'])
characters.append(ch)
st.write(ch.name)
st.write(ch.factions)

st.write(data.targets.targets)