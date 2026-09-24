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

    for numero in numeros:
        if numero == 0:
            zeros_final.remove(numero)
            zeros_final.append(numero)
            
    return zeros_final
        
def processar_fila(clientes: list[tuple]):
    aux = []
    index = 0

    for client in clientes:
        if client[1] >= 60:
            aux.insert(index, client)
            index+=1
        else:
            aux.append(client)

    return aux


def encontrar_picos(numeros: list[int]):
    picos = []
    index = 1

    while(index < len(numeros) - 1):
        if numeros[index-1] < numeros[index] and \
            numeros[index] > numeros[index + 1]:
            
            picos.append(numeros[index])

    return picos

         
def validar_extrato(saldo_inicial: float, 
                    transacoes: list):
    
    index = 0
    saldo_final = saldo_inicial

    while (index < len(transacoes)):
        if saldo_final < 0:
            return f"Extrato Inválido: Saldo Negativo na Posição {index}"
        else:
            saldo_final += transacoes[index]
        
        return f"Extrato Válido: Saldo Final R$ {saldo_final}"





if __name__ == '__main__':
    numeros_pares = filtrar_pares([1, 2, 3, 4, 5, 6])
    print(f"1 - {numeros_pares}")
    
    negativos = contar_negativos([2,1,-1,4,-9,-7])
    print(f"2 - {negativos}")

    soma = somar_maiores_que([10, 5, 20, 3, 15], 8)
    print(f"3 - {soma}")

    sem_negativos = zerar_negativos([4, -2, 7, -9, 0])
    print(f"4 - {sem_negativos}")

    valor = contem_valor(["maçã", "banana", "uva"], "banana")
    print(f"5 - {valor}")

    aprovados = contar_aprovados([8.5, 5.0, 7.0, 6.5, 9.0])
    print(f"6 - {aprovados}")

    filtro_palavras = filtrar_palavras_curtas(["sol", "computador", "python", "mar"], 6)
    print(f"7 - {filtro_palavras}")

    not_duplicados = remover_duplicados([1, 3, 2, 3, 1, 4, 2])
    print(f"11 - {not_duplicados}")

    zero_final = mover_zeros_para_o_final([0, 1, 0, 3, 12, 0, 5])
    print(f"17- {zero_final}")

    fila = processar_fila([("Ana", 25), ("Bento", 67), ("Carla", 18), ("Daniel", 72)])
    print(f"18 - {fila}")

    picos = encontrar_picos([1, 5, 2, 6, 3, 1, 8, 4])
    print(f"19 - {picos}")

    saldo1 = validar_extrato(100, [-50, -60, 20])
    print(f"20.1 - {saldo1}")

    saldo2 = validar_extrato(50, [30, -40, -20, 100])
    print(f"20.2 - {saldo2}")