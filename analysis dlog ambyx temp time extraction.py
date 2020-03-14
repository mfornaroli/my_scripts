import re
import datetime
list_of_strings = []
list_of_strings_2 = []

"""
per usare bisogna:
capire quanti tb ci sono tra tb che si vuole misurare, e effettiva misura di temperatura
scrivere in file di testo quali sono gli step di cui vogliamo sapere la temperatura.. dipende dal programma..

"""
num_tb = 4
with open(r"C:\Users\Mfornaroli\Desktop\TEMP TRIAL\LOG_temp_WOTLC_FULL_BIB_-32.txt") as f:
    dlog_content = f.readlines()
dlog_content = [x.strip() for x in dlog_content]
print("dlog saved in vector: ", len(dlog_content), " lines")

with open(r"C:\TEMP\measured_operations.txt") as f:
    measured_operations = f.readlines()
measured_operations = [x.strip() for x in measured_operations]
print("measured operations saved in vector: ", len(measured_operations), " lines")
print(measured_operations)

for line in range(len(dlog_content)):
# for line in range(90000, 91100): debug
    if 'abp85::pshstats_temperature' in dlog_content[line] and 'Running test' in dlog_content[line] and 'print_info' in dlog_content[line]:
        string_2 = dlog_content[line]
        time = re.findall(r'\d{2}:\d{2}:\d{2}', dlog_content[line])
        print("trovato temperature measurement alla riga: ", line)
        print(dlog_content[line])
        testblock_counter = 0
        flag = 0
        for line_1 in range(line-1, line-300, -1):
                # print('esaminiamo riga', line_1)
                if 'Running test' in dlog_content[line_1] and testblock_counter <= num_tb:
                    print(dlog_content[line_1])
                    testblock_counter +=1
                    for measured_op in measured_operations:
                            if measured_op in dlog_content[line_1] and flag == 0 :
                                print("eureka!!")
                                print(measured_op)
                                string = 'temp measured at: ' + time[0] + " - after: " + measured_op
                                print('temp measured at: ', time[0], " after: ", measured_op)
                                flag = 1
                                list_of_strings = list_of_strings + [string]
                                list_of_strings_2 = list_of_strings_2 + [string_2]
                                break

print(list_of_strings)

for line in range(len(list_of_strings)):
    with open(r"C:\Users\Mfornaroli\Desktop\TEMP TRIAL\output_file_-32.txt" , "a+") as myfile:
        myfile.write(list_of_strings[line])
        myfile.write("\n")
        # myfile.write(list_of_strings_2[line])
        # myfile.write("\n")

