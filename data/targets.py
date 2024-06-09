from data.characters import characters

targets: list[dict] = []

targetName = 'Rey'
chs = [ch for ch in characters if ch['name'] == targetName]
if chs == []:
    raise ValueError(f'Target for character {targetName} not created as the character does not exist.')
elif len(chs) > 1:
    raise ValueError(f'More than one character with name {targetName} exists.')
else:
    targets.append(chs[0])