class Torres:
    def __init__(self, n):#constructor que recibe un número n que representa el número de discos en la torre inicial.
        self.n = n
        self.torre1 = list(range(n, 0, -1))
        self.torre2 = []
        self.torre3 = []

    def mover_disco(self, origen, destino):#sacar el disco superior de la torre de origen y añadirlo a la torre de destino.
        disco = origen.pop()
        destino.append(disco)