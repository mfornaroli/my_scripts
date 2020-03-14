PL_list = ["0x000 0x2B 0x02", "0x000 0x36 0x1C", "0x000 0x71 0x17", "0x000 0x81 0x17" ]  #lista dei panic log che si vuole decodificare

PL_dec = [11010, 13852, 28951, 33047] # solo x informazione, traduzione in decimale
VB_vector = []
CE_vector = []
PL_with_ph_address_vector = []
LBA_vector = []
temp_vector = []
PL_vector = []
ph_addr_vector = []
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
            if PL != "0x000 0x36 0x1C":
                PL_with_ph_address_vector.append(PL)
                print(dlog_content[line])
                print("LBA: ", dlog_content[line].split()[5:9][::-1])
                print("VB:  ", dlog_content[line].split()[9:11], PL)
                print("CE:  ", dlog_content[line].split()[11:13])
                print('Physical address: ', dlog_content[line].split()[13:17])

                LBA_vector.append(dlog_content[line].split()[5:9][::-1])
                VB_vector.append(dlog_content[line].split()[9:11] + ["PL: " , PL])
                CE_vector.append(dlog_content[line].split()[11])
                ph_addr_vector.append(dlog_content[line].split()[13:17] + ["PL: " , PL] )


print(len(PL_vector))
print(len(temp_vector))
# print(PL_vector)
# print(temp_vector)

# for i in range(len(PL_vector)):
#     print(PL_vector[i][0]+" " + PL_vector[i][1] , " / ", temp_vector[i])

for j in range(len(VB_vector)):
    print(VB_vector[j], "ce: ", CE_vector[j], "LBA: " , LBA_vector[j])
    # print(CE_vector[j])
    # print(LBA_vector[j])
scale = 16
num_of_bits = 8

print("heeey", len(ph_addr_vector), len(PL_with_ph_address_vector))

for j in range(len(ph_addr_vector)):
    #print(ph_addr_vector[j])
    bin_vector = bin(int(ph_addr_vector[j][0], scale))[2:].zfill(num_of_bits), bin(int(ph_addr_vector[j][1], scale))[2:].zfill(num_of_bits), bin(int(ph_addr_vector[j][2], scale))[2:].zfill(num_of_bits), bin(int(ph_addr_vector[j][3], scale))[2:].zfill(num_of_bits)
    #print(bin_vector)
    bin_vector = bin_vector[::-1]
    #print(bin_vector)
    PB_location = bin_vector[0]+ bin_vector[1][0:7]
    plane_location = bin_vector[1][7]
    page_location = bin_vector[2] + bin_vector[3][0:6]
    # print("PH BLOCK: ", PB_location)
    # print("plane: ", plane_location )
    # print("page: ", page_location)

    print("panicLog: / ", PL_with_ph_address_vector[j][5::], " / nand: /", CE_vector[j], " / ph_block_dec: / ", int(PB_location, 2), " / plane_dec:/ ", int(plane_location,2), " / page_dec: / ", int(page_location, 2), " / LBA: /", LBA_vector[j]  )
    # print("nand: ", CE_vector[j])
    # print("ph block dec: ", int(PB_location, 2))
    # print("plane dec: ", int(plane_location,2) )
    # print("page dec: ", int(page_location, 2))