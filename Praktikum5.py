#Task 1
class Fraction:
    def __new__(cls, numerator, denominator):
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю.")
        instance = super().__new__(cls)
        instance.numerator = numerator
        instance.denominator = denominator
        instance._simplify()
        return instance

    def _simplify(self):
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)
        common_divisor = gcd(abs(self.numerator), abs(self.denominator))
        self.numerator //= common_divisor
        self.denominator //= common_divisor
        if self.denominator < 0:
            self.numerator, self.denominator = -self.numerator, -self.denominator

    @property
    def value(self):
        return round(self.numerator / self.denominator, 3)

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Можно складывать только объекты типа Fraction.")
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Можно вычитать только объекты типа Fraction.")
        return Fraction(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Можно умножать только объекты типа Fraction.")
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Можно делить только объекты типа Fraction.")
        if other.numerator == 0:
            raise ZeroDivisionError("Нельзя делить на ноль.")
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    @classmethod
    def from_string(cls, fraction_str):
        numerator, denominator = map(int, fraction_str.split('/'))
        return cls(numerator, denominator)

    @staticmethod
    def is_fraction(obj):
        return isinstance(obj, Fraction)

# Пример:
f1 = Fraction(1, 2)
f2 = Fraction(3, 4)
print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)
print(f1.value)

#Task 2(с матрицами)
from fractions import Fraction

class FractionMatrix:
    def __new__(cls, matrix):
        if not all(isinstance(row, list) and len(row) == len(matrix[0]) for row in matrix):
            raise ValueError("Все строки матрицы должны быть списками одинаковой длины")
        if not all(isinstance(item, Fraction) for row in matrix for item in row):
            raise ValueError("Все элементы матрицы должны быть дробями (Fraction)")
        instance = super(FractionMatrix, cls).__new__(cls)
        instance.matrix = matrix
        instance.rows = len(matrix)
        instance.cols = len(matrix[0]) if matrix else 0
        return instance

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны иметь одинаковые размерности для сложения")
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return FractionMatrix(result)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны иметь одинаковые размерности для вычитания")
        result = [[self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return FractionMatrix(result)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы")
        result = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
        return FractionMatrix(result)

    def transpose(self):
        result = [[self.matrix[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return FractionMatrix(result)

    @property
    def determinant(self):
        if self.rows != self.cols:
            raise ValueError("Определитель можно вычислить только для квадратных матриц")
        if self.rows == 1:
            return self.matrix[0][0]
        if self.rows == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        det = Fraction(0)
        for c in range(self.cols):
            sub_matrix = [row[:c] + row[c+1:] for row in self.matrix[1:]]
            sub_det = FractionMatrix(sub_matrix).determinant
            det += ((-1) ** c) * self.matrix[0][c] * sub_det
        return det

    def __str__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.matrix])

    @classmethod
    def identity(cls, size):
        matrix = [[Fraction(int(i == j)) for i in range(size)] for j in range(size)]
        return cls(matrix)

    @staticmethod
    def is_square(matrix):
        return matrix.rows == matrix.cols

# Пример:
m1 = FractionMatrix([[Fraction(1, 2), Fraction(1, 3)], [Fraction(2, 5), Fraction(3, 4)]])
m2 = FractionMatrix([[Fraction(1, 3), Fraction(2, 3)], [Fraction(1, 2), Fraction(2, 5)]])
print("Сложение матриц:")
print(m1 + m2)
print("Умножение матриц:")
print(m1 * m2)
print("Определитель матрицы m1:")
print(m1.determinant)
print("Транспонированная матрица m1:")
print(m1.transpose())