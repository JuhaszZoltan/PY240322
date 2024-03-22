class Film:
    def __init__(self, sor:str) -> None:
        v:list[str] = sor.strip().split(';')
        self.cim:str = v[0]
        self.fazis:int = int(v[1])
        self.bemutato:str = v[2]
        self.kiadas:int = int(v[3])
        self.bevetel:int = int(v[4])
        self.haszon:float = self.bevetel / self.kiadas

def feladat03() -> None:
    filmek:list[Film] = []
    marvel_file = open('marvel.txt', 'r', encoding='utf8')
    for s in marvel_file: filmek.append(Film(s))

    print(f'3.1: {len(filmek)} marvel film van')

    osszkoltseg:int = 0
    for f in filmek:
        osszkoltseg += f.kiadas
    kerekitett_atlag:float = round(osszkoltseg / len(filmek), 2)
    print(f'3.2: atlagos gyartasi koltseg: ${kerekitett_atlag}M')

    maxi:int = 0
    for i in range(1, len(filmek)):
        if filmek[i].haszon > filmek[maxi].haszon:
            maxi = i
    print(f'3.3: legkotseghatekonyabb film: {filmek[maxi].cim}')

    keresett_filmek:list[str] = []
    evszam:str = input('3.4: irjon be egy evszamot: ')
    for f in filmek:
        if evszam in f.bemutato:
            keresett_filmek.append(f.cim)
    if len(keresett_filmek) == 0:
        print(f'\t{evszam}-ban/ben nem volt marvel film')
    else:
        print(f'\t{evszam}.ban/ben megjelent filmek:')
        for f in keresett_filmek:
            print(f'\t\t- {f}')

def feladat01() -> None:
    szoveg:str = input('írjon be egy legalább 9 karakterből álló szöveget: ')
    if len(szoveg) > 8:
        print(szoveg.lower()[::-1])
        # for i in range(len(szoveg)):
        #     kisbetus:str = szoveg.lower()
        #     print(kisbetus[len(kisbetus) - 1 - i], end='')
    else: print(f'a {szoveg} kevesebb, mint 9 karakter hosszú :(')

def feladat02() -> None:
    print('''paradicsom:  1000 Ft/Kg 
    paprika:     800 Ft/Kg 
    vöröshagyma:  200 Ft/Kg''')
    osszar:float = 0
    while input('kíván vásárolni?: ') == 'igen':
        termek:str = input('melyik termekbol?: ')
        egysegar:int = 0
        if termek == 'paradicsom': egysegar = 1000
        elif termek == 'paprika': egysegar = 800
        elif termek == 'vöröshagyma': egysegar = 200
        else: print('nincs ilyen termék!')
        if egysegar != 0:
            mennyiseg:float = float(input(f'hány kg {termek}-ra/re van szüksége?: '))
            tetel:float = egysegar * mennyiseg
            osszar += tetel
    kerekitett_ar:int = round(osszar)
    print(f'összesen fizetendő: {kerekitett_ar} HUF')