
# Execício 1
def formatar_saudacao(nome:str, cidade:str):
    return f"Olá {nome}, seja bem-vindo(a) a {cidade}!"

#Exercício 2
def calcular_perimetro(largura: float, altura: float) -> float:
    perimetro = 2 * (largura + altura)
    return perimetro



if __name__ == '__main__':

    print("EXERCICIOS =============================== \n\n")
    saudacao = formatar_saudacao("Alice", "Porto Alegre")
    print(f"1 - {saudacao}")
    perimetro = calcular_perimetro(altura=10, largura=5)
    print(f"2 - {perimetro}")
    print("==========================================")