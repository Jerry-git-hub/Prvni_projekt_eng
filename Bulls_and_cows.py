
import random

print('Hi there!')
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game. ")


def spravne_cislo(cislo):

    for i in str(cislo):
        cislo2 = str(cislo)
        pocet = cislo2.count(i)
        #print(i, pocet)
        if pocet > 1:
            return False
        elif int(cislo) < 1000 or int(cislo) > 9999:
            return False
    return True

mode = True
while mode:

    cislo = int(random.random() * 10000)
    #print(cislo)
    if spravne_cislo(cislo) == False:
        continue
    else:
        #print(cislo)
        #print(type(cislo))
        break
#print(cislo)
for i in range(0, 3):

    tip_cisla = int(input('Enter the number:'))
    #tip_cisla = 2325
    novy_slovnik = {}
    novy_slovnik2 = {}
    j = 0
    for i in str(cislo):
        novy_slovnik[j] = novy_slovnik.get(i, i)
        j = j + 1
    #print(novy_slovnik)
    b = 0

    for i in str(tip_cisla):
        novy_slovnik2[b] = novy_slovnik2.get(i, i)
        b = b + 1
    #print(novy_slovnik2)
    k = 0
    for i in novy_slovnik:

        if novy_slovnik.get(i) == novy_slovnik2.get(i):
            #print(novy_slovnik[i])
            k = k + 1

    if k == 1:
        k = str(k) + ' bull'
    elif k > 1:
        k = str(k) + ' bulls'

    elif k == 0:
        k = str(k) + ' bulls'
    #print(tip_cisla)
    pocitac_cislo = cislo

    muj_tip = tip_cisla


    pocitac_slovnik = {}
    muj_slovnik = {}
    for i in str(pocitac_cislo):
        pocitac_slovnik[i] = pocitac_slovnik.get(i, 0) + 1

    #print(pocitac_slovnik)

    for i in str(muj_tip):
        muj_slovnik[i] = muj_slovnik.get(i, 0) + 1

    #print(muj_slovnik)
    h = 0

    for i in set(str(muj_tip)) & set(str(pocitac_cislo)):

        if muj_slovnik.get(i) == pocitac_slovnik.get(i):
            #print(muj_slovnik.get(i), 'pocet shod')
            h = h + int(muj_slovnik.get(i))
        elif muj_slovnik.get(i) != pocitac_slovnik.get(i):
            if muj_slovnik.get(i) > pocitac_slovnik.get(i):
                h = h + int(pocitac_slovnik.get(i))
            else:
                h = h + int(muj_slovnik.get(i))

    if h == 1:
        h = str(h) + ' cow'
    elif h > 1:
        h = str(h) + ' cows'
    elif h == 0:
        h = str(h) + ' cows'

    print(k,',', h)

print(cislo)