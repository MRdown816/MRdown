from time import sleep

## palavra do jogador
palavra = str(input('Qual é a palavra: '))

##esconder palavra
c = ''
while not len(c) == 500:
    c = c + ' '
    print(c)

##tentativas
tent = 5

##letrastentadas
letrastent = []

##lista
tracosedecifrados = ['_'] * len(palavra)

##O inicio do loop
while tent > 0:

    ##menu
    print('Bem vindo!!')
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
    print(f'\nVoçê tem {tent} tentativas!')
    print(f'Letras tentadas: {letrastent}')
    
    
    #letra
    letra = str(input('\nDigite uma letra que deseja verificar: '))
    for tentadas in letrastent:
        if letra in tentadas:
            print(f'\033[34mVoçê já tentou essa letra!!!\033[m')
    
    letrastent.append(letra)

    ##checkar
    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                tracosedecifrados[i] = letra
    else:
        tent = tent - 1
    
    if '_' not in tracosedecifrados:
        print(palavra)
        print(f'Voçê ganhou!! A palavra era {palavra}!')
        break
    if tent == 0:
        print(f'\033[31mVoçê perdeu!!\033[m a palavra era \033[34m{palavra}\033[m!')
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
