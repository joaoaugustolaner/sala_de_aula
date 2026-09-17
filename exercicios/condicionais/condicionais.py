def fizz_buzz(numero:int):
    if numero % 3 == 0 and numero % 5 == 0:
        return "fizzbuzz"
    elif numero % 5 == 0:
        return "buzz"
    elif numero % 3 == 0:
        return "fizz"
    else:
        return numero

if __name__ == "__main__":
    teste = fizz_buzz(15)
    print(teste)