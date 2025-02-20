from Boneco import boneco
import random
from biblioteca import biblioteca
print("1- frutas, 2-casa,3-escritorio ,4-escola ,5-esporte")
opcao = int(input("escolha o tema: "))
palavra = biblioteca(opcao)
palavra_aleatoria = random.choice(palavra)
lista = palavra_aleatoria
cont = len(lista)
letras = [] 
letra_certa = 0
preencher = '*'
erro = 0 
for z in range(0, cont):
    letras.append(preencher)
print("A palavra e: ", letras)
while True:
    
    letra = str(input("digite sua letra: "))
    if letra not in lista:
        print("n tem essa letra")
        erro +=1 
        if erro > 6:
            print("voce perdeu!\nAcabaram suas tentativas...")
            break
        else:
            boneco(erro) 
    else:
        for i in range(0,cont):
            if(letra == lista[i]):
                del letras[i]
                letras.insert(i,lista[i])
                letra_certa += 1
        if letra_certa == cont:
            print(letras)
            print("\nVoce ganhou!")
            break
        else:
            print(letras)

    
    