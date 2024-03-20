
#input
#1 feladat
szavak_lista=[]
with open("./info.txt","r",encoding="UTF-8") as fm:
    for  sor in fm:       
        print(sor ,file=fm)
#alprogram
#2 felaadt     
def szavak_szama(mondat):
    with open("./info.txt","r",encoding="UTF-8") as fm:
        for  sor in fm:       
            print(sor ,file=fm)

    for szavak in mondat:
        szavak = mondat.split()

    return len(szavak)


#3 feladat
def visszafelé_szöveg(szöveg):
    
    with open("./info.txt","r",encoding="UTF-8") as fm:
        for  sor in fm:       
            print(sor ,file=fm)

    return szöveg[-1]


#4. feladat
def szavak_listaba(mondat):
    with open("./info.txt","r",encoding="UTF-8") as fm:
        for  sor in fm:       
            print(sor ,file=fm)

    
    szavak = mondat.split()
    return szavak




szavak_lista = szavak_listaba(mondat)
print("A szavak listába olvasása:")


#5 feladat

def maganhangzok_szama(szoveg):
    maganhangzok = "aeiouáéíóöőúüű"
    szam = 0
    for betu in szoveg:
        if betu.lower() in maganhangzok:
            szam += 1
    return szam

def massalhangzok_szama(szoveg):
    massalhangzok = " b, c, d, f, g, h, j, k, l, m, n, p, r, s, t, v, z."
    szam = 0
    for betu in szoveg:
        if betu.lower() in massalhangzok:
            szam += 1
    return szam




# Tesztelés
szoveg = "Ez egy példa szöveg magánhangzók számának kiszámolására."
print


#kiir
def kiir():
    print(szavak_lista)
    print("A szöveg visszafelé:", visszafelé_szöveg(szöveg=))
    print("A mondat szavainak száma:", szavak_szama(szavak_lista))

    






        



    

