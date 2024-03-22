from module import *

filmek:list[Film] = []
marvel_file = open('marvel.txt', 'r', encoding='utf-8')
for s in marvel_file: filmek.append(Film(s))

print(f'3.1: {len(filmek)} film van')

osszkoltseg:int = 0
for f in filmek:
    osszkoltseg += f.kiadas
kerekitett_atlag:float = round(osszkoltseg / len(filmek), 2)
print(f'3.2: atlagos gyartasi koltseg: ${kerekitett_atlag}M')

maxi:int = 0
for i in range(1, len(filmek)):
    if filmek[i].haszonarany > filmek[maxi].haszonarany:
        maxi = i
print(f'3.3: a legköltseghatekonyabb film: {filmek[maxi].cim}')


evszam:str = input('3.4: irjon be egy evszamot: ')
print(f'a {evszam}-ban/ben megjelent marvel filmek: ')
for f in filmek:
    if evszam in f.bemutato:
        print(f'\t{f.cim}')

# feladat01()
# feladat02()