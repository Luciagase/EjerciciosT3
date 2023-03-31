#Iterativo

def determinanteSarrus(matriz):
    if len(matriz) != 3:
        print("No es de 3x3")
        return
    det = matriz[0][0]*matriz[1][1]*matriz[2][2] + matriz[0][1]*matriz[1][2]*matriz[2][0] + matriz[0][2]*matriz[1][0]*matriz[2][1] - matriz[0][2]*matriz[1][1]*matriz[2][0] - matriz[0][1]*matriz[1][0]*matriz[2][2] - matriz[0][0]*matriz[1][2]*matriz[2][1]
    return det


#Recursivo
def determinanteSarrusRecursivo(matriz):
    if len(matriz) != 3:
        print("No es de 3x3")
        return
    if len(matriz) == 1:
        return matriz[0][0]
    else:
        det = 0
        for i in range(3):
            det += (-1)**i * matriz[0][i] * determinanteSarrusRecursivo([fila[:i] + fila[i+1:] for fila in matriz[1:]])
        return det
    
