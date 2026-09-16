
# Execício 1
def formatar_saudacao(nome:str, cidade:str):
    return f"Olá {nome}, seja bem-vindo(a) a {cidade}!"

#Exercício 2
def calcular_perimetro(largura: float, altura: float) -> float:
    perimetro = 2 * (largura + altura)
    return perimetro

# Exercício 3
def fahrenheit_para_celsius(temp_f: float):
    temp_celsius = (temp_f - 32) * (5 / 9)
    return temp_celsius

#Exercício 4
def calcular_gorjeta_por_pessoa(conta:float, 
                                porcentagem_gorjeta:float,
                                pessoas:int):
    gorjeta = (conta * (porcentagem_gorjeta / 100)) / pessoas
    return gorjeta

# Exercício 5
def resumo_circulo(raio:float):
    pi = 3.14159
    area = pi * (raio**2)
    return f"Um círculo de raio {raio} tem área de {area:.2f}"

# Exercício 6
def resumo_juros_basico(capital:float, taxa:float, anos:int):
    M = capital * (1 + taxa/100)**anos
    return f"Após {anos} anos, R$ {capital}, cresce para R${M:.2f}"



if __name__ == '__main__':

    print("EXERCICIOS =============================== \n\n")
    saudacao = formatar_saudacao("Alice", "Porto Alegre")
    print(f"1 - {saudacao}")
    
    perimetro = calcular_perimetro(altura=10, largura=5)
    print(f"2 - {perimetro}")
    
    temperatura_celsius = fahrenheit_para_celsius(68)
    print(f"3 - {temperatura_celsius}")
    
    gorjeta = calcular_gorjeta_por_pessoa(100, 15, 3)
    print(f"4 - {gorjeta}")
    
    area = resumo_circulo(3)
    print(f"5 - {area}")

    juros = resumo_juros_basico(1000, 5, 3)
    print(f"6 - {juros}")


    print("==========================================")