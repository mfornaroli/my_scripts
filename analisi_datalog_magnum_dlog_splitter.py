from os import listdir
from os.path import isfile, join

logs_directory = r"C:\Users\Mfornaroli\Documents\My Received Files"
files_in_directory = [f for f in listdir(logs_directory) if isfile(join(logs_directory, f))]
datalog_vector = [x for x in files_in_directory if x.endswith(".txt")]

for datalog_under_analysis in datalog_vector:
    with open("C:/Users/Mfornaroli/Documents/My Received Files/" + datalog_under_analysis, "r") as f:
        dlog_content_string = f.readlines()
    dlog_content_string = [x.strip() for x in dlog_content_string]     # contiene tutto cio' che ci serve, riga = stringa
    dlog_content_list = ["fake_line"]*len(dlog_content_string)   # definizione della lista

    print(len(dlog_content_list)) # contiene testo stringa per stringa
    print(len(dlog_content_string)) # fittizio...

    for line in range(len(dlog_content_string)):
        dlog_content_list[line] = dlog_content_string[line].split()
    dlog_content_list = [x for x in dlog_content_list if x != []]   # contiene tutto cio che ci serve ! spezzettato
    print(dlog_content_list)

    print(dlog_content_list)          # contiene testo parola per parola
    print(len(dlog_content_list)) # contiene testo stringa per stringa
    print(len(dlog_content_string))

    lenght = len(dlog_content_list)
    for line in range(0, lenght):
        # print(line)
        # print(dlog_content_string[line])
        # print(dlog_content_list[line])
        if len(dlog_content_list[line]) <= 2:
            dlog_content_list[line] = dlog_content_list[line] * 10
    #
    test_start_counter = 0
    test_start_lines = []
    # print(range(len(dlog_content_list)))
    # print(len(dlog_content_list))
    # print(len(dlog_content_string))
    for line in range(0, len(dlog_content_string)):
        if "tb_Continuity_1" in dlog_content_string[line]:
            test_start_counter += 1
            test_start_lines = test_start_lines + [line]
    print("there are ", test_start_counter, "dummy in this datalog", datalog_under_analysis)

    for temp in range(1,test_start_counter+1):
        print("creiamo il datalog splittato numero: ", temp)
        with open("C:/Users/Mfornaroli/Documents/My Received Files/" + "datalog_splittato_" + str(temp) + "_" + datalog_under_analysis, "w") as f:
            if temp != test_start_counter:
                for line in range(test_start_lines[temp-1], test_start_lines[temp]):
                    f.write(dlog_content_string[line])
                    f.write("\n")
            if temp == test_start_counter:
                for line in range(test_start_lines[temp-1], len(dlog_content_string)):
                    f.write(dlog_content_string[line])
                    f.write("\n")

    # if test_start_counter > 1:
    #     with open("C:/Users/Mfornaroli/Desktop/cartella temp/datalog_magnum/" + datalog_under_analysis, "w") as f:
    #         f.write("questo file di testo non ci serve piu'. balza zio!")
