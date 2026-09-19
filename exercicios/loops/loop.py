def filtrar_pares(numeros: list):
    pares = [] # ou pares = list()

    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        
    return pares

def contar_negativos(numeros: list):
    count = 0
    for numero in numeros:
        if numero < 0:
            count+=1
    return count

def somar_maiores_que(numeros: list, limite:int):
    soma = 0
    for numero in numeros:
        if numero > limite:
            soma+=numero
    
    return soma

def zerar_negativos(numeros: list):
    aux = numeros.copy()

    for numero in numeros:
        if numero < 0:
            indice = numeros.index(numero)
            aux[indice] = 0
    
    return aux

def contem_valor(lista:list, alvo):
    index = 0 
    while(index < len(lista)):
        if lista[index] == alvo:
            return True
        index=+1

    return False

def contar_aprovados(notas: list):
    count = 0
    for nota in notas:
        if nota >= 7:
            count+=1

    return count

def filtrar_palavras_curtas(palavras:list , tamanho_maximo:int):
    filtro = []

    for palavra in palavras:
        if len(palavra) <= tamanho_maximo:
            filtro.append(palavra)

    return filtro



def separar_pares_impares(numeros:list):
    pares, impares = 0

    for numero in numeros:
        if numero % 2 != 0:
            impares+=1
        else:
            pares+=1
    
    return f"Pares: {pares} | Ímpares: {impares}"

def encontrar_extremos(numeros: list):
    maior, menor = 0

    for numero in numeros:
        if numero > maior:
            maior = numero
        
        if numero < menor:
            menor = numero
        
    return (menor, maior)

def simular_saque(saldo_inicial:float, saques: list):

    index = 0
    permitidos = []
    negados = []

    while (index < len(saques)):
        if saldo_inicial - saques[index] >= 0:
            permitidos.append(saques[index])
            saldo_inicial-=saques[index]
        else:
            negados.append(saques[index])
        index+=1
    
    return saldo_inicial








if __name__ == '__main__':
    numeros_pares = filtrar_pares([1, 2, 3, 4, 5, 6])
    print(numeros_pares)
    