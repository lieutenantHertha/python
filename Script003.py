# This is a scirpt of ranaming filenames according to some external dataset.
'''
import csv
import os

with open('filenames.csv', 'r') as naming_file:
    csv_reader = csv.DictReader(naming_file, delimiter=',')

    os.chdir('work_stack/')
    for single_file in os.listdir():
        file_name, file_extension = os.path.splitext(single_file)
        register_number = file_name[4:7]
        for single_line in csv_reader:
            if str(single_line['Number'].zfill(3)) == register_number:
                new_filename = '{}-{}-{}{}'.format(register_number,
                                                   single_line['RegisterDoc'], single_line['ProjectName'], file_extension)
                os.rename(single_file, new_filename)
                print(new_filename)
                break
            else:
                continue
'''
