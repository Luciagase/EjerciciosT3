class Nave:
    def __init__(self,nombre,largo,trip,cant_pas):
        self.nombre= nombre
        self.largo= largo
        self.trip= trip
        self.cant_pas= cant_pas
    
    def __str__(self):
        info ="Nave:"+ self.nombre
        info += ",largo"+ str(self.largo)
        info += ",tripulación:" + str(self.trip)
        info += ",cantidad de pasajeros:" + str(self.trip)
        return info 

def merge_sort_nombre(collection: list) -> list:
    def merge(left: list, right: list) -> list:
        def _merge():
            while left and right:
                yield (left if left[0].nombre <= right[0].nombre else right).pop(0)
            yield from left
            yield from right

        return list(_merge())

    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    return merge(merge_sort_nombre(collection[:mid]), merge_sort_nombre(collection[mid:]))

def merge_sort_cant_pas(collection: list) -> list:
    def merge(left: list, right: list) -> list:
        def _merge():
            while left and right:
                yield (left if left[0].cant_pas <= right[0].cant_pas else right).pop(0)
            yield from left
            yield from right

        return list(_merge())

    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    return merge(merge_sort_nombre(collection[:mid]), merge_sort_nombre(collection[mid:]))

def binary_search_por_nombre(sorted_collection: list[Nave], item: str):
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        midpoint = left + (right - left) // 2
        current_item = sorted_collection[midpoint]
        if current_item.nombre == item:
            return midpoint
        elif item < current_item.nombre:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return None

def busca_nave_por_nombre(lista,nombre_b):
    print('\nse busca la nave con "'+ nombre_b + '":')
    pos=binary_search_por_nombre(lista,nombre_b)
    return lista [pos]

def main():
    #lista de naves
    lista_naves = []
    lista_naves.append(Nave("Halcón Milenario", 200, 7, 20))
    lista_naves.append(Nave("Estrella de la Muerte", 2000, 50, 5000))
    lista_naves.append(Nave("cohete", 300, 72, 240))
    lista_naves.append(Nave("avion ", 20, 3, 2))
    lista_naves.append(Nave("helicóptero", 30, 9, 10))
    lista_naves.append(Nave("caza ", 10, 4, 5))
    
    #ordenar las naves por nombre
    lista_naves_ord=merge_sort_nombre(lista_naves)
    #mostrar los nombres de las naves ordenadas
    for i in lista_naves_ord:
        print(i)
    #buscar la nave "Halcón Milenario"
    print(busca_nave_por_nombre(lista_naves_ord,"Halcón Milenario"))
    #buscar la nave "Estrella de la Muerte"
    print(busca_nave_por_nombre(lista_naves_ord,"Estrella de la Muerte"))

    lista_naves_ord_cant_pas=merge_sort_cant_pas(lista_naves)

    print("las cinco primeras naves ordenadas por pasajeros:")
    i=0
    while i<5:
        print(lista_naves_ord_cant_pas[i])
        i+=1
    
if __name__=="__main__":
    main()
