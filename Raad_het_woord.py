import random
from hangman import hangman

def split(word): 
    nieuwe_list = []
    for char in word:
        nieuwe_list.append(char)
    return nieuwe_list 
   
verzameling = ['brommer','auto','vliegtuig','bus']
te_raden_woord = random.choice(verzameling)
lengte_te_raden_woord = len(te_raden_woord)
aantal_fout_geraden_letters= 0

print('\n')

goed_geraden_letters = []
fout_geraden_letters = []
lengte = 0
aantal_beurten = 0

#  Het te raden woord splitten in aparte letters in list
letters_in_list = split(te_raden_woord)

doorgaan = True
while doorgaan:
    #het uitprinten van allemaal streepjes in de lengte van het te raden woord
    print('Het te raden woord heeft een lengte van '+str(lengte_te_raden_woord)+' letters')    
    while lengte < (lengte_te_raden_woord):
        goed_geraden_letters.append('_')
        lengte +=1
    uitprinten= ' '.join(goed_geraden_letters)
    print(uitprinten)
    print('\n')
    # oproepen van functie hangman
    hangman(aantal_fout_geraden_letters)
    
    # input door speler van een bepaalde letter en check of deze al eerder is ingevoerd
    invoer_letter = input(print('\nGeef hier uw te raden letter'))
    if invoer_letter in goed_geraden_letters or invoer_letter in fout_geraden_letters:
            print('deze letter heb je al gehad, probeer opnieuw')
            continue
    
    # input door speler van een bepaalde letter en check of deze voor komt in het te rade woord
    if invoer_letter in te_raden_woord:        
        print('YES, hebt een goede letter geraden!')
        for i in range(0,len(letters_in_list)):
            if invoer_letter == letters_in_list[i]:
                goed_geraden_letters[i]= invoer_letter
           
        aantal_beurten = aantal_beurten+1

        # als speler heeft gewonnen
        if '_' not in goed_geraden_letters:
            print('Je hebt het woord '+te_raden_woord.upper() +' geraden in '+str(aantal_beurten)+' beurten!!!')
            nogeenkeer = input('Wilt u nog een spelletje spelen? (y/n) : ')
            if nogeenkeer == 'n':
                doorgaan = False
            else:
                # alles resetten voor nieuw spel
                aantal_beurten = 0
                aantal_fout_geraden_letters= 0
                te_raden_woord = random.choice(verzameling)
                lengte_te_raden_woord = len(te_raden_woord)
                letters_in_list = split(te_raden_woord)
                goed_geraden_letters = []
                fout_geraden_letters = []
                lengte = 0
                
    else: # als speler geen goede letter heeft geraden
        print('Helaas, probeer opnieuw')
        fout_geraden_letters.append(invoer_letter)
        aantal_beurten = aantal_beurten+1
        aantal_fout_geraden_letters  = aantal_fout_geraden_letters+1

        # als hangman volledig is en dus speler heeft verloren
        if aantal_fout_geraden_letters == 7:
            hangman(aantal_fout_geraden_letters)
            print('Je hebt helaas verloren!')
            nogeenkeer2 = input('Wilt u nog een spelletje spelen? (y/n) : ')
            if nogeenkeer2 == 'n':
                doorgaan = False
            else:
                # alles resetten voor nieuw spel
                aantal_beurten = 0
                aantal_fout_geraden_letters= 0
                te_raden_woord = random.choice(verzameling)
                lengte_te_raden_woord = len(te_raden_woord)
                letters_in_list = split(te_raden_woord)
                goed_geraden_letters = []
                fout_geraden_letters = []
                lengte = 0

     
print('GAME OVER')



