class Matrix(object):
    def __init__(self, f, g):
        self.a1 = float(f[0])
        self.a2 = float(f[1])
        self.a3 = float(g[0])
        self.a4 = float(g[1])

    def __str__(self):
        return "[%f  %f] \n[%f  %f]" % (self.a1, self.a2, self.a3, self.a4)

    def __rmul__(self, s):
        return Matrix([self.a1*s, self.a2*s], [self.a3*s, self.a4*s])

    def __add__(self, other):
        return Matrix([self.a1 + other.a1, self.a2 + other.a2], [self.a3 + other.a3, self.a4 + other.a4])

    def __sub__(self, other):
         return Matrix([self.a1 - other.a1, self.a2 - other.a2], [self.a3 - other.a3, self.a4 - other.a4])

    def determinant(self):
        return (self.a1 * self.a4) - (self.a2 * self.a3)

    def trace(self):
        return self.a1 + self.a4

    def inverse(self):
        d = self.determinant()
        if d == 0:
            return "The matrix is singular."
        else:
            return Matrix([self.a4/d, self.a2/(-d)], [self.a3/(-d), self.a1/d])

    def characteristic_polynomial(self):
        d = self.determinant()
        t = self.trace()
        return "x^2-%f*x+%f" % (t, d)

    def matrix_product(self, other):
        b1 = self.a1 * other.a1 + self.a2 * other.a3
        b2 = self.a1 * other.a2 + self.a2 * other.a4
        b3 = self.a3 * other.a1 + self.a4 * other.a3
        b4 = self.a3 * other.a2 + self.a4 * other.a4
        return Matrix([b1, b2], [b3, b4])
