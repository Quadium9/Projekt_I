import enum


class StarsType(enum.Enum):
    hypergiants = 'Hiper Gigant',
    supergiants = 'Super Gigant',
    brightgiants = 'Żółty Olbrzym',
    giants = 'Olbrzym',
    subgiants = 'Subolbrzym',
    dwarf = 'Karzeł',
    subdwarf = 'Podkarzeł',
    reddwarf = 'Czerwony Karzeł',
    whitedwarf = 'Biały Karzeł',
    browndwarf = 'Brązowy Karzeł',
    unknown = 'Nieznana'


StarsLevel = {
    'hypergiants': 0,
    'supergiants': 10,
    'brightgiants': 21,
    'giants': 47,
    'subgiants': 53,
    'dwarf': 69,
    'subdwarf': 78,
    'reddwarf': 90,
    'whitedwarf': 102,
    'browndwarf': 156
}


def check_level(starnumber):
    if starnumber > StarsLevel['browndwarf']:
        return StarsType.browndwarf.value
    if starnumber > StarsLevel['whitedwarf']:
        return StarsType.whitedwarf.value
    if starnumber > StarsLevel['reddwarf']:
        return StarsType.reddwarf.value
    if starnumber > StarsLevel['subdwarf']:
        return StarsType.subdwarf.value
    if starnumber > StarsLevel['dwarf']:
        return StarsType.dwarf.value
    if starnumber > StarsLevel['subgiants']:
        return StarsType.subgiants.value
    if starnumber > StarsLevel['giants']:
        return StarsType.giants.value
    if starnumber > StarsLevel['brightgiants']:
        return StarsType.brightgiants.value
    if starnumber > StarsLevel['supergiants']:
        return StarsType.supergiants.value
    if starnumber > StarsLevel['hypergiants']:
        return StarsType.hypergiants.value
