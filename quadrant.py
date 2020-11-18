from prettytable import PrettyTable, ALL
import csv

##############################################################################

#IMPORTING CSV DATA

with open('Eisenhower.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    urgent_important = []
    non_urgent_important = []
    urgent_non_important = []
    non_urgent_non_important = []

    for task in csv_reader:
        if task['Urgent/Non Urgent'] == 'Urgent' and task['Important/Non Important'] == 'Important':
            urgent_important.append(task['Task'])
        elif task['Urgent/Non Urgent'] == 'Non Urgent' and task['Important/Non Important'] == 'Important':
            non_urgent_important.append(task['Task'])
        elif task['Urgent/Non Urgent'] == 'Urgent' and task['Important/Non Important'] == 'Non Important':
            urgent_non_important.append(task['Task'])
        elif task['Urgent/Non Urgent'] == 'Non Urgent' and task['Important/Non Important'] == 'Non Important':
            non_urgent_non_important.append(task['Task'])
        else:
            print('Error, please define urgency and importance.')


##############################################################################

#FORMATTING THE ARRAYS

def correct_depth(list):
    max_lists = 10
    if len(list) > max_lists:
        max_lists = len(list)
    else:
        while len(list) < max_lists:
            list.append('')
        else:
            return list


correct_depth(urgent_important)
correct_depth(non_urgent_important)
correct_depth(urgent_non_important)
correct_depth(non_urgent_non_important)


#Defining new lists for width
width_urgent_important = []
width_non_urgent_important = []
width_urgent_non_important = []
width_non_urgent_non_important = []

def correct_width(list, new_list):
    max_string_len = 30
    for string in list:
        if len(string) > max_string_len:
            max_string_len = len(string)
        else:
            while len(string) < max_string_len:
                string += " "
            new_list.append(string)

correct_width(urgent_important, width_urgent_important)
correct_width(non_urgent_important, width_non_urgent_important)
correct_width(urgent_non_important, width_urgent_non_important)
correct_width(non_urgent_non_important, width_non_urgent_non_important)


formatted_urgent_important = '\n'.join(width_urgent_important)
formatted_non_urgent_important = '\n'.join(width_non_urgent_important)
formatted_urgent_non_important = '\n'.join(width_urgent_non_important)
formatted_non_urgent_non_important = '\n'.join(width_non_urgent_non_important)


##############################################################################

#CREATING THE TABLE


t = PrettyTable()
t.hrules = ALL
t.field_names = ['', 'Urgent', 'Non-Urgent']
t.add_row(['Important', formatted_urgent_important, formatted_non_urgent_important])
t.add_row(['Non-Important', formatted_urgent_non_important, formatted_non_urgent_non_important])
print(t)


##############################################################################



























# print ("""+-----+---------------------------------------+----------------------------------------+
# |     | Urgent                                | Non Urgent                             |
# +-----+---------------------------------------+----------------------------------------+
# |     |                                       |                                        |
# |  I  |                                       |                                        |
# |  m  |                                       |                                        |
# |  p  |                                       |                                        |
# |  o  |                                       |                                        |
# |  r  |                                       |                                        |
# |  t  |                                       |                                        |
# |  a  |                                       |                                        |
# |  n  |                                       |                                        |
# |  t  |                                       |                                        |
# |     |                                       |                                        |
# |     |                                       |                                        |
# |     |                                       |                                        |
# |     |                                       |                                        |
# |     |                                       |                                        |
# |     |                                       |                                        |
# |     |                                       |                                        |
# |     |                                       |                                        |
# |     |                                       |                                        |
# |     |                                       |                                        |
# +-----+---------------------------------------+----------------------------------------+
# |     |                                       |                                        |
# |  N  |                                       |                                        |
# |  o  |                                       |                                        |
# |  n  |                                       |                                        |
# |     |                                       |                                        |
# |  I  |                                       |                                        |
# |  m  |                                       |                                        |
# |  p  |                                       |                                        |
# |  o  |                                       |                                        |
# |  r  |                                       |                                        |
# |  t  |                                       |                                        |
# |  a  |                                       |                                        |
# |  n  |                                       |                                        |
# |  t  |                                       |                                        |
# |     |                                       |                                        |
# |     |                                       |                                        |
# |     |                                       |                                        |
# |     |                                       |                                        |
# |     |                                       |                                        |
# |     |                                       |                                        |
# |     |                                       |                                        |
# |     |                                       |                                        |
# +-----+---------------------------------------+----------------------------------------+""")
