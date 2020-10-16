# This is a script of renaming filenames according to its original filename.
'''
import os
import sys

print(sys.executable)
os.chdir('work_stack/')

for single_file in os.listdir():
    full_name, file_extension = os.path.splitext(single_file)
    order_number, register_doc, project_name = full_name.split('-')
    new_full_name = '{}-{}{}'.format('2016' + order_number, project_name, file_extension)
    # print(new_full_name)
    os.rename(single_file, new_full_name)
'''
