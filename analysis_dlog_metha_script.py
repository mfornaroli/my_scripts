import os
from os import listdir
from os.path import isfile, join
import pandas as pd

list_of_metha_names = ['Metha SN']
list_of_test_results = ['test results']
list_of_fail_loop = ['failing loop']
list_of_fail_details = ['Details']
list_of_cmd13_status = ['cmd13 response']
job_path = r'C:\Users\Mfornaroli\Desktop\UM_QUAL_Turquoise\extended last run (up to 90TB and beyond)\mfornaroli_20200122_154647_dd21'
all_directories = [x[0] for x in os.walk(job_path)]
metha_directories = [y for y in all_directories if y[-4::]== 'LOGs']
print('there are: ', len(metha_directories, ), " metha'")
for i in range(len(metha_directories)):
    if len(list_of_metha_names) == len(list_of_test_results) == len(list_of_fail_details) == len(list_of_cmd13_status) == len(list_of_fail_loop):
        metha_name = metha_directories[i][-14::].replace('\\', '')
        print('now we analyse: ', metha_name)
        list_of_metha_names.append(metha_name)
        clean_directory_1 = metha_directories[i].replace('\\', '/')
        clean_directory_2 = clean_directory_1.replace('//', '/')
        # print("heeeeyyyyyyyyyy", clean_directory_2)
        print(len(os.listdir(clean_directory_2)))
        if len(os.listdir(clean_directory_2)) != 0:
            clean_UM_log_directory = clean_directory_2 + '/FlowLOG'
            files_in_directory = [f for f in listdir(clean_UM_log_directory) if isfile(join(clean_UM_log_directory, f))]
            UM_datalog_vector = [x for x in files_in_directory if 'QUAL_UM' in x]
            finalizeTFD_log_vector = [x for x in files_in_directory if 'FinalizeTFD' in x]
            Post_ops_vector = [x for x in files_in_directory if 'PostTestOperations' in x]
            pre_test_ops = [x for x in files_in_directory if 'PreTestOperations' in x]

            if len(UM_datalog_vector) > 1:    # caso in cui ci sia piu' di un datalog... strano
                if len(finalizeTFD_log_vector)==1:
                    finalizeTFD_PATH = clean_UM_log_directory + '/' + finalizeTFD_log_vector[0]
                    with open(finalizeTFD_PATH, "r") as f:   # questo file non sempre e' attendibile.. occhio.
                        dlog_content = f.readlines()
                        dlog_content_list = [x.strip() for x in dlog_content]  # contiene tutto cio' che ci serve, riga = stringa
                        fail_flag_1 = 0
                        pass_flag_1 = 0
                        for dlog_line in dlog_content_list[::-1]:
                            if 'FAIL' in dlog_line:
                                list_of_test_results.append('FAIL')
                                list_of_fail_loop.append('loop not available')
                                list_of_fail_details.append('more than one dlog ')
                                list_of_cmd13_status.append('more than one dlog')
                                break
                            if 'PASS' in dlog_line:
                                list_of_test_results.append('PASS')
                                list_of_fail_loop.append('loop not available')
                                list_of_fail_details.append('more than one dlog ')
                                list_of_cmd13_status.append('more than one dlog')
                                break
                            if 'Metha Serial' in dlog_line:     # ovvero e' arrivato in pratica a fine dlog
                                list_of_test_results.append('more than one dlog')
                                list_of_fail_loop.append('more than one dlog')
                                list_of_fail_details.append('more than one dlog')
                                list_of_cmd13_status.append('more than one dlog')

                                break
                if len(finalizeTFD_log_vector) == 0:
                    list_of_test_results.append('terminated')
                    list_of_fail_loop.append('terminated')
                    list_of_fail_details.append('terminated')
                    list_of_cmd13_status.append('terminated')
                else:
                    list_of_test_results.append('terminated?')
                    list_of_fail_loop.append('loop not available')
                    list_of_fail_details.append('should be pass')
                    list_of_cmd13_status.append('should be pass')

            elif UM_datalog_vector == []:
                if len(pre_test_ops) == 1:
                    pre_ops_PATH = clean_UM_log_directory + '/' + pre_test_ops[0]
                    print(pre_ops_PATH)
                    with open(pre_ops_PATH, "r") as f:
                        dlog_content = f.readlines()
                        dlog_content_list = [x.strip() for x in dlog_content]
                        fail_prec_flag = 0
                        for dlog_line in dlog_content_list[::-1]:
                            print(dlog_line)
                            if ('TFS Errors:' in dlog_line and fail_prec_flag == 0) or ('| [ActualResponse  :' in dlog_line and fail_prec_flag == 0):
                                print('heeeeeeeeyyyy we have found the line in pre test: see >> ', dlog_line)
                                print(metha_name)
                                list_of_test_results.append('FAIL PREC')
                                list_of_fail_loop.append('pre test')
                                list_of_fail_details.append(dlog_line)
                                list_of_cmd13_status.append('none')
                                fail_prec_flag = 1
                                break
                            if 'Metha PC Name' in dlog_line and fail_prec_flag == 0:
                                list_of_test_results.append('FAIL PREC')
                                list_of_cmd13_status.append('check_the_datalog')
                                list_of_fail_details.append('check_the_datalog')
                                list_of_fail_loop.append('check_the_datalog')
                                print('should this branch be taken? ', metha_name)
                                path_2 = clean_UM_log_directory
                                string_to_be_used_2 = 'start' + ' ' + path_2
                                os.system(string_to_be_used_2)
                                break
                else:
                    print('should this branch be opened?', metha_name)
                    path_2 = clean_UM_log_directory
                    string_to_be_used_2 = 'start' + ' ' + path_2
                    os.system(string_to_be_used_2)

                    print('test not started')
                    list_of_test_results.append('ko')
                    list_of_fail_loop.append('ko')
                    #list_of_post_ops.append('ko')
                    list_of_cmd13_status.append('ko')
                    list_of_fail_details.append('ko')

            elif len(UM_datalog_vector) == 1:
                UM_datalog_vector_PATH = clean_UM_log_directory + '/' + UM_datalog_vector[0]
                print('ecco path da usare per leggere datalog:  ', UM_datalog_vector_PATH)
                with open(UM_datalog_vector_PATH, "r") as f:
                    fail_flag = 0
                    pass_flag = 0
                    dlog_content = f.readlines()
                    dlog_content_list = [x.strip() for x in dlog_content]  # contiene tutto cio' che ci serve, riga = stringa
                    if 'FAIL' in dlog_content_list[-2]:
                        print('entriamo nel branch fail... ')
                        fail_flag = 1
                        list_of_test_results.append('FAIL')
                        flag_cmd13 = 0
                        flag_details = 0
                        for dlog_line in dlog_content_list[::-1]:
                            if 'CMD13' in dlog_line and flag_cmd13 == 0:
                                print('cmd13 trovato...')
                                list_of_cmd13_status.append(dlog_line)
                                flag_cmd13 = 1
                            if 'Detail  :' in dlog_line and flag_cmd13 == 1:
                                print('detail trovato... ')
                                list_of_fail_details.append(dlog_line)
                                flag_details = 1
                            if 'loop' in dlog_line and flag_cmd13 == 1 and flag_details == 1:
                                list_of_fail_loop.append(dlog_line)
                                break

                            if ('errno' in dlog_line) and flag_cmd13 == 0 and flag_details == 0:
                                list_of_cmd13_status.append('check_the_datalog')
                                list_of_fail_details.append(dlog_line)
                                list_of_fail_loop.append('check_the_datalog')
                                # print('it fails but its not a standard fail, opening the dlog folder!', metha_name)
                                # path_2 = clean_UM_log_directory
                                # string_to_be_used_2 = 'start' + ' ' + path_2
                                # os.system(string_to_be_used_2)
                                break
                            if ('Exec() >> TFS Errors' in dlog_line) and flag_cmd13 == 0 and flag_details == 0:
                                list_of_cmd13_status.append('check_the_datalog')
                                list_of_fail_details.append(dlog_line)
                                list_of_fail_loop.append('check_the_datalog')
                                # print('it fails but its not a standard fail, opening the dlog folder!', metha_name)
                                # path_2 = clean_UM_log_directory
                                # string_to_be_used_2 = 'start' + ' ' + path_2
                                # os.system(string_to_be_used_2)
                                break
                            elif ('Metha PC Name' in dlog_line) and flag_cmd13 == 0 and flag_details == 0:
                                list_of_cmd13_status.append('check_the_datalog')
                                list_of_fail_details.append('check_the_datalog')
                                list_of_fail_loop.append('check_the_datalog')
                                print('it fails but its not a standard fail, opening the dlog folder!', metha_name)
                                path_2 = clean_UM_log_directory
                                string_to_be_used_2 = 'start' + ' ' + path_2
                                os.system(string_to_be_used_2)
                                break
                    elif 'PASS' in dlog_content_list[-2]:
                        pass_flag = 1
                        #print(metha_name, ' Passed')
                        list_of_test_results.append('PASS')
                        list_of_fail_loop.append('PASS')
                        #list_of_post_ops.append('PASS')
                        list_of_cmd13_status.append('PASS')
                        list_of_fail_details.append('PASS')
                    elif pass_flag == 0 and fail_flag == 0:
                        #print('i cant identify this one as pass or fail, ', metha_name)
                        list_of_test_results.append('terminated?')
                        list_of_fail_loop.append('terminated')
                        #list_of_post_ops.append('unidentified')
                        list_of_fail_details.append('terminated')
                        list_of_cmd13_status.append('terminated')

                        # print('was this terminated?', metha_name)
                        # path_2 = clean_UM_log_directory
                        # string_to_be_used_2 = 'start' + ' ' + path_2
                        # os.system(string_to_be_used_2)

        else:
            print('empty directory here', metha_name)
            list_of_test_results = list_of_test_results + [metha_name + ' empty']
            list_of_fail_loop = list_of_fail_loop + ['empty folder']
            #list_of_post_ops = list_of_post_ops + ['empty folder']
            list_of_fail_details = list_of_fail_details + ['empty folder']
            list_of_cmd13_status = list_of_cmd13_status + ['empty folder']
    else:
        print('ah! sembra che tu sia incappato in un caso non coperto dal tuo scriptino! birbante')
        break


