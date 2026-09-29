
from animal import Animal
from gato import Gato
from animal_abs import Animal as animal_abstrato
from cachorro import Cachorro

if __name__ == "__main__":


    cao = Cachorro()
    # print(cao.fazer_som())

    gato = Gato("Leôncio")
    print(gato.fazer_som())

    animal = Animal(gato.nome)
    print(animal.fazer_som())