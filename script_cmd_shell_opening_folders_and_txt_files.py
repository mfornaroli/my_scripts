import os
# path_1 = 'C:/Users/Mfornaroli/Desktop/FBGA_issue_caterina_fail_LBA.txt'
path_2 = r'C:\Users\Mfornaroli\Desktop'
#path_2 = 'C:\\Users\\Mfornaroli\\Desktop'
# string_to_be_used_1 = 'notepad.exe' + ' ' + path_1
string_to_be_used_2 = 'start' + ' nuova_cartella'
string_to_be_used_3 = 'mkdir' + ' ' + path_2 + '\\' + 'nuova_cartella'
print(string_to_be_used_3)

os.system(string_to_be_used_3)
#os.system(string_to_be_used_2)