from MaquinaMecanica import MaquinaMecanica

class Bicicleta(MaquinaMecanica):
    DEFAULT_RADIO =33.0
    MIN_RADIO = 17.75
    MAX_RADIO = 36.85
    MAX_DESP = 200.0
    def __init__(self, marca, modelo, fuerzaMotriz="ANIMAL", radioRueda=DEFAULT_RADIO):
        super().__init__(marca,modelo,fuerzaMotriz)
        self.radioRueda = radioRueda
        self.totalKM = 0
    def info(self):
        return "{} Radio: {}, Kilometros: {}".format(super().info(), self.radioRueda, self.totalKM)
    




bisi = Bicicleta("Orbea","PAPAP","ANIMAL", 18)
bisi2 = Bicicleta("Bisi2","Bisiclista")



print(bisi.info())
print(bisi2.info())