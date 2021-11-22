from database.db_constelations import DBConstellations, Constellations
from database.db_stars import DBStars, Stars
from database.db_drawingconstellation import  DrawingConstellation, DbDrawingConstellation
import pandas as pd
import common.cardinal_direction as cd


def importconstelations():
    file = pd.read_csv("Gwiazdozbiory.csv", encoding='cp1250', sep=",")
    df = pd.DataFrame(file, columns=['Name', 'declination', 'rectascension', 'Symbolism', 'area'])
    i = 0
    while i < file.Name.size:
        print(i)
        newconst = Constellations()
        newconst.name = df.loc[i, 'Name']
        newconst.declination = float(df.loc[i, 'declination'])
        newconst.rectascension = float(df.loc[i, 'rectascension'])
        newconst.symbolism = df.loc[i, 'Symbolism']
        newconst.area = df.loc[i, 'area']
        if float(df.loc[i, 'declination']) >= 0:
            newconst.sky_side = cd.CardinalDirection.North.value
        else:
            newconst.sky_side = cd.CardinalDirection.South.value
        print(newconst)
        DBConstellations(newconst).add_entity()
        i = i + 1


def importstar():
        file = pd.read_excel('../Mariadb/Gwiazdy.xlsx')
        i = 0

        while i < file.Name.size:
            star = Stars()
            star.name = file.Name[i]
            star.rectascensionh = file.Rectascensionh[i]
            star.rectascensionm = file.Rectascensionm[i]
            star.rectascensions = file.Rectascensions[i]
            star.declinationh = file.Declinationh[i]
            star.declinationm = file.Declinationm[i]
            star.declinations = file.Declinations[i]
            star.radial_speed = file.RadialSpeed[i]
            star.distance = file.Distance[i]
            star.brightness = file.Brightness[i]
            star.star_type = file.StarType[i]
            star.mass = file.Mass[i]
            star.greek_symbol = file.GreekSymbol[i]
            star.confirmed = 'YES'
            cons = DBConstellations().get_one_by_name(file.Constellation[i])
            star.constellation = cons
            res = DBConstellations(star).add_entity()
            print(res)
            i = i + 1


def drawnigconst():
    file = pd.read_excel('../Mariadb/RysowanieID.xlsx')
    i = 0

    while i < file.inID.size:
        inid = DBStars().get_one_by_name(file.inID[i])
        outid = DBStars().get_one_by_name(file.outID[i])
        const_id = DBConstellations().get_one_by_name(file.constellationID[i])
        drstar = DrawingConstellation()
        drstar.star_name_in = inid[0].id
        drstar.star_name_out = outid[0].id
        drstar.constellation_id = const_id.id
        print(drstar.star_name_out, drstar.star_name_in, drstar.constellation_id)
        res = DbDrawingConstellation(drstar).add_entity()
        print(res)
        i = i + 1


importconstelations()