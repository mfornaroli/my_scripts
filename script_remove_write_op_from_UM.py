
with open(r"C:\Users\Mfornaroli\Desktop\UM_turquoise_metha\UM_for_Metha15.txt") as f:
# with open(r"C:\Users\Mfornaroli\Desktop\UM_turquoise_metha\prova.txt") as f:
    dlog_content = f.readlines()
dlog_content = [x.strip() for x in dlog_content]
new_UM_list_of_lists = []
print("done saving UM in vector")
print(len(dlog_content))
# print(dlog_content)


for line in range(len(dlog_content)):
    if line % 10000 == 0:
        print("processing...", line , "line")
    if dlog_content[line].startswith('23') and dlog_content[line + 1].startswith('25'):
        # new_UM_list_of_lists = new_UM_list_of_lists + [dlog_content[line]] + [dlog_content[line + 1]]
        dlog_content[line] = 'remove_me'
        dlog_content[line + 1] = 'remove_me'
print("done cutting off write operations")
print(len(new_UM_list_of_lists))


# for line in range(len(new_UM_list_of_lists)):
#     if line % 10000 == 0:
#         print("writing...", line , "line")
#     with open(r"C:\Users\Mfornaroli\Desktop\UM_turquoise_metha" + "/UM_only_read.txt", "a+") as myfile:
#         myfile.write(new_UM_list_of_lists[line])
#         myfile.write("\n")

clean_dlog_content = [x for x in dlog_content if x != 'remove_me']
print(len(clean_dlog_content))

for line in range(len(clean_dlog_content)):
    if line % 10000 == 0:
        print("writing...", line , "line")
    with open(r"C:\Users\Mfornaroli\Desktop\UM_turquoise_metha" + "/UM_only_read.txt", "a+") as myfile:
        myfile.write(clean_dlog_content[line])
        myfile.write("\n")