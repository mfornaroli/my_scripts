import os
print([(x, y,  x*y) for x in range(1,11) for y in range(2,10) if x % 2 == 1 ])

print([f for f in os.listdir(r"C:\Users\Mfornaroli\Desktop\cartella_temp\datalog_magnum") if f[-4:] == ".bat"])
"""
il secondo ciclo for, sulla y, e' dentro quello sulla x 
closure (si portano dietro output di altre funzioni
"""
