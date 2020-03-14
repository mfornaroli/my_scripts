
from os import listdir
from os.path import isfile, join
from tkinter.filedialog import askopenfilename
# DRB... the following are found always before possible FAIL, so... no need to fix the fail issue for now.
things_to_measure = [
                     "tb_Idd_stby_36_195_x1",
                     "tb_Iddq_Stby_36_195_x1",
                     "tb_Idd_stby_36_195_x8",
                     "tb_Iddq_Stby_36_195_x8",
                     "tb_Idd_trans_33_18",
                     "tb_Iddq_trans_33_18"
                     ]
# to add for AQLY FLOW analysis / there's a difference in the datalog, for these tb
things_to_measure_2 = [
                     "tb_IddR_x1_27_17_20",
                     "tb_IddqR_x1_27_17_20",
                     "tb_IddR_x1_36_195_20",
                     "tb_IddqR_x1_36_195_20",
                     "tb_IddR_x4_36_195_26",
                     "tb_IddqR_x4_36_195_26",
                     "tb_IddR_x4_36_195_52",
                     "tb_IddqR_x4_36_195_52",
                     "tb_IddR_x4_36_195_200",
                     "tb_IddqR_x4_36_195_200",
                     "tb_IddR_x8_36_195_26",
                     "tb_IddqR_x8_36_195_26",
                     "tb_IddR_x8_36_195_52",
                     "tb_IddqR_x8_36_195_52",
                     "tb_IddR_x8_36_195_200",
                     "tb_IddqR_x8_36_195_200",
                     ]

# print("\n    select a datalog from which you want to analyze data... ")
# filename = askopenfilename()
# print(filename)
#
# logs_directory = input("     \n     copia incollami sta directory,  zio! :")

logs_directory = "C:/Users/Mfornaroli/Desktop/cartella_temp/datalog_magnum"
files_in_directory = [f for f in listdir(logs_directory) if isfile(join(logs_directory, f))]
datalog_vector = [x for x in files_in_directory if x.endswith(".txt")]

