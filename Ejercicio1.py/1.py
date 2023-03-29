class Torres:
    def __init__(self, n):#constructor que recibe un número n que representa el número de discos en la torre inicial.
        self.n = n
        self.torre1 = list(range(n, 0, -1))
        self.torre2 = []
        self.torre3 = []
