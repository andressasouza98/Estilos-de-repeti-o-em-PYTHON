# Imprimei todos os números exceto o 13 (laço"while")

contador = 1 
while(contador <= 20):
    if(contador == 13):
        contador = contador + 1 
        continue
    else :
        print(contador)
        contador = contador + 1