import csv
from collections import Counter
from matplotlib import pyplot as plt
import numpy as np

language_counters = [Counter() for index in range(3)]

with open('Language_Popularity_Survey.csv', 'r') as data_file:
    csv_reader = csv.DictReader(data_file)

    for single_row in csv_reader:
        for index in range(3):
            language_counters[index].update(
                list(single_row.values())[index].split(';'))

for single_counter in language_counters:
    del single_counter['']
    del single_counter['NA']

lang_counter_2017 = language_counters[0]
lang_counter_2018 = language_counters[1]
lang_counter_2019 = language_counters[2]

lang_keys_2017 = set(single_key for single_key in lang_counter_2017.keys())
lang_keys_2018 = set(single_key for single_key in lang_counter_2018.keys())
lang_keys_2019 = set(single_key for single_key in lang_counter_2019.keys())

common_lang = sorted(
    list(
        lang_keys_2017.intersection(lang_keys_2018).intersection(
            lang_keys_2019)))

new_counter_2017 = dict()
new_counter_2018 = dict()
new_counter_2019 = dict()

for single_common_lang in common_lang:
    new_counter_2017[single_common_lang] = lang_counter_2017[
        single_common_lang]
    new_counter_2018[single_common_lang] = lang_counter_2018[
        single_common_lang]
    new_counter_2019[single_common_lang] = lang_counter_2019[
        single_common_lang]

plt.style.use('fivethirtyeight')
lang_axis = list(common_lang)
x_indexes = np.arange(len(common_lang))
bar_width = 0.3
plt.barh(x_indexes - bar_width,
         new_counter_2017.values(),
         color='#60acfc',
         height=bar_width,
         label='2017')
plt.barh(x_indexes,
         new_counter_2018.values(),
         color='#5bc49f',
         height=bar_width,
         label='2018')
plt.barh(x_indexes + bar_width,
         new_counter_2019.values(),
         color='#ff7c7c',
         height=bar_width,
         label='2019')
plt.legend()
plt.title('Technologies Popularity With Time')
plt.xlabel('Variaties Of Technology')
plt.ylabel('Popularity Of Technology')
plt.yticks(ticks=x_indexes, labels=common_lang)
plt.tight_layout()
plt.show()