class Film:
    def __init__(self, s:str) -> None:
        v:list[str] = s.strip().split(';')
        self.cim:str = v[0]
        self.fazis:int = int(v[1])
        self.bemutato:str = v[2]
        self.kiadas:int = int(v[3])
        self.bevetel:int = int(v[4])
        self.haszon:float = self.bevetel / self.kiadas

def feladat01a() -> None:
    szoveg:str = input('irjon be egy legaláabb 9 karakter hosszu szoveget: ')
    if len(szoveg) > 8:
        for i in range(len(szoveg)):
            kisbetus:str = szoveg.lower()
            print(kisbetus[len(kisbetus) - 1 - i], end='')
    else: print(f'a {szoveg} kevesebb 9 karakter!')

def feladat01b() -> None:
    sz:str = input(f'irj be egy legaláabb 9 karakter hosszu szoveget: ')
    if len(sz) > 8: print(sz.lower()[::-1])
    else: print(f'a {sz} kevesebb, mint 9 karakter!')

def feladat02() -> None:
    print('''paradicsom:  1199 Ft/Kg 
paprika:     1349 Ft/Kg 
vöröshagyma:  289 Ft/Kg''')

    osszar:int = 0
    while input('kíván vásárolni?: ') == 'igen':
        termek:str = input('melyik termékből?: ')
        egysegar:int = 0
        if   termek == 'paradicsom':  egysegar = 1199
        elif termek == 'paprika':     egysegar = 1349
        elif termek == 'vöröshagyma': egysegar =  289
        else: print('nincs ilyen termék!')
        if egysegar != 0:
            mennyiseg:float = float(input(f'hány kg {termek}-t kér?: '))
            tetel:float = egysegar * mennyiseg
            osszar += tetel
    print(f'összesen fizetendő: {osszar} Ft')