print(len(list_of_metha_names))
print(len((list_of_test_results)))
print(len((list_of_fail_details)))
print(len((list_of_cmd13_status)))
print(len((list_of_fail_loop)))

final_dict = {'list_of_metha_names': list_of_metha_names[1::],
              'list_of_test_results': list_of_test_results[1::],
              'list_of_fail_details': list_of_fail_details[1::],
              'list_of_cmd13_status': list_of_cmd13_status[1::],
              'list_of_fail_loop': list_of_fail_loop[1::]}

if len(list_of_metha_names) == len(list_of_test_results) == len(list_of_fail_details) == len(list_of_cmd13_status) == len(list_of_fail_loop):
    df = pd.DataFrame(final_dict)
    print(df.head())
    df.to_excel(job_path + r'\output_table.xlsx')
else:
    print('something wrong, data cant be analyzed')


# if len(list_of_metha_names) == len(list_of_test_results) == len(list_of_fail_details) == len(list_of_cmd13_status) == len(list_of_fail_loop):
#     for line in range(len(list_of_metha_names)):
#         with open(job_path + r'\output_file_1.txt', "a+") as myfile:
#             #print(list_of_metha_names[line])
#             myfile.write(list_of_metha_names[line] + " / " + list_of_test_results[line] + " / " + list_of_fail_details[line] + "  /  " + list_of_cmd13_status[line]  +  " / " + list_of_fail_loop[line])
#             myfile.write("\n")
#     # for line in range(len(to_be_written), to_be_written_counter*2):
#     #     with open(r'C:\Users\Mfornaroli\Desktop\UM QUAL Turquoise\vm05419\mfornaroli_20190925_173955_dd21' + r'\output_file_0.txt', "a+") as myfile:
#     #         #print(list_of_metha_names[line])
#     #         myfile.write(to_be_written[line])
#     #         #myfile.write("\n")
#
# else:
#     print('something went wrong, data cant be analized ')

