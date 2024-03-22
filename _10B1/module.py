
class Film:
    def __init__(self, s:str) -> None:
        v:list[str] = s.strip().split(';')
        self.cim:str = v[0]
        self.fazis:int = int(v[1])
        self.bemutato:str = v[2]
        self.kiadas:int = int(v[3])
        self.bevetel:int = int(v[4])
        self.haszonarany:float = self.bevetel / self.kiadas


def feladat01() -> None:
    szoveg:str = input('írjon be egy legalább 9 karakterből álló szöveget: ')
    if len(szoveg) > 8: print(szoveg.lower()[::-1])
    else: print('hiba!')

    if len(szoveg) > 8:
        for i in range(len(szoveg)):
            print(szoveg[len(szoveg) - i - 1].lower(), end='')
    else: print(f'a {szoveg} nincs legalább 9 karakter')

def feladat02() -> None:
    print('''paradicsom:  1199 Ft/Kg 
    paprika:     1349 Ft/Kg 
    vöröshagyma:  289 Ft/Kg''')

    osszar:int = 0
    while input('szeretn-e vásárolni?: ') == 'igen':
        termek:str = input('mit szeretne vásárolni?: ')
        egysegar:int = 0
        if termek == 'paradicsom': egysegar = 1199
        elif termek == 'paprika': egysegar = 1349
        elif termek == 'vöröshagyma': egysegar = 289
        else : print('sajnálom, nincs ilyen tejmék! :(')
        if egysegar != 0:
            mennyiseg:float = float(input(f'hány kg {termek}-et szeretne vásárolni?: '))
            tetel:float = egysegar * mennyiseg
            osszar += tetel
    print(f'összesen fizetendő: {osszar}')