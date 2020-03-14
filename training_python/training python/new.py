import os
def elenca(directory, suffisso):
    """
    stampa una lista di files che terminano per .txt
    da directory fornita in input"""
    risultato = []
    for filename in os.listdir(directory):
    # for filename in os.listdir(r"C:\Users\Mfornaroli\Desktop\cartella temp\datalog_magnum"):    # raw string, doesn't interpret!
        if filename[-len(suffisso):] == suffisso:
            print(filename)
            risultato.append(filename)

    return risultato

if __name__ == "__main__":
    print(elenca(r"C:\Users\Mfornaroli\Desktop\cartella_temp\datalog_magnum", "txt"))

