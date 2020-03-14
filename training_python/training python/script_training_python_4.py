import os
def elenca():
    """stampa una lista di files che terminano per .txt"""
    # for filename in os.listdir("C:/Users/Mfornaroli/Desktop/cartella_temp/datalog_magnum"):
    for filename in os.listdir(r"C:\Users\Mfornaroli\Desktop\cartella_temp\datalog_magnum"):    # raw string, doesn't interpret!
        if filename[-4:] == ".txt":
            print(filename)

if __name__ == "__main__":
    elenca()

