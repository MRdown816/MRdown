from time import sleep
print('Fill this part alone')


palavra = str(input('What is the word: '))


c = ''
while not len(c) == 500:
    c = c + ' '
    print(c)

print('you can now pass it to the other player, good luck (:')


tent = 5


letrastent = []


tracosedecifrados = ['_'] * len(palavra)


while tent > 0:

    
    print('Welcome to the hangman game!!')
    if tent == 5:
        print('''|--------------------------|
     |                   __|__
     |                  |     |          »»»»»»»»  JOGO DA
     |                  |     |
     |                  |_____|
     |                     |                    
     |                   __|____
     |                 |   |    |
     |                 |   |    | 
     |                 |   |    |         »»»»»» F  O  R  C  A
     |                     |
     |                   __|__                            
     |                  |     |
     |                  |     |
     |                  |     |
     |                  |     |
     |
     |
 ----|------------''')
    elif tent == 4:
        print('''|--------------------------|
     |                   __|__      
     |                  |     |              »»»»»»»»  JOGO DA
     |             -----|-----|------   
     |                  |_____|
     |                     |                    
     |                   __|____
     |                 |   |    |
     |                 |   |    | 
     |                 |   |    |              »»»»»» F  O  R  C  A
     |                     |
     |                   __|__                            
     |                  |     |
     |                  |     |
     |                  |     |
     |                  |     |
     |
     |
 ----|------------''')
    elif tent == 3:
        print('''|--------------------------|
     |                   __|__      
     |                  |     |              »»»»»»»»  JOGO DA
     |             -----|-----|------   
     |                  |_____|
     |                     |                    
     |                   __|____
     |                 |   |    |
     |                 |   | ---|---
     |                 |   |    |              »»»»»» F  O  R  C  A
     |                     |
     |                   __|__                            
     |                  |     |
     |                  |     |
     |                  |     |
     |                  |     |
     |
     |
 ----|------------''')
    elif tent == 2:
        print('''|--------------------------|
     |                   __|__      
     |                  |     |              »»»»»»»»  JOGO DA
     |             -----|-----|------   
     |                  |_____|
     |                     |                    
     |                 ____|____
     |                |    |    |
     |             ---|--- | ---|---
     |                |    |    |              »»»»»» F  O  R  C  A
     |                     |
     |                   __|__                            
     |                  |     |
     |                  |     |
     |                  |     |
     |                  |     |
     |
     |
 ----|------------''')
    elif tent == 1:
        print('''|--------------------------|
     |                   __|__      
     |                  |     |              »»»»»»»»  JOGO DA
     |             -----|-----|------   
     |                  |_____|
     |                     |                    
     |                 ____|____
     |                |    |    |
     |             ---|--- | ---|---
     |                |    |    |              »»»»»» F  O  R  C  A
     |                     |
     |                   __|__                            
     |                  |     |
     |                  |  ---|---
     |                  |     |
     |                  |     |
     |
     |
 ----|------------''')
             
    for palavralimpa in tracosedecifrados:
        print(palavralimpa, end='')
    print(f'\nyou have {tent} attempts!')
    print(f'attempted letters: {letrastent}')
    
    

    letra = str(input('\nwrite a letter that you wish to verify: '))
    for tentadas in letrastent:
        if letra in tentadas:
            print(f'\033[34myou have already attempted that letter!!!\033[m')
    
    letrastent.append(letra)

    
    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                tracosedecifrados[i] = letra
    else:
        tent = tent - 1
    
    if '_' not in tracosedecifrados:
        print(palavra)
        print(f'You won (: !! The word was \033[34m{palavra}\033[m!')
        break
    if tent == 0:
        print(f'\033[31mYou lost ): !!\033[m the word was \033[34m{palavra}\033[m!')
        print('''\033[31m..........................
.                     .
.                     .
.                   . . . 
.                   .   .
.                   . . .
.                     .
.               . . . . . . .
.               .     .      .  
.               .     .      . 
.                     .   
.                     .
.                  . . . .
.                  .     .
.                  .     .
.                  .     .
.
. 
...........     
        \033[m''')
        break
