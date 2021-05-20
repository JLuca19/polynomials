from numbers import Number

class Polynomial:
    def __init__(self, coefs):

        self.coefficients = coefs    

    def degree(self):

        return len(self.coefficients) - 1 

    def __str__(self):

        coefs= self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{''if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and \
            self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,) + self.coefficients[1:])

        elif isinstance(other, Polynomial):
            # Work out how many coefficient places the two polynomials have in common.
            common = min(self.degree(), other.degree()) + 1
            # Sum the common coefficient positions.
            coefs = tuple(a + b for a, b in zip(self.coefficients[:common],
                                             other.coefficients[:common]))

            # Append the high degree coefficients from the higher degree summand.
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        else:
            return NotImplemented
    
    def __radd__(self, other):
        return self + other