print("ciao")
print("mamma\n")

age = 10
if age < 5:
    print("too little!")
elif 5<= age <= 15:
    print("ok!")
else:
    print("too old dude")

for fruit in ['apple', 'banana', 'watermelon']:
    print("i like ", fruit)

print("\n")

d = {"name": "michele", "cognome" : "er_forna", "eta'":"25"}

for k in d:
    print(k)
for k in d:
    print("chiave = %s, valore = %s"  %(k, d[k]))

print("\n")
print(list(d.items()))

print("\n")
for x in d.items():
    print(x)
print("\n")
for x,y in d.items():
    print(x,y)

print("\n")
print(list(enumerate(["ciao", "mamma","come","va"])))
print("\n")
for indice,valore in enumerate(["ciao", "mamma","come","va"]):
    print("indice = %d valore = %s" %(indice,valore))
print("\n")

# continue, break, pass. useful functions. PASS to be used to replace a block of code which is... yet to be written
def square(x):
    return x*x
print(square(10))

def pippo():
    print("pippo")

# le variabili puoi farle VEDERE a tutte le funzioni, ma non puoi modificarle all'interno della funzione. prova un po' sta cosa ...

# inversion of control ...
# global variable. . . check it out.

def f(x,y,z=0, w=1):
    print("x=%s y=%s z=%s w=%s" %(x,y,z,w))

# asterisco forza l'interprete ad assegnare i valori uno ad uno...

f("a", "b")
f("a", "b", w="c" )
print("\n")
def func(x, *pippo):
    print(x, pippo)

func(1)
func(1,2)
func(1,2,3,4)

print("\n")


def func(x, **pippo):
    print(x, pippo)

func(x=1, y=2)


def func(x, *pluto, **pippo):
    print(x, pluto, pippo)
func(1,2,3,4, y=2)

# functions are also OBJECTS. binding: they can be assigned to some variable.
# binding between object/function and a name. can be put in DATA STRUCTURE.
pippo = print
pippo("hey")

# vedi: funzionamento CLOSURE...