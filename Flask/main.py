from orm import DBStars, DBConstellations, DBPlanet

db = DBStars().get_all()
for d in db:
    print(d)

dv = DBConstellations().get_all()
for i in dv:
    print(i)

dc = DBPlanet().get_all()
for i in dc:
    print(i)
