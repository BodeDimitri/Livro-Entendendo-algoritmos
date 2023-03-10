def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacaoporSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

print(ordenacaoporSelecao([3, 2, 1, 10, 9, 8, 7]))


#Ex- 1) Lista
#Ex- 2) Lista
#Ex- 3) Arrays
#Ex- 4) Maior tempo de execução e movimentar os outros elementos. Movimentação dos outros elementos
#Ex- 5) 