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
	

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = [1,2,3,5,4,10,9,8,7,6]
print (pesquisa_binaria(ordenacaoporSelecao(minha_lista), 3)) #2
