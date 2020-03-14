import os
from os import listdir
from os.path import isfile, join
list_of_metha_names = []
all_directories = [x[0] for x in os.walk(r'C:\Users\Mfornaroli\Desktop\datalog_from_ax6\prova_script')]
print(all_directories)

print('lets begin!')
session_number = []
session_time = []

for i in range(len(all_directories)):
    clean_directory = all_directories[i].replace('\\', '/')
    print(clean_directory, i)
    if len(os.listdir(clean_directory)) != 0:
        files_in_directory = [f for f in listdir(clean_directory) if isfile(join(clean_directory, f))]
        print(files_in_directory)
        for i in range(len(files_in_directory)):
            print(files_in_directory[i].split('_')[1])
            print(files_in_directory[i].split('_')[-1][0:6])
            if files_in_directory[i].split('_')[1] not in session_number:
                session_number.append(files_in_directory[i].split('_')[1])
                session_time.append(files_in_directory[i].split('_')[-1][0:6])
            elif files_in_directory[i].split('_')[1] in session_number and files_in_directory[i].split('_')[-1][0:6] not in session_time:
                session_number.append(files_in_directory[i].split('_')[1])
                session_time.append(files_in_directory[i].split('_')[-1][0:6])

            print(len(session_number))
            print((session_time))
            vs_number_temp = files_in_directory[i].split('_')[1]
            vs_time_temp = files_in_directory[i].split('_')[-1][0:6]

print(session_number)
print(session_time)

for i in range(len(session_number)):
    path_2 = r'C:\Users\Mfornaroli\Desktop'
    stringa_temp = session_number[i] + '_' + session_time[i]
    print(stringa_temp)
    string_to_be_used_3 = 'mkdir' + ' ' + path_2 + '\\' + stringa_temp
    os.system(string_to_be_used_3)
for k in range(len(session_time)):
    for i in range(len(all_directories)):
        clean_directory = all_directories[i].replace('\\', '/')
        print(clean_directory, i)
        if len(os.listdir(clean_directory)) != 0:
            files_in_directory = [f for f in listdir(clean_directory) if isfile(join(clean_directory, f))]
            print(files_in_directory)
            for j in range(len(files_in_directory)):
                if files_in_directory[j].split('_')[1] == session_number[k] and files_in_directory[j].split('_')[-1][0:6] == session_time[k]:
                    print("e qui mettiamo il comando di copy")
                    directory_to_be_copied_to = r'C:\Users\Mfornaroli\Desktop' + '\\' + session_number[k] + '_' + session_time[k]
                    string_to_be_used_4 = 'copy' + ' ' + clean_directory + '/' + files_in_directory[j] + ' ' + directory_to_be_copied_to
                    string_to_be_used_4 = string_to_be_used_4.replace('/', '\\')
                    print(string_to_be_used_4)
                    os.system(string_to_be_used_4)






# for i in range(len(all_directories)):
#     metha_name = metha_directories[i][-14::].replace('\\', '')
#     print('now we analyse: ', metha_name)
#     list_of_metha_names.append(metha_name)
#     clean_directory_1 = metha_directories[i].replace('\\', '/')
#     clean_directory_2 = clean_directory_1.replace('//', '/')
#     if len(os.listdir(clean_directory_2)) != 0:
#         clean_UM_log_directory = clean_directory_2 + '/FlowLOG'
#         files_in_directory = [f for f in listdir(clean_UM_log_directory) if isfile(join(clean_UM_log_directory, f))]
#
#         UM_datalog_vector = [x for x in files_in_directory if 'QUAL_UM' in x]
#         Post_ops_vector = [x for x in files_in_directory if 'PostTestOperations' in x]
#         pre_test_ops_vector = [x for x in files_in_directory if 'PreTestOperations' in x]