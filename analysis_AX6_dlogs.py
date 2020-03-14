from os import listdir
from os.path import isfile, join

list_of_avg_TLC = []
list_of_max_TLC = []
list_of_min_TLC = []
dlog_lenght_list = []

logs_directory = r"C:\Users\Mfornaroli\Desktop\datalog_from_ax6\jf9E_fine_ciclatura\ultimo_run_lanciato"
files_in_directory = [f for f in listdir(logs_directory) if isfile(join(logs_directory, f))]
datalog_vector = [x for x in files_in_directory if x.endswith(".log")]
print('there is this number of datalogs/units: ', len(datalog_vector))
unit_dictionary = {}

for datalog_under_analysis in datalog_vector:
    print(datalog_under_analysis)
    with open(logs_directory + r'/' + datalog_under_analysis, "r") as f:
        # print(datalog_under_analysis.split('_'))
        unit = datalog_under_analysis.split('_')[6]
        unit_dictionary[unit] = 0
        dlog_content_list = f.readlines()
        dlog_content_list = [x.strip() for x in dlog_content_list]
        dlog_lenght_list = dlog_lenght_list + [str(len(dlog_content_list))]
        flag_avg = 0
        # flag_max = 0
        # flag_min = 0
        for dlog_line in dlog_content_list[::-1]:
           # print(dlog_line)
            if ('Average Block Erase for SLC' in dlog_line) and flag_avg == 0:
                print(dlog_line)
                print(dlog_line.split(':')[-1])
                unit_dictionary[unit] = int(dlog_line.split(':')[-1])
                flag_avg = 1
                break

print('there is this number of units in the dictionary: ', len(unit_dictionary))


sorted_unit_dictionary = {k: v for k, v in sorted(unit_dictionary.items(), key=lambda item: item[1])}
print(sorted_unit_dictionary)

for key in sorted_unit_dictionary:
    print( key, '>  SLC cycles:', sorted_unit_dictionary[key])

list_of_units = [int(key) for key in sorted_unit_dictionary]
list_of_units.sort()
for elem in list_of_units:
    print(elem)
