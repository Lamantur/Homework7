

class Matrix:
    def __init__(self, matr) -> None:

        self.matr: list = matr

    def __str__(self) -> str:
        return ('\n'.join('\t'.join(map(str, row)) for row in self.matr))

    def __add__(self, other):
        result: list = []
        result = [[self.matr[i][j] + other.matr[i][j] for j in range
                   (len(self.matr[0]))] for i in range(len(self.matr))]
        return ('\n'.join('\t'.join(map(str, row)) for row in result))


M1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
M2 = Matrix([[0, 2, 1], [4, 1, 2], [1, 1, 1]])
print("______M1____________")
print(M1)
print("______M2____________")
print(M2)
print("______M1+M2_________")
print(M1+M2)
