class Film:
    def __init__(self, sor:str) -> None:
        v:list[str] = sor.strip().split(';')
        self.cim:str = v[0]
        self.fazis:int = int(v[1])
        self.datum:str = v[2]
        self.koltseg:int = int(v[3])
        self.bevetel:int = int(v[4])
        self.haszon:float = self.bevetel/self.koltseg


def feladat01() -> None:
    karakterlanc:str = input('írj be egy legalább 9 karakter hosszú szöveget: ')
    if len(karakterlanc) > 8:
        kisbetus:str = karakterlanc.lower()
        for i in range(len(kisbetus)):
            print(kisbetus[len(kisbetus) - 1 - i], end='')
        # print(karakterlanc.lower()[::-1])
    else: print(f'a {karakterlanc} kevesebb, mint 9 karakter!')


def feladat02() -> None:
    print('paradicsom:  1000 Ft/kg')
    print('paprika:     1200 Ft/kg')
    print('vöröshagyma:  300 Ft/kg')

    osszar:float = 0
    while input('kíván vásárolni?: ') == 'igen':
        termek:str = input('melyik termékből?: ')
        egysegar:int = 0
        if termek == 'paradicsom': egysegar = 1000
        elif termek == 'paprika': egysegar = 1200
        elif termek == 'vöröshagyma': egysegar = 300
        else: print('nincs ilyen termék!')
        if egysegar != 0:
            mennyiseg:float = float(input(f'hány Kg {termek}re/re van szüksége?: '))
            tetel_ar:float = egysegar * mennyiseg
            osszar += tetel_ar
    print(f'összesen fizetendő: {round(osszar)}')