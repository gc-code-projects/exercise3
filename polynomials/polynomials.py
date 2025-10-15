from numbers import Number


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a - b for a, b in zip(self.coefficients,
                                                other.coefficients))
            if self.degree() == common - 1:
                coefs += tuple(-i for i in other.coefficients[common:])
            else:
                coefs += self.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] - other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __rsub__(self, other):
        return Polynomial(tuple(-i for i in (self - other).coefficients))

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            degree_sum = self.degree() + other.degree() + 1
            coefs = [0] * degree_sum
            for i in range(self.degree() + 1):
                for j in range(other.degree() + 1):
                    coefs[i + j] += self.coefficients[i] * other.coefficients[j]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial(tuple(i * other for i in self.coefficients))

        else:
            return NotImplemented

    def __rmul__(self, other):
        return Polynomial(tuple(i * other for i in self.coefficients))

    def __pow__(self, expo):
        if isinstance(expo, Integral) and expo > 0:
            ret = Polynomial((self.coefficients))
            for i in range(1, expo):
                ret *= self
            return ret
        else:
            return NotImplemented

    def __call__(self, x):
        ret = 0
        for i, c in enumerate(self.coefficients):
            ret += c * x ** i
        return ret

