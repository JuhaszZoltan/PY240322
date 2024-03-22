from module import *

# 3. feladat:
filmek:list[Film] = []
file = open('marvel.txt', 'r', encoding='utf-8')
for s in file: filmek.append(Film(s))

# 3.1:
print(f'3.1: {len(filmek)} filmje van a marvel moziverzumnak')

#3.2:
osszkoltseg:int = 0
for f in filmek:
    osszkoltseg += f.koltseg
kerekitett_atlag:float = round(osszkoltseg / len(filmek), 2)
print(f'3.2: atlagos gyartasi koltseg: ${kerekitett_atlag}M')

# 3.3:
maxi:int = 0
for i in range(1, len(filmek)):
    if filmek[i].haszon > filmek[maxi].haszon:
        maxi = i
print(f'3.3: legkoltseghatekonyabb film: {filmek[maxi].cim}')

#3.4:
ev:str = input('3.4: írj be egy évszámot: ')
print(f'a {ev}-ban/ben megjelent filmek:')
for f in filmek:
    if ev in f.datum:
        print(f'\t{f.cim}')

# feladat01()

# feladat02()