import os
import datetime

# os.remove('novel.txt')

# os.rename('first_draft.txt', 'finished_masterpiece.txt')

# os.path.exists('finished_masterpiece.txt')

# os.path.getsize('finished_masterpiece.txt')

# print(os.path.getmtime('finished_masterpiece.txt'))

# timestamp = os.path.getmtime('finished_masterpiece.txt')
# print(datetime.datetime.fromtimestamp(timestamp))

# file = 'file.dat'
# if os.path.isfile(file):
#     print(os.path.isfile(file))
#     print(os.path.getsize(file))
# else:
#     print(os.path.isfile(file))
#     print('File not found')

# print(os.path.abspath('Working-with-Files.py'))

# os.mkdir('new_dir')
# os.chdir('new_dir')
# print(os.getcwd())

# ======================================================

# target_dir = 'new_dir'
# if os.path.isdir(target_dir):
#     print('Directory already exists')
# else:
#     print(f"The directory '{target_dir}' does not exist in '{os.getcwd()}'")

dir = 'website'
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print('{} is a directory'.format(fullname))
    else:
        print('{} is a file'.format(fullname))
