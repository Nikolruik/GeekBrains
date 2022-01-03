class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(str, self.matrix))

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for n_i in range(len(self.matrix[i])):
                self.matrix[i][n_i] =  self.matrix[i][n_i] + other.matrix[i][n_i]
        return Matrix.__str__(self)


a = Matrix([[1, 3, 5], [43, 32, 21]])
b = Matrix([[1, 3, 5], [43, 32, 21]])
print(a.__add__(b))