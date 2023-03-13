#Apenas a recursiva sem um caso-base
def regressiva(i):
    print(i)
    regressiva(i-1)



#1) Caso-base é quando a função não chama a si mesma/ 2) Caso-recursivo: Função chama a si mesma
def regressiva2(i):
    print(i)
    if i <= 1: #1
        return 
    else: #2
        regressiva2(i - 1)

