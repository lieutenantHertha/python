'''
import csv

with open('work_stack/register_dates.csv', 'r', encoding='GBK') as f:
    csv_reader = csv.DictReader(f, delimiter=',')
    result_list = []
    for single_line in csv_reader:
        result_list.append(single_line)

    def sort_criteria(dict):
        return dict['Register_Date']

    sorted_version = sorted(result_list, key=sort_criteria)
    for single_item in sorted_version:
        print('{}\t{}'.format(single_item['File_Number'], single_item['Register_Date']))
'''
