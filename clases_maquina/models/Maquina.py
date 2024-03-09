from abc import ABC, abstractmethod

class Maquina(ABC):
    marca = ""
    modelo = ""
    numeroDeSerie = 0
    n_maquinas = 0

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        Maquina.n_maquinas += 1
        self.numeroDeSerie = Maquina.n_maquinas

    def info(self):
        return "Marca: {}, Modelo: {}, NºSerie: {}".format(self.marca, self.modelo, self.numeroDeSerie)
    
    def getMarca(self):
        return self.marca

