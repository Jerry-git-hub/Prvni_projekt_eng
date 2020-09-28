# Přivítání uživatele:

print('Dobrý den, vítá vás Text analyzator!')

# Získání uživatelského jména a hesla:

jmeno = input('Prosím, zadejte své uživatelské jméno:')

heslo = input('Prosím, zadejte své heslo:')

slovník_na_hesla = {'bob' : '123', 'ann' : 'pass123', 'mike' : 'password123', 'liz' : 'pass123'}


mode = True

while mode:
    if heslo == slovník_na_hesla.get(jmeno, 0):

        print('Vítejte v programu!')
        '''
        author =
        '''
        TEXTS = ['''
        Situated about 10 miles west of Kemmerer, 
        Fossil Butte is a ruggedly impressive 
        topographic feature that rises sharply 
        some 1000 feet above Twin Creek Valley 
        to an elevation of more than 7500 feet 
        above sea level. The butte is located just 
        north of US 30N and the Union Pacific Railroad, 
        which traverse the valley. ''',

                 '''At the base of Fossil Butte are the bright 
                 red, purple, yellow and gray beds of the Wasatch 
                 Formation. Eroded portions of these horizontal 
                 beds slope gradually upward from the valley floor 
                 and steepen abruptly. Overlying them and extending 
                 to the top of the butte are the much steeper 
                 buff-to-white beds of the Green River Formation, 
                 which are about 300 feet thick.''',

                 '''The monument contains 8198 acres and protects 
                 a portion of the largest deposit of freshwater fish 
                 fossils in the world. The richest fossil fish deposits 
                 are found in multiple limestone layers, which lie some 
                 100 feet below the top of the butte. The fossils 
                 represent several varieties of perch, as well as 
                 other freshwater genera and herring similar to those 
                 in modern oceans. Other fish such as paddlefish, 
                 garpike and stingray are also present.'''
                 ]

        # Výběr textu:

        text_volba = input('Prosím, vyberte, který text si přejete analyzovat (1/2/3')
        analyzovany_text = ''

        if text_volba == '1':
            analyzovany_text = TEXTS[0]
        elif text_volba == '2':
            analyzovany_text = TEXTS[1]
        elif text_volba == '3':
            analyzovany_text = TEXTS[2]

        # Pro vybraný text zjistěte požadované statistiky

        ocesany_text = []
        analyzovany_text = analyzovany_text.split()
        pocet_slov = int()
        zacina_velkym_pismenem = int()
        velke_slovo = int()
        male_pismeno = int()
        kolik_cisel = int()
        cetnost_slov = {}
        nejdelsi_slovo = []
        grafika = '*'
        soucet_cisel = int()
        for slovo in analyzovany_text:

            slovo = slovo.strip('.,?!')
            pocet_slov = pocet_slov + 1
            if slovo.istitle():
                zacina_velkym_pismenem = zacina_velkym_pismenem + 1
            if slovo.isupper():
                velke_slovo = velke_slovo + 1
            if slovo.islower():
                male_pismeno = male_pismeno + 1
            if slovo.isnumeric():
                kolik_cisel = kolik_cisel + 1
                soucet_cisel = soucet_cisel + int(slovo)

            cetnost_slov[len(slovo)] = cetnost_slov.get(len(slovo), 0) + 1
            nejdelsi_slovo = cetnost_slov.keys()

        print('V textu je:', pocet_slov, 'slov')
        print('V textu je:', zacina_velkym_pismenem, 'slov začínajících velkým písmenem')
        print('V textu je:', velke_slovo, 'slov psaných velkými písmeny')
        print('V textu je:', male_pismeno, 'slov psaných malými písmeny')
        print('V textu je:', kolik_cisel, 'číslo')
        print('Jednoduchý sloupcový graf, který reprezentuje četnost různých slov v textu:')
        for i in sorted(nejdelsi_slovo):
            print(i, '*' * cetnost_slov.get(i, 0), cetnost_slov.get(i, 0))

        print('Součet všech čísel v textu:', soucet_cisel)

        jmeno = input('Prosím, zadejte své uživatelské jméno:')

        heslo = input('Prosím, zadejte své heslo:')
    else:
        print('Zadali jste špatné heslo. Přístup odepřen')
        jmeno = input('Prosím, zadejte své uživatelské jméno:')

        heslo = input('Prosím, zadejte své heslo:')


