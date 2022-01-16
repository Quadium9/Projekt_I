from database.db_constelations import DBConstellations, Constellations
from database.db_stars import Stars
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
            try:
                star = Stars()
                star.name = file.Name[i]
                star.rectascensionh = file.Rectascensionh[i]
                star.rectascensionm = file.Rectascensionm[i]
                star.rectascensions = file.Rectascensions[i]
                star.declinationh = file.Declinationh[i]
                star.declinationm = file.Declinationm[i]
                star.declinations = file.Declinations[i]
                if file.RadialSpeed[i] == 'None':
                    star.radial_speed = None
                else:
                    star.radial_speed = file.RadialSpeed[i]
                if file.Distance[i] == 'None':
                    star.distance = None
                else:
                    star.distance = file.Distance[i]
                if file.Brightness[i] == 'None':
                    star.brightness = None
                else:
                    star.brightness = file.Brightness[i]
                if file.Mass[i] == 'None':
                    star.mass = None
                else:
                    star.mass = file.Mass[i]
                if file.GreekSymbol[i] == 'None':
                    star.greek_symbol = ''
                else:
                    star.greek_symbol = file.GreekSymbol[i].strip()
                star.star_type = file.StarType[i]
                star.confirmed = 'YES'
                cons = DBConstellations().get_one_by_name(file.Constellation[i])
                star.constellation = cons
                res = DBConstellations(star).add_entity()
                print(res)
                i = i + 1
            except:
                i = i + 1


importstar()
