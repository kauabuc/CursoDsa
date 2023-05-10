class Circulo:
    pi = 3.14

    def __init__(self, raio=5) -> None:
        self.raio = raio

    def area(self):
        return (self.raio * self.raio) * Circulo.pi

    def set_raio(self, novo_raio):
        self.raio = novo_raio

    def get_raio(self):
        return self.raio


circ = Circulo()
print(circ.get_raio())

circ1 = Circulo(7)
print(circ1.get_raio())

circ.set_raio(3)
print(circ.get_raio())
