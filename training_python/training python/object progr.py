# classi di solito vanno con la maiuscola.
class Poly(object):
    def __init__(self, coeff):
        self.coeff = coeff
        print("oggetto Poly, con coefficienti: ", self.coeff)
    def eval(self, x):
        risultato = 0
        for c in reversed(self.coeff):
            risultato = c + risultato*x
        return risultato
    def derive(self):
        risultato = []
        for c,i in enumerate(self.coeff):
            risultato.append(c*i)
        return Poly(tuple(risultato[1:]))


p = Poly((4,3,2))
print(p.eval(10))
derivata = p.derive()
print(p.derive().eval(10))
print(derivata.eval(10))


"""
class decorators... 

"""