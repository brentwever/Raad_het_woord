def hangman(aantal_fouten):
    if aantal_fouten == 7:
        print('     ','------')
        print('     ','|    |')
        print('     ','|    O')
        print('     ','|  --|--')
        print('     ','|    |')
        print('     ','|   / \ ')
        print('     ','|     ')
    
    if aantal_fouten == 6:
        print('     ','------')
        print('     ','|    |')
        print('     ','|    O')
        print('     ','|  --|--')
        print('     ','|    |')
        print('     ','|   /  ')
        print('     ','|     ')
    if aantal_fouten == 5:
        print('     ','------')
        print('     ','|    |')
        print('     ','|    O')
        print('     ','|  --|--')
        print('     ','|    |')
        print('     ','|     ')
        print('     ','|     ')
    if aantal_fouten == 4:
        print('     ','------')
        print('     ','|    |')
        print('     ','|    O')
        print('     ','|  --|--')
        print('     ','|       ')
        print('     ','|     ')
        print('     ','|     ')
    if aantal_fouten == 3:
        print('     ','------')
        print('     ','|    |')
        print('     ','|    O')
        print('     ','|  --|')
        print('     ','|    ')
        print('     ','|     ')
        print('     ','|     ')
    if aantal_fouten == 2:
        print('     ','------')
        print('     ','|    |')
        print('     ','|    O')
        print('     ','|    |')
        print('     ','|     ')
        print('     ','|     ')
        print('     ','|     ')
    if aantal_fouten == 1:
        print('     ','------')
        print('     ','|    |')
        print('     ','|    O')
        print('     ','|      ')
        print('     ','|      ')
        print('     ','|      ')
        print('     ','|     ')
    if aantal_fouten == 0:
        print('     ','------')
        print('     ','|    |')
        print('     ','|   ')
        print('     ','|  ')
        print('     ','|  ')
        print('     ','|    ')
        print('     ','|     ')