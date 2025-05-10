# Algoritmo de Ordenamiento Burbuja
def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Algoritmo de Ordenamiento por Inserción
def ordenamiento_insercion(lista):
    for i in range(1, len(lista)):
        valor_actual = lista[i]
        posicion = i

        while posicion > 0 and lista[posicion-1] > valor_actual:
            lista[posicion] = lista[posicion-1]
            posicion -= 1

        lista[posicion] = valor_actual
    return lista


def calcular_cambio(montoVuelto, billetes):
    print("\nCambio necesario:")
    for valor in billetes:
        cantidad = int(montoVuelto // valor)
        if cantidad > 0:
            print(str(cantidad) + " de S/ " + str(valor))
            montoVuelto -= (cantidad * valor)
            montoVuelto = round(montoVuelto, 2)

if __name__ == '__main__':
    print("--- Ordenamiento Burbuja ---")
    lista_burbuja = [34, 23, 12, 45, 9, 1, 24]
    print("Lista original:", lista_burbuja)
    print("Lista ordenada:", ordenamiento_burbuja(lista_burbuja.copy()))

    print("\n--- Ordenamiento Inserción ---")
    lista_insercion = [34, 23, 12, 45, 9, 1, 24]
    print("Lista original:", lista_insercion)
    print("Lista ordenada:", ordenamiento_insercion(lista_insercion.copy()))

    print("\n--- Problema del Vuelto ---")
    billetesDisponibles = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05]
    montoVuelto = float(input("Ingrese el monto del vuelto: "))
    calcular_cambio(montoVuelto, billetesDisponibles)
