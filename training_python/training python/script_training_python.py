print("Hello World!!")

# materiale su bitbucket. python training. python language training.
# in un processor: there are bytes (natural e floating point). python: read eval print (loop)
# literals >> stringa con testo. lavora con oggetti. vedremo anche PROGRAMMAZIONE FUNZIONALE.
# testo = seq num interi. print(0xff), print(1+2j)
# oggi, per tradurre tutti gli alfabeti >> UNICODE standard. python 2 non segue unicode. il 3 si. il \n per andare a capo
# gli escape sono gli stessi di C.
# r" RAW STRING. non interpretare gli slash! tipo print(r"ciao\n mamma")
# BOOLEANS True and False con la maiuscola
# (2+3j) * (2-3j) / SOMME: concatenano le STRINGHE... lol
# int/int = floating point. doppio slash: divisione INTERA. 12//5 = 2, % prende il resto.
# not (True or False)
# operators of shortcut
# False and (qualsiasi cosa) sara SEMPRE FALSA, non valuta neanche la seconda parte. True and x restituisce sempre x. False or x restituisce sempre x.
# 0x01 << 1 = 0x02
# containers of data: LIST (1). parenthesis square. neg index starts from end
# list slicing, list[1:6:2] dall'uno al 6, saltando di 2. [::-1} INVERT ORDER.
# TUPLE. IMMUTABLE LIST. object that doesnt want to be changed
# DICTIONARIES. {} PARENTHESIS. dictionary["key"]
# vedi hashtable algorithms. for doing dictionaries. immutable objects have hash value.
# ordine delle chiavi non e' preservato, per questo algoritmo. liste invece preservano ordine
# NON posso usare una lista come CHIAVE. 'unhashable type list', devono essere immutabili !
# "a string %s, an integer %d" % ("abc", 1) FORMAT OPERATORS. PRINTF >> trovi tutto.
# d = {"nome":"michele", "cognome":"fornaroli"} >> r"my name is %(nome)s" %d
# SETS. set1 = set([1,2,3,2,3,1]). 2 in set >> True.


i = 0 # what happens? there's a dictionary with key i, object zero associated
i = 1 # object one linked to i, previous link removed !
b = 'ciao' # same thing in this case.
b = 'mama' # 'ciao' object with no reference, erased from memory...
x=1
x+=1 # object 2 is now linked. we obtain a new link.. objects are immutable.

dir()
dir(__builtins__)
sum([1,2,3])
len((1,2,3))
range(3)        # iterator. object equivalent of iteration.
list(range(3))


