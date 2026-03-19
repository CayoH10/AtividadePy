def soma_elementos(numeros): #Atividade 1
    return sum(numeros)

numeros = [5,6,7,8,9]
print(soma_elementos(numeros))

def contar_pares(numeros): #Atividade 2
    pares = []
    for i in numeros:
        if i % 2 == 0:
            pares.append(i)
    return pares
numeros = [2,4,5,7,8]
print(contar_pares(numeros))

def maior_numero(numeros): #Atividade 3
    return max(numeros)

numeros = [21, 54, 46, 87]
print(maior_numero(numeros))

def quant_maiores(numeros): #Atividade 4
    num = 20
    valores = []
    for i in numeros:
        if i > num:
            valores.append(i)
    return valores
numeros = [12,20,34,77,98,100]
print(quant_maiores(numeros))

def soma_pares(numeros): #Atividade 5
    lista = []
    for i in numeros:
        if i % 2 == 0:
            lista.append(i)
    return sum(lista)

numeros = [2, 4, 7, 9, 20]
print(soma_pares(numeros))

def existencia_num(numeros): #Atividade 6
    num = 7
    for i in numeros:
        if i == num:
            return True
        
numeros = [5, 7, 8, 9, 10]
print(existencia_num(numeros))

def inverter_lista(numeros): #Atividade 7
    lista = []
    for i in range(len(numeros) - 1, -1, -1):
        lista.append(numeros[i])
    return lista

numeros = [1,2,3,4,5,6,7]
print(inverter_lista(numeros))

def contar_ocorrencias(numeros): #Atividade 8
    lista = []
    num = 4
    for i in numeros:
        if i == num:
            lista.append(i)
    return len(lista)

numeros = [4,5,6,7,4,2,23,46,4,86]
print(contar_ocorrencias(numeros))

def contar_positivos(numeros): #Atividade 9
    lista = []
    for i in numeros:
        if i >= 0:
            lista.append(i)
    return lista

numeros = [-3, -2, -1, 0, 1, 2, 3]
print(contar_positivos(numeros))

def produto_num(numeros): #Atividade 10
    resultado = 1
    for i in numeros:
        resultado *= i
    return resultado

numeros = [3,4,6,2]
print(produto_num(numeros))

def contar_vogais(s): #Atividade 11
    vogais = "aeiouAEIOU"
    contador = 0
    for i in s:
        if i in vogais:
            contador += 1
    return contador

s = "Ola, mundo!"
print(contar_vogais(s))

def contar_char(s): #Atividade 12
    contador = 0
    for i in s:
        contador +=1
    return contador

s = "Paradigma!"
print(contar_char(s))

def ocorrencias_char(s): #Atividade 14
    char = "cC"
    contador = 0
    for i in s:
        if i in char:
            contador += 1
    return contador
s = "Claus"
print(ocorrencias_char(s))