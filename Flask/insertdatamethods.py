from database.db_constelations import DBConstellations, Constellations
import pandas as pd
import common.cardinal_direction as cd


def getdata():
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

getdata()

