import random

def split(word): 
    nieuwe_list = []
    for char in word:
        nieuwe_list.append(char)
    return nieuwe_list 
   
verzameling = ['brommer','auto','vliegtuig']
te_raden_woord = random.choice(verzameling)
lengte_te_raden_woord = len(te_raden_woord)
aantal_fout_geraden_letters= 0

print('\n')
print('Het te raden woord heeft een lengte van '+str(lengte_te_raden_woord)+' letters')

#het uitprinten van allemaal streepjes in de lengte van het te raden woord
lengte = 0
goed_geraden_letters = []
while lengte < (lengte_te_raden_woord):
    goed_geraden_letters.append('_')
    lengte +=1
uitprinten= ''.join(goed_geraden_letters)
print(uitprinten)

aantal_beurten = 0

#  Het te raden woord splitten in aparte letters in list
letters_in_list = split(te_raden_woord)

not_win = True
while not_win:
    invoer_letter = input(print('\nGeef hier uw te raden letter'))
    
    if invoer_letter in te_raden_woord:
        if invoer_letter in goed_geraden_letters:
            print('deze letter heb je al gehad, probeer opnieuw')
            continue
        print('YES, hebt een goede letter geraden, ga door!')
        for i in range(0,len(letters_in_list)):
            if invoer_letter == letters_in_list[i]:
                goed_geraden_letters[i]= invoer_letter

        separator = ''
        samengevoegd = separator.join(goed_geraden_letters)
        print('\n'+(samengevoegd)   )        
        aantal_beurten = aantal_beurten+1
        if '_' not in goed_geraden_letters:
           break
    
    else:
        print('Helaas, probeer opnieuw')
        separator = ''
        samengevoegd = separator.join(goed_geraden_letters)
        print('\n'+(samengevoegd)   )
        aantal_beurten = aantal_beurten+1
        aantal_fout_geraden_letters  = aantal_fout_geraden_letters+1

     
print('Je hebt het woord geraden! Game over')
print('Je hebt het woord geraden in '+str(aantal_beurten)+' beurten!!!')
print('Je hebt '+str(aantal_fout_geraden_letters)+ ' letters fout geraden.')



