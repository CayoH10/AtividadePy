def soma_elementos(matriz): #Atividade 1
    soma = 0
    for linha in matriz:
        for elemento in linha:
            soma += elemento
    return soma
matriz = [
    [1,2,3],
    [4,5,6]
]
print(soma_elementos(matriz))

def maior_elemento(matriz): #Atividade 2
    return max(max(linha) for linha in matriz)

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(maior_elemento(matriz))

def soma_diagonal(matriz): #Atividade 3
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]
    return soma

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(soma_diagonal(matriz))

def transposta(matriz): #Atividade 4
    linhas = len(matriz)
    colunas = len(matriz[0])
    resultado = []
    for j in range(colunas):
        nova_linha = []
        for i in range(linhas):
            nova_linha.append(matriz[i][j])
        resultado.append(nova_linha)
    return resultado

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(transposta(matriz))

def multiplicar(matriz): #Atividade 5
    k = 4
    resultado = []
    for linha in matriz:
        nova_linha = []
        for elemento in linha:
            nova_linha.append(elemento * k)
        resultado.append(nova_linha)
    return resultado

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(multiplicar(matriz))

def identidade(matriz): #Atividade 6
    linhas = len(matriz)

    for linha in matriz:
        if len(matriz) != linhas:
            return False
        
    for i in range(linhas):
        for j in range(linhas):
            if i == j:
                if matriz[i][j] != 1:
                    return False
            else:
                if matriz[i][j] != 0:
                    return False
    return True

matriz = [
    [1,0,0],
    [0,1,0],
    [0,0,1]
]
print(identidade(matriz))

def soma_matrizes(A, B): #Atividade 7
    m = len(A)
    n = len(A[0])
    resultado = []

    for i in range(m):
        linha = []
        for j in range(n):
            linha.append(A[i][j] + B[i][j])
        resultado.append(linha)
    return resultado

matriz1 = [
    [1,2,3],
    [4,5,6]
]

matriz2 = [
    [1,2,3],
    [4,5,6]
]
print(soma_matrizes(matriz1, matriz2))

def contar_maiores(matriz): #Atividade 8
    x = 5
    contador = 0
    for linha in matriz:
        for elemento in linha:
            if elemento > x:
                contador += 1
    return contador

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(contar_maiores(matriz))

def maior_soma(matriz): #Atividade 9
    maior = float('-inf')
    indice = -1

    for i, linha in enumerate(matriz):
        soma = sum(linha)
        if soma > maior:
            maior = soma
            indice = i
    return indice

matriz = [
    [1,2,3],
    [7,8,9],
    [4,5,6]
]
print(maior_soma(matriz))

def media_elementos(matriz): #Atividade 10
    soma = 0
    total = 0

    for linha in matriz:
        for elemento in linha:
            soma += elemento
            total += 1

    if total == 0:
        return 0
    return soma / total

matriz = [
    [1,2,3],
    [4,5,6]
]
print(media_elementos(matriz))




        
        