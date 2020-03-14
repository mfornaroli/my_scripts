# prima colonna, da cercare nell'etx. seconda trial nickname, terza description
possibili_etx = [['ArrayTest', 'ARRAYTEST', 'Array Test' ]  ,
                 ['NAND_VERIFICATION_SLC_sticky', 'SLC_cyc_stickyOFF', '-'],
                 ['NAND_VERIFICATION_MLC_sticky', 'MLC_cyc_stickyOFF', '-'],
                 ['NAND_VERIFICATION_SLC',  'SLC_cyc' , '-' ],
                 ['NAND_VERIFICATION_MLC',  'MLC_cyc', '-' ],
                  ['HTDR_MLC', 'NV-HTDR_MLC', 'HTDR MLC Nand Ver' ],
                  ['FO', 'UM_' , 'UM_' ],
                  ['FH1', 'HTOL' , 'HTOL' ],
                  ['FW2', 'FW2_', 'WEAR OUT '],
                  ['FW3', 'FW3_EOL', 'FW3_EOL'],
                  ['AQLD1', 'AQLD1', 'AQLD1'],
                  ['check', 'BCHECK1','BCHECK1'],
                  ['LTDR_MLC' , 'LTDR_MLC', 'LTDR MLC'],
                  ['LTDR_SLC', 'LTDR_SLC', 'LTDR SLC'],
                  ['ERASECOUNT', 'ECOUNT', 'ERASE COUNT READ'],
                  ['CROSSTEMP', 'CROSSTEMP' , 'CROSS TEMP RUN'],
                  ['AQLD2', 'AQLD2', 'AQLD2'],
                  ['EFR', 'UM_EFR', 'EFR'],
                  ['PARTITIONING', 'PARTITIONING', 'PARTITIONING'],
                  ['HTDR_SLC', 'SLC-HTDR', 'SLC HTDR'],
                  ['B2', 'B2', 'B2'],
                  ['PRETEST', 'BCHECK', 'BCHECK'],
                  ['FW1', 'FW1_', 'FW1 WEAR OUT'],
                  # ['FW3', 'FW3', 'FW3'],
                 ]


import os
from os import listdir
from os.path import isfile, join
from tkinter.filedialog import askopenfilename
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

print("\n    select file which ends with fw wave ID..")
filename = askopenfilename()
print(filename)
print("nota: funziona se in directory ci sono programmi etx e un solo .py - temp traveler")

import webbrowser, sys
path_1 = input("     \n     copia incollami sta directory,  zio! :")
# COND1_FOR_SMART = input("    \n     copia incollami sta COND1 per SMART :")    # qui ci sono dadistinguere i due casi...
# COND1_FOR_SMART = filename[-21:-4].replace('_','-')
print(path_1)

# DESIGN_ID = COND1_FOR_SMART[0:4]
# FW_WAVE_ID = COND1_FOR_SMART[-5::]
# uC_DESIGN_ID = COND1_FOR_SMART[5:11]

DESIGN_ID = 'J57X'
FW_WAVE_ID = 'FW007'
COND1_FOR_SMART = 'J57X_PS8226_FW007'
uC_DESIGN_ID = 'PS8226'
#

onlyfiles = [f for f in listdir(path_1) if isfile(join(path_1, f))]
etx_vector = [x for x in onlyfiles if x.endswith(".etx")]
# TEMP_TRAVELER = [x for x in onlyfiles if 'tt_eng'in x]
TEMP_TRAVELER = 'tt_eng_J57X_PS8226_FW004.py'
vettore_trial_description = ["a"]*len(etx_vector)
vettore_trial_nickname=["a"]*len(etx_vector)

