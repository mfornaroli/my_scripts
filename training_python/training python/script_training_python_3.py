# funzione che simula un ADC
# input: range tensioni su cui ci muoviamo, num di valori discreti (0/n-1 values), valore tensione.
# output: numero intero compreso tra n ed n-1.
# se siamo sopra o sotto >> da come output zero e n - 1.

def adc(minv, maxv, n, vin):
    if vin < minv:
        return 0
    elif vin > maxv:
        return n-1
    step = ( maxv - minv ) / n
    return int((vin - minv )/step)



tensione_massima = 20
tensione_minima = 10
risoluzione = 4

print("iniziamo... ")
print(adc(1, 13, 6, 11))
print(adc(1, 100, 6, 11))
print(adc(4, 33, 100, 11))

print("output %d" % adc(
    tensione_minima,
    tensione_massima,
    risoluzione,
    9))

print("\n")
for tensione in [9, 29, 11.1, 13.2]:
    print("output %d" % adc(
        tensione_minima,
        tensione_massima,
        risoluzione,
        tensione))

# cerchiamo di renderlo piu' efficiente... CASHiamo
# ora: funzione che crei simulatore di adc. togliamo vin dagli input della funzione..
# output >> funzione che accetta in input vin, valore letto della tensione, e da come output le stesse cose di prima. lol
# funzione il cui output e' una funzione, che accetta valori costanti di adc e genera un'altra funzione che accetti solo tensione in ingresso!!


def adc_closure(minv, maxv, n):
    step = (maxv - minv) / n  # e' la cosa che voglio cashare
    def inner(vin):
        if vin < minv:
            return 0
        elif vin > maxv:
             return n-1
        return int((vin - minv )/step)
    return inner   # output e' funzione, tutte variabili di funzione madre, funzione interna se le ricorda)


mio_adc = adc_closure(          # risultato (inner: codice + valori) viene salvato qui. creiamo la funzione che fa il lavoro...
    tensione_minima,
    tensione_massima,
    risoluzione,
)
for tensione in [9, 29, 11.1, 13.2]:
    print("closure: input %.2f output %d" %(tensione, mio_adc(tensione)))



print("\n")
def pippo(x):
    def inner1(y):
        print(x,y)
    def paperino(a,b):
        print(x, a, b)
    return(inner1, paperino)

w,j = pippo("hello")
j("mom", "dad")