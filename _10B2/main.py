from module import *

filmek:list[Film] = []
file = open('marvel.txt', 'r', encoding='utf-8')
for s in file: filmek.append(Film(s))

print(f'3.1: {len(filmek)} film van')

osszkoltseg:int = 0
for f in filmek:
    osszkoltseg += f.kiadas
atlag:float = round(osszkoltseg / len(filmek), 2)
print(f'3.2: atlagos gyartasi koltseg: ${atlag}M')

maxi:int = 0
for i in range(1, len(filmek)):
    if filmek[i].haszon > filmek[maxi].haszon:
        maxi = i
print(f'3.3: legkötséghatékonyabb film: {filmek[maxi].cim}')

evszam:str = input('3.4: írj be egy évszámot: ')
print(f'{evszam}-ban/ben bemutatott filmek:')
for f in filmek:
    if evszam in f.bemutato:
        print(f'\t{f.cim}')

# feladat01a()
# feladat01b()
# feladat02()