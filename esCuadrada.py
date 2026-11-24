def esCuadrada(matriz):

    assert isinstance(matriz, list), "la interfaz exige que sudoku debe ser una lista"

    numeroFila = len(matriz)

    for fila in matriz:

        if len(fila) != numeroFila:

            return False
        
    return True
