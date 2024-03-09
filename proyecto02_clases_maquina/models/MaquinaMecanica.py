from Maquina import Maquina

class MaquinaMecanica(Maquina):
    DEFAULT_FUERZA = "COMBUSTIBLE"

    def __init__(self, marca, modelo, fuerzaMotriz=DEFAULT_FUERZA):
        super().__init__(marca, modelo)
        self.fuerzaMotriz = fuerzaMotriz

    def info(self):
        return "Marca: {}, Modelo: {}, NºSerie: {}, Fuerza: {}".format(self.marca, self.modelo, self.numeroDeSerie, self.fuerzaMotriz)