dut_finder_string_vector = ['1', '2', '3', '4', '5', '6', '7', '8']
results_dictionary = {}
file_counter = 1
for datalog_under_analysis in datalog_vector:
    # define temporary variables that we need for each loop
    temp_measure_results = [[], [], [], [], [], [], [], []]
    vector_nand0_dut = ['NAND_0(Dut_1)', 'NAND_0(Dut_2)', 'NAND_0(Dut_3)', 'NAND_0(Dut_4)', 'NAND_0(Dut_5)','NAND_0(Dut_6)', 'NAND_0(Dut_7)', 'NAND_0(Dut_8)']
    units_in_dlog_counter = 0
    fid_dictionary = {'Dut 1': [], "Dut 2": [], 'Dut 3': [], "Dut 4": [], 'Dut 5': [], "Dut 6": [], 'Dut 7': [],'Dut 8': []}
    dut_presence_vector = [0, 0, 0, 0, 0, 0, 0, 0]
    print("we are analysing datalog", file_counter, datalog_under_analysis)
    fname = "C:/Users/Mfornaroli/Desktop/cartella_temp/datalog_magnum/" + datalog_under_analysis
    # import datalog, store it as a list of lists, remove empty lines
    with open(fname) as f:
        dlog_content = f.readlines()
    dlog_content = [x.strip() for x in dlog_content]
    for line in range(len(dlog_content)):
        dlog_content[line] = dlog_content[line].split()
    dlog_content = [x for x in dlog_content if x != []]
    # making sure each list of list line is "long" enough... ugly trick to make things work
    for line in range(len(dlog_content)):
        if len(dlog_content[line])<=2:
            dlog_content[line] = dlog_content[line]*10

    # checking the fids of present units and putting them in a dictionary which links them to the DUT they're in...
    dut_index = 1
    for nand0_dut in vector_nand0_dut:
        for line in range(len(dlog_content)):
             if dlog_content[line][0]== nand0_dut:
                 fid_dictionary["Dut " + str(dut_index)] = dlog_content[line][-3::]
                 units_in_dlog_counter += 1
                 dut_presence_vector[dut_index - 1] = 1
                 break
             else:
                 fid_dictionary["Dut " + str(dut_index)] = ["absent"]
        dut_index+=1
    # at this point we have a dictionary associating each dut to a certain FID
    number_of_duts = sum(dut_presence_vector)
    print("number of units in this datalog: ", number_of_duts)
    print(fid_dictionary)
    print(dut_presence_vector)
    temp_res_index = 0
    for dut_number_minus_one in range(0,8):
        if dut_presence_vector[dut_number_minus_one] == 1:
            temp_measure_results[temp_res_index] = fid_dictionary["Dut " + str(dut_number_minus_one + 1)]
            temp_res_index += 1
    # temp measure results gia contiene i fid in ordine di dut...
    for thing_to_measure in things_to_measure:
        print("looking for: ", thing_to_measure)
        for line in range(len(dlog_content)):
            if thing_to_measure in dlog_content[line][2]:
                print("just found ", thing_to_measure)
                for i in range(0,number_of_duts):      # PER OGNI RIGA IN CUI TROVIAMO IL NOSTRO DATO ...
                  # print('lista di liste creata fino ad ora per questo fid:',temp_measure_results[i])
                  # print("riga a cui abbiamo beccato testblock che ci interessa: ", line)
                  # print("the index of the dut we're taking the results of is: ", i)
                  # print("lunghezza della riga a cui andiamo a pescare il dato: ", len(dlog_content[line + 3 + (i*2)][8]))
                  # print("nuova misura da aggiungere alla riga: ",[thing_to_measure, dlog_content[line + 3 + (i*2)][8]])
                  print("riga prima del dato: ", dlog_content[line + 2 + (i * 2)])
                  print("riga da cui andiamo a prendere il dato: ", dlog_content[line + 3 + (i * 2)])
                  # print("\n")
                  temp_measure_results[i] = temp_measure_results[i] + [thing_to_measure, dlog_content[line + 3 + (i*2)][8]] + [dlog_content[line+3+(i*2)][9]]
                break

    # iniziamo a mettere qui le modifiche, cosi possiamo verificare se funzionano
    for thing_to_measure in things_to_measure_2:
        print("looking for: ", thing_to_measure)
        for line in range(len(dlog_content)):
            if thing_to_measure in dlog_content[line][2]:
                print("just found ", thing_to_measure)
                for i in range(0,number_of_duts):
                  # print('lista di liste creata fino ad ora per questo fid:',temp_measure_results[i])
                  # print("riga a cui abbiamo beccato testblock che ci interessa: ", line)
                  # print("the index of the dut we're taking the results of is: ", i)
                  # print("lunghezza della riga a cui andiamo a pescare il dato: ", len(dlog_content[line + 2 + (i*2)][8]))
                    print("la riga prima... del dato: ", dlog_content[line + 1 + (i*2)])
                    print("il dut: ", dlog_content[line + 1 + (i * 2)][1])
                    dut_measured_now = dlog_content[line + 1 + (i * 2)][1]
                    if dut_measured_now in dut_finder_string_vector:
                        print("fid associato al dut: ", fid_dictionary["Dut " + str(dut_measured_now)])
                        fid_nel_dut = fid_dictionary["Dut " + str(dut_measured_now)]
                        for temp_index_meas_results in range(0,number_of_duts):
                            print(" let's see if we find this fid: ", fid_nel_dut)
                            print("sara' forse uguale a questo fid? ", temp_measure_results[temp_index_meas_results][0:3])
                            if temp_measure_results[temp_index_meas_results][0] == fid_nel_dut[0] and temp_measure_results[temp_index_meas_results][1] == fid_nel_dut[1] and temp_measure_results[temp_index_meas_results][2] == fid_nel_dut[2]:
                                print("si, sono uguali!")
                                temp_measure_results[temp_index_meas_results] = temp_measure_results[temp_index_meas_results] + [thing_to_measure,dlog_content[line + 2 + (i * 2)][8]] + [dlog_content[line + 2 + (i * 2)][9]]
                    if dut_measured_now not in dut_finder_string_vector:
                        # temp_measure_results[temp_index_meas_results] = temp_measure_results[temp_index_meas_results] + [thing_to_measure,"none"] + ["none"]
                        break
                    print("riga da cui andiamo a prendere il dato: ",  dlog_content[line + 2 + (i*2)])
                  # print("nuova misura da aggiungere alla riga: ",[thing_to_measure, dlog_content[line + 2 + (i*2)][8]])
                  # print("\n")
                break

    results_dictionary["Datalog{0}".format(file_counter)]=temp_measure_results
    file_counter +=1


for i in range(len(datalog_vector)):
    list_of_lists = results_dictionary["Datalog" + str(i+1)]
    with open(logs_directory + "/output_analysis.txt", "a+") as myfile:
        # myfile.write("Datalog" + str(i+1) + "\n")
        myfile.write('\n'.join(['\t'.join([str(cell) for cell in row]) for row in list_of_lists]))
        myfile.write("\n")
    myfile.close()


