PL_list = ["0x000 0x2B 0x02", "0x000 0x36 0x1C", "0x000 0x71 0x17", "0x000 0x81 0x17" ]
temp_vector = []
PL_vector = []
with open(r"C:\Users\Mfornaroli\Desktop\full_dump_PL_BLOCK.txt") as f:
    dlog_content = f.readlines()

dlog_content = [x.strip() for x in dlog_content]
new_UM_list_of_lists = []
print("done saving log in vector")
print('number of rows in text file: ', len(dlog_content))



for line in range(len(dlog_content) - 1):
    for PL in PL_list:
        if dlog_content[line].startswith(PL):
            # cmd23_arg = int(dlog_content[line].split()[1], 16)
            print( dlog_content[line].split()[1:3],  " line number: ",  line)
            PL_vector.append(dlog_content[line].split()[1:3])
            print("temperature: ", dlog_content[line + 66].split()[9],  " line number: ",  line + 66)
            temp_vector.append(dlog_content[line + 66].split()[9])

print(len(PL_vector))
print(len(temp_vector))
# print(PL_vector)
# print(temp_vector)
for i in range(len(PL_vector)):
    print(PL_vector[i][0]+" " + PL_vector[i][1] , " / ", temp_vector[i])