class Torres:
    def __init__(self, n):#constructor que recibe un número n que representa el número de discos en la torre inicial.
        self.n = n
        self.torre1 = list(range(n, 0, -1))
        self.torre2 = []
        self.torre3 = []

    def mover_disco(self, origen, destino):#sacar el disco superior de la torre de origen y añadirlo a la torre de destino.
        disco = origen.pop()
        destino.append(disco)

    def resolver(self):#imprime el estado actual de las torres
        print("Torre 1:", self.torre1)
        print("Torre 2:", self.torre2)
        print("Torre 3:", self.torre3)
        self._resolver(self.n, self.torre1, self.torre2, self.torre3)#llama a la función recursiva _resolver

    def _resolver(self, n, origen, auxiliar, destino):
        if n == 1:#solo haya un disco en la torre de origen, se mueve directamente a la torre de destino y se imprime el movimiento
            self.mover_disco(origen, destino)
            print("Mover disco de torre", origen, "a torre", destino)
            print("Torre 1:", self.torre1)
            print("Torre 2:", self.torre2)
            print("Torre 3:", self.torre3)
        else:
            self._resolver(n-1, origen, destino, auxiliar)# llama recursivamente a _resolver para mover los n-1 discos superiores de la torre de origen a la torre auxiliar
            self.mover_disco(origen, destino)#se mueve el disco inferior a la torre de destino 
            print("Mover disco de torre", origen, "a torre", destino)
            print("Torre 1:", self.torre1)
            print("Torre 2:", self.torre2)
            print("Torre 3:", self.torre3)
            self._resolver(n-1, auxiliar, origen, destino)#vuelve a llamar a _resolver para mover los discos de la torre auxiliar a la torre de destino.