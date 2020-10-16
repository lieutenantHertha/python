# This is a script of extracting register date from external administrative license
'''
import os
import csv

os.chdir('work_stack/')

with open('register_dates.csv', 'w') as destination_file:
    fieldnames = ['File_Number', 'Register_Date']
    csv_writer = csv.DictWriter(destination_file, fieldnames=fieldnames, delimiter=',')
    csv_writer.writeheader()
    for single_file in os.listdir():
        with open(single_file, 'r', encoding='UTF-8') as source_file:
            file_number, extension = os.path.splitext(single_file)
            register_dates = {}
            for single_line in source_file:
                pass
            register_dates['File_Number'] = file_number
            register_dates['Register_Date'] = single_line.strip(' ').strip('\n')
            csv_writer.writerow(register_dates)
'''