inside = False                               # variabile di controllo per sapere se etx i-esimo e' presente gia' nel nostro "archivio"
for i in range(len(etx_vector)):                                                       # con i ci scorriamo tutti gli .etx
    for j in range(len(possibili_etx)):            # con j ci scorriamo, per ogni i, tutti i possibili etx noti...
        if possibili_etx[j][0] in etx_vector[i]:
             vettore_trial_nickname[i] = possibili_etx[j][1]
             vettore_trial_description[i] = possibili_etx[j][2]
             inside = True
             break
        else:
            inside = False
    if inside == False:
        print(etx_vector[i])
        vettore_trial_nickname[i] = input("\n a lui quale trial nickname associamo?\n\n ")
        vettore_trial_description[i] = vettore_trial_nickname[i] + '_1.8'
    is_inside = False

    if "EUDA" in etx_vector[i]:
            vettore_trial_nickname[i] = vettore_trial_nickname[i] + "_EUDA" + '_1.8'
            vettore_trial_description[i] = vettore_trial_description[i] + " SLC" + '_1.8'
    elif "UDA" in etx_vector[i]:
            vettore_trial_nickname[i] = vettore_trial_nickname[i] + "_UDA" + '_1.8'
            vettore_trial_description[i] = vettore_trial_description[i] + " MLC" + '_1.8'
    if "FENH" in etx_vector[i]:
            vettore_trial_nickname[i] = vettore_trial_nickname[i] + "_FENH"
            vettore_trial_description[i] = vettore_trial_description[i] + " FULL SLC" + '_1.8'
    # if "RUN" in etx_vector[i]:
    #         vettore_trial_nickname[i] = vettore_trial_nickname[i] + "_RUN"
    if "RUN" in etx_vector[i]:
            vettore_trial_nickname[i] = vettore_trial_nickname[i] + "_" + etx_vector[i][-8:-4] + '_1.8'
print(etx_vector)
print(vettore_trial_nickname)

# path, dobbiamo trasformare / in \   ....boh, pare che cmq va fatto a mano, porca vacca
from os import path
path_2 = os.path.normpath(path_1)   # PIU O MENO FA QUESTO LAVORO
# webbrowser.open('http://miwvd045:84/WebSoftwareAM.aspx/')


for i in range(len(etx_vector)):

    url = 'http://miwvd045:84/NewSoftware.aspx?EQUIPMENT=Ambyx%205'
    driver = webdriver.Chrome("C:/Users/Mfornaroli/Desktop/script python/chromedriver.exe")
    driver.get(url)

    example_box = driver.find_element_by_id('TextBox1')   # tasto destro, inspect per vedere le id dei vari campi da riempire
    example_box.send_keys(DESIGN_ID)

    example_box = driver.find_element_by_id('TextBox4')   # tasto destro, inspect per vedere le id dei vari campi da riempire
    example_box.send_keys(uC_DESIGN_ID)

    example_box = driver.find_element_by_id('TextBox5')   # tasto destro, inspect per vedere le id dei vari campi da riempire
    example_box.send_keys(FW_WAVE_ID)

    # example_box = driver.find_element_by_id('TextBox6')   # tasto destro, inspect per vedere le id dei vari campi da riempire
    # example_box.send_keys(COND1_FOR_SMART)

    example_box = driver.find_element_by_id('TextBox7')   # tasto destro, inspect per vedere le id dei vari campi da riempire
    example_box.send_keys(vettore_trial_nickname[i])

    example_box = driver.find_element_by_id('TextBox14')   # tasto destro, inspect per vedere le id dei vari campi da riempire
    example_box.send_keys(path_2)

    example_box = driver.find_element_by_id('TextBox15')   # tasto destro, inspect per vedere le id dei vari campi da riempire
    example_box.send_keys(etx_vector[i])

    example_box = driver.find_element_by_id('TextBox8')   # tasto destro, inspect per vedere le id dei vari campi da riempire
    example_box.send_keys(vettore_trial_description[i])

    example_box = driver.find_element_by_id('TextBox16')   # tasto destro, inspect per vedere le id dei vari campi da riempire
    example_box.send_keys(TEMP_TRAVELER)

    input("Press Enter to continue...")
    driver.close()

# SALVARE:
#     example_box = driver.find_element_by_id('button2')   # e' il bottone SAVE
#     example_box.submit()                                                 # CLICK









#
#
