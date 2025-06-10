# Función Merge Sort para ordenar la lista
def merge_sort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        merge_sort(izquierda)
        merge_sort(derecha)

        # Intercalando listas ordenadas
        i = j = k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

# Función para realizar búsqueda binaria en una lista ordenada
def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# Programa principal
if __name__ == "__main__":
    # Entrada del usuario
    numeros = input("Ingrese una lista de números separados por coma: ")
    lista = list(map(int, numeros.split(",")))

    # Ordenar la lista usando Merge Sort
    merge_sort(lista)
    print(f"Lista ordenada: {lista}")

    # Buscar un número específico
    objetivo = int(input("Ingrese el número que desea buscar: "))
    resultado = busqueda_binaria(lista, objetivo)

    if resultado != -1:
        print(f"El número {objetivo} se encuentra en la posición {resultado} de la lista ordenada.")
    else:
        print(f"El número {objetivo} no se encuentra en la lista.")