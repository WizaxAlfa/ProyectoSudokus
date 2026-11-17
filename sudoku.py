def esCuadrada(matriz):
    assert isinstance(matriz, list), "la interfaz exige que sudoku debe ser una lista"
    for check in matriz:
        if len(check) != len(matriz):
            return False
        return True






if __name__ == '__main__':
    # Test Cases:
    assert esCuadrada ([[1, 2, 3],
                        [2, 3, 1, 4],
                        [3, 1, 2]]) is True
    
    assert esCuadrada ([[1, 2, 3],
                        [2, 3, 1],
                        [3, 1, 2],
                        [2, 4, 6]]) is False

    assert esCuadrada ([['a', 'b', 'c'],
                        ['b', 'c', 'a'],
                        ['c', 'a', 'b']]) is True
