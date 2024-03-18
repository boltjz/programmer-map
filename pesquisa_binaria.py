def buscaMenor(arr):
    # Inicializa o menor valor como o primeiro elemento da lista
    menor = arr[0]
    # Inicializa o índice do menor valor como 0
    menor_indice = 0
    # Percorre a lista a partir do segundo elemento
    for i in range(1, len(arr)):
        # Se o elemento atual for menor que o menor valor encontrado até agora
        if arr[i] < menor:
            # Atualiza o menor valor e seu índice
            menor = arr[i]
            menor_indice = i
    # Retorna o índice do menor valor
    return menor_indice

def ordenacaoporSelecao(arr):
    # Cria uma nova lista vazia
    novoArr = []
    # Percorre a lista original
    for i in range(len(arr)):
        # Encontra o menor elemento restante na lista e o remove
        menor = buscaMenor(arr)
        # Adiciona o menor elemento encontrado à nova lista
        novoArr.append(arr.pop(menor))
    # Retorna a nova lista ordenada
    return novoArr

def pesquisa_binaria(lista, item):
    # Inicializa os índices baixo e alto para a pesquisa binária
    baixo = 0
    alto = len(lista) - 1
    # Loop de busca binária
    while baixo <= alto:
        # Calcula o índice do elemento do meio da lista
        meio = (baixo + alto) // 2
        # Obtém o valor do elemento do meio
        chute = lista[meio]
        # Verifica se o valor do meio é igual ao item procurado
        if chute == item:
            # Retorna o índice do elemento se for encontrado
            return meio
        # Se o valor do meio for maior que o item, atualiza o índice alto
        if chute > item:
            alto = meio - 1
        # Se o valor do meio for menor que o item, atualiza o índice baixo
        else:
            baixo = meio + 1
    # Retorna None se o item não for encontrado
    return None

# Lista inicial desordenada
minha_lista = [1, 2, 3, 5, 4, 10, 9, 8, 7, 6]

# Ordena a lista usando o algoritmo de seleção
lista_ordenada = ordenacaoporSelecao(minha_lista)

# Realiza a pesquisa binária na lista ordenada pelo item 3 e imprime o resultado
print(pesquisa_binaria(lista_ordenada, 3))
