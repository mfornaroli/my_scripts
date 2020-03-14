
with open(r"C:\Users\Mfornaroli\Desktop\UM_H1_project_ares.txt") as f:
    dlog_content = f.readlines()

dlog_content = [x.strip() for x in dlog_content]
new_UM_list_of_lists = []
print("done saving UM in vector")
print('number of rows in text file: ', len(dlog_content))

lba_to_be_found = 22647968

for line in range(len(dlog_content) - 1):
        lim_inf = 0
        lim_sup = 0
        cmd23_arg = 0
        if line % 10000 == 0:
            print("processing...line",  line )
        if dlog_content[line].startswith('23') and dlog_content[line + 1].startswith('25'):
            lim_inf = int(dlog_content[line + 1].split()[1], 16)
            cmd23_arg = int(dlog_content[line].split()[1], 16)
            lim_sup = lim_inf + cmd23_arg
            if (lba_to_be_found >= lim_inf) and (lba_to_be_found <= lim_sup) :
                print('bingo! LBA found in write op at line: ', line )
                print(lim_inf)
                print(lim_sup)
                print(lba_to_be_found)
                print(dlog_content[line])
                break

        if dlog_content[line].startswith('23') and dlog_content[line + 1].startswith('18'):
            lim_inf = int(dlog_content[line + 1].split()[1], 16)
            cmd23_arg = int(dlog_content[line].split()[1], 16)
            lim_sup = lim_inf + cmd23_arg
            if (lba_to_be_found >= lim_inf) and (lba_to_be_found <= lim_sup) :
                print('bingo! LBA found in read op at line: ', line)
                print('limite inferiore ', lim_inf)
                print('limite superiore ' , lim_sup)
                print('LBA ricercato    ', lba_to_be_found)
                print(dlog_content[line])
                break
