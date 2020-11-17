from prettytable import prettytable

urgent_important = [] 
non_urgent_important = []
urgent_non_important = []
non_urgent_non_important = []



t = PrettyTable(['', 'Urgent', 'Non-Urgent'])
t.add_row(['Important', urgent_important, non_urgent_important])
t.add_row(['Non-Important', urgent_non_important, non_urgent_non_important])

print(t)






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
