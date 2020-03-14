"""
map function: livello di astrazione superiore. mappa tutti i valori di iterabile e li associa a funzione, e ritorna iterabile.
filter function: GUARDALA TU...
"""
def square(x):
    return x*x
list(map(square, [1,2,3,4,5]))
print(list(map(square, [1, 2, 3, 4, 5])))

def is_mp3(filename):
    return filename[-4:]== ".mp3"
print(is_mp3("pippo"))
print(is_mp3("pippo.mp3"))
