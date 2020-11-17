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


formatted_urgent_important = '\n'.join(urgent_important)
formatted_non_urgent_important = '\n'.join(non_urgent_important)
formatted_urgent_non_important = '\n'.join(urgent_non_important)
formatted_non_urgent_non_important = '\n'.join(non_urgent_non_important)


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
