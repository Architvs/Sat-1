import csv

lines = list()
rownumbers_to_remove= [5,6]

with open('names.csv', 'r') as read_file:
    reader = csv.reader(read_file)
    for row_number, row in enumerate(reader, start=1):
        if(row_number not in rownumbers_to_remove):
            lines.append(row)

with open('delete.csv', 'w') as write_file:
    writer = csv.writer(write_file)
    writer.writerows(lines)
