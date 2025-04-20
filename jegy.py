import random

def osztaly_adatok():
    letszam = int(input("Add meg az osztály létszámát: "))
    
    jegyek = []
    for i in range(letszam):
        jegy = random.randint(1, 10)
        jegyek.append(jegy)
    
    atlag = sum(jegyek) / letszam
    
    bukott = 0
    volt_egyes = False
    volt_kituno = False
    
    for jegy in jegyek:
        if jegy < 4:
            bukott += 1
        if jegy == 1:
            volt_egyes = True
        if jegy == 10:
            volt_kituno = True
    
    print(f"Jegyek: {jegyek}")
    print(f"Átlag: {atlag}")
    print(f"Bukott diákok száma: {bukott}")
    print(f"Volt-e 1-es osztályzat: {'Igen' if volt_egyes else 'Nem'}")
    print(f"Van-e kitűnő jegy: {'Igen' if volt_kituno else 'Nem'}")

osztaly_adatok()
