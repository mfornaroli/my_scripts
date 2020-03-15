import os
from datetime import datetime
print(dir(os))
print(os.getcwd())

# print(os.getcwd())
print(os.listdir(r'C:\Users\Mfornaroli\Desktop\script python'))
# create a folder on the Desktop

os.mkdir('new_folder_1')  # it won't work, with two directories
os.makedirs('new_folder_2/new_folder_3')

# then we can remove them
os.rmdir('new_folder_1')
os.removedirs('new_folder_2/new_folder_3')

# renaming files
# os.rename('old_name.file', 'new_name.file')

mod_time = os.stat('analisi_datalog_magnum.py').st_mtime
print(mod_time)
print(datetime.fromtimestamp(mod_time))

# you can use this for example to search for a file :D
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('current path: ', dirpath)
    print('files: ', filenames)
    print('directories: ', dirnames)


print(os.environ.get('HOME'))
