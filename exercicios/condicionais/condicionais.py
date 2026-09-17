def fizz_buzz(numero:int):
    if numero % 3 == 0 and numero % 5 == 0:
        return "fizzbuzz"
    elif numero % 5 == 0:
        return "buzz"
    elif numero % 3 == 0:
        return "fizz"
    else:
        return numero

def verificar_paridade(numero: int):
    if numero%2 == 0: #if numero%2 != 0
        return "par"
    return "ímpar"

def classificar_numero(numero: int):
    if numero > 0:
        return "Positivo"
    if numero < 0:
        return "Negativo"
    
    return "Zero"

def calcular_resultado(nota_1: float, nota_2:float):
    if (nota_1 + nota_2) / 2 > 7:
        return "Aprovado"
    
    return "Reprovado"

def maior_de_dois(a:int, b:int):
    if a > b:
        return "O primeiro é maior"
    if a == b:
        return "São iguais"
    
    return "São iguais"

def calcular_desconto(valor_compra:float, 
                      cliente_vip:bool):
    if cliente_vip or valor_compra > 200:
        return f"Valor final: R$ {valor_compra*0.85}"
    return f"Valor final: R$ {valor_compra * 0.95}"

def conceito_nota(nota:float):
    if nota >= 9 and nota < 10:
        return "A"
    if nota >= 7 and nota < 9:
        return "B"
    if nota > 5 and nota < 7:
        return "C"
    return "F"

def validar_triangulo(a:float, b:float, c:float):
    if (a+b > c) and (b+c > a) and (a+c > b):
        if a == b == c:
            return "Equilátero"

        if a == b != c:
            return "Isóceles"
        
        if a != b != c:
            return "Escaleno"
    else:
        return "Não é triângulo"

def calcular_imposto(salario:float):
    

if __name__ == "__main__":
    teste = fizz_buzz(15)
    print(teste)