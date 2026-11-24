def esCuadrada(matriz):

    assert isinstance(matriz, list), "la interfaz exige que sudoku debe ser una lista"

    numeroFila = len(matriz)

    for fila in matriz:

        if len(fila) != numeroFila:

            return False
        
    return True

def sonNumerosEnteros (matriz):

    for fila in matriz:

        for numero in fila:

            if not isinstance(numero, int):
                return False
    return True

def numerosEnRango(matriz):

    numerosValidos = range(1, len(matriz) + 1)

    for fila in matriz:

        for numero in fila:

            if numero not in numerosValidos:
                return False

    return True

def checkNumerosValidos(sudoku):

    try:
        isinstance(sudoku, list)
    except TypeError:
        print("el input debe ser una lista")
    return sonNumerosEnteros(sudoku) and numerosEnRango(sudoku)


def checkFilas(sudoku):

    for fila in sudoku:

        posicionNumero = 0

        for numero in fila:

            if numero in fila[posicionNumero + 1:]:
                return False
            
            else:

                posicionNumero += 1

    return True
        

if __name__ == '__main__':
    # Test Cases:
    assert esCuadrada ([[1, 2, 3],
                        [2, 3, 1],
                        [3, 1, 2]]) is True
    
    assert esCuadrada ([[1, 2, 3],
                        [2, 3, 1],
                        [3, 1, 2],
                        [2, 4, 6]]) is False

    assert esCuadrada ([['a', 'b', 'c'],
                        ['b', 'c', 'a'],
                        ['c', 'a', 'b']]) is True
