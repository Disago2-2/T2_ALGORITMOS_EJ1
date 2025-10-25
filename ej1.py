import random

def generar_palabra():
    palabra = ''
    for _ in range(4):
        letra = chr(random.randint(97, 122)) 
        palabra += letra
    return palabra


def generar_matriz(n):
    matriz = []
    for _ in range(n):
        fila = [generar_palabra() for _ in range(n)]
        matriz.append(fila)
    return matriz


def tiene_vocal(palabra):
    for vocal in "aeiou":
        if vocal in palabra:
            return True
    return False


def contar_vocales_matriz(matriz):
    
    if len(matriz) == 1:
        return contar_vocales_fila(matriz[0])
    
    
    mitad = len(matriz) // 2
    superior = matriz[:mitad]
    inferior = matriz[mitad:]
    
    
    return contar_vocales_matriz(superior) + contar_vocales_matriz(inferior)


def contar_vocales_fila(fila):
    
    if len(fila) == 1:
        return 1 if tiene_vocal(fila[0]) else 0
    
    
    mitad = len(fila) // 2
    izquierda = fila[:mitad]
    derecha = fila[mitad:]
    
    return contar_vocales_fila(izquierda) + contar_vocales_fila(derecha)


# Programa principal
def main():
    n = int(input("Ingrese el tamaño de la matriz cuadrada: "))
    matriz = generar_matriz(n)
    
    print("\nMatriz generada:")
    for fila in matriz:
        print(fila)
    
    total_con_vocal = contar_vocales_matriz(matriz)
    print(f"\nTotal de palabras con al menos una vocal: {total_con_vocal}")


main()
