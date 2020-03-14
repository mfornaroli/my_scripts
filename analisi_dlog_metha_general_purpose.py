import os
from os import listdir
from os.path import isfile, join

list_of_metha_names = []

input_string = r"C:\Users\Mfornaroli\Desktop\UM_QUAL_Turquoise" \
               r"\extended last run (up to 90TB and beyond)\
               mfornaroli_20200122_154647_dd21"
all_directories = [x[0] for x in os.walk(input_string)]
print(all_directories)
metha_directories = [y for y in all_directories if y.split('_')[-1] == 'LOGs']
print("there are: ", len(metha_directories), " metha")

for i in range(len(metha_directories)):
    UM_datalog_vector = []
    UM_dlog_PATH = []
    metha_name = metha_directories[i].split('\\')[-1].replace('\\', '')
    list_of_metha_names.append(metha_name)
    clean_directory_1 = metha_directories[i].replace('\\', '/').replace('//', '/')
    if len(os.listdir(clean_directory_1)) != 0:
        clean_UM_log_directory = clean_directory_1 + '/FlowLOG'
        # print('peschiamo da: ', clean_UM_log_directory)
        files_in_directory = [f for f in listdir(clean_UM_log_directory) if isfile(join(clean_UM_log_directory, f))]
        # print(files_in_directory)
#         #UM_datalog_vector = [x for x in files_in_directory if 'PreTestOperations.txt' in x]
#         #UM_datalog_vector = [x for x in files_in_directory if 'QUAL_UM.txt' in x]
        UM_datalog_vector = [x for x in files_in_directory if 'RV_Endurance_CQ_M2.txt' in x]
#         UM_datalog_vector = [x for x in files_in_directory if 'PostTestOperations.txt' in x]
        # print(UM_datalog_vector)
        # print("BINGO", metha_name)
        # print(UM_datalog_vector)

        for j in range(len(UM_datalog_vector)):
            UM_dlog_PATH.append(clean_UM_log_directory + '/' + UM_datalog_vector[j])
        for datalog_under_analysis in UM_dlog_PATH:
            with open(datalog_under_analysis, "r") as f:
                # print(metha_name,'peschiamo dal datalog: ', datalog_under_analysis)
                dlog_content = f.readlines()
                dlog_content_list = [x.strip() for x in dlog_content]  # contiene tutto cio' che ci serve, riga = stringa
                for dlog_line in dlog_content_list[::-1]:  # all the stats that you want here!
                    # if 'loop_UM' in dlog_line:
                    # if 'ProductSerialNumber' in dlog_line:
                    # if 'WrittenData100MBSize       ' in dlog_line:
                    # if 'Detected Panic Logs: ' in dlog_line:
                    if 'CTRL Temp' in dlog_line:
                        # print( metha_name,'/' , dlog_line)
                        print(dlog_line)
                        # print(UM_dlog_PATH)
                        # break


