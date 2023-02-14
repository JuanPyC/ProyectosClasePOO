class Punto :

    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

    def print_coord(self):
        print("coordenadas x:",self.x,"coordenada y:", self.y)

punto = Punto(5, 10)
punto.print_coord()
