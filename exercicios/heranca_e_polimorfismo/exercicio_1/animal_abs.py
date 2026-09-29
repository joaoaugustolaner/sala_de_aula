from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def fazer_som(self):
        pass