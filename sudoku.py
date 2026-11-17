def esCuadrada(matriz):
    return len(matriz[0]) == len(matriz)




if __name__ == '__main__':
    # Test Cases:
    assert esCuadrada ([[1, 2, 3],
                        [2, 3, 1],
                        [3, 1, 2]]) is True
    
    assert esCuadrada ([[1, 2, 3],
                        [2, 3, 1],
                        [3, 1, 2],
                        [2, 4, 6]]) is False