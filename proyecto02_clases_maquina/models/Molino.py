from MaquinaMecanica import MaquinaMecanica

class Molino(MaquinaMecanica):
    def __init__(self, tipoDeMolino, marca, modelo, fuerzaMotriz=MaquinaMecanica.DEFAULT_FUERZA):
        super().__init__(marca, modelo, fuerzaMotriz)
        self.tipoDeMolino = tipoDeMolino
    def info(self):
        return "{} Molino de : {}".format(super().info(), self.tipoDeMolino)