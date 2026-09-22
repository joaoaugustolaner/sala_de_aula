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
            saldo_inicial-= saques[index]
        else:
            negados.append(saques[index])
        index+=1
    
    return saldo_inicial

def remover_duplicados(lista: list):

    not_duplicados = []
        
    for numero in lista:
        if numero not in not_duplicados:
            not_duplicados.append(numero)
    
    return not_duplicados


def media_positivos(numeros: list):
    if not numeros: #verifica se len(numeros) == 0
        return 0.0
    
    divisor = 0
    valor = 0
    for numero in numeros:
        if numero > 0:
            valor += numero
            divisor += 1
    
    return valor/divisor

def validador_senha(senhas:list[str]):
    validas = []
    for senha in senhas:
        if len(senha) > 8:
            validas.append(senha)

    return validas

def primeiro_impar(numeros: list):

    index = 0

    while (index < len(numeros)):
        if numeros[index] % 2 != 0:
            return numeros[index]
    
    return None


def contar_ocorrencias(lista:list, target):
    ocurrences = 0
    for element in lista:
        if element == target:
            ocurrences+=1

    return ocurrences

def is_estritamente_crescente(palavras: list):

    index = 1

    while (index < len(palavras) - 1):
        if len(palavras[index] > len(palavras[index-1])):
            pass
        else:
            return False
    
    return True

def mover_zeros_para_o_final(numeros: list):
    zeros_final = numeros.copy()

    for numero in zeros_final:
        #TODO: 
        pass
    pass




if __name__ == '__main__':
    numeros_pares = filtrar_pares([1, 2, 3, 4, 5, 6])
    print(numeros_pares)
    
    not_duplicados = remover_duplicados([1, 3, 2, 3, 1, 4, 2])
    print(not_duplicados)

    zero_final = mover_zeros_para_o_final([0, 1, 0, 3, 12, 0, 5])
    print(zero_final)
    