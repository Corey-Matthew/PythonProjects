#!/usr/bin/env python3

import csv

csv_file = open("/home/cdavis/PycharmProjects/udemy_course/csv_example.csv", "r")
content = csv.reader(csv_file, delimiter="|")
header = next(content)
no_row = len(list(content))
for rows in content:
    print(rows)
csv_file.close()

print(header)
print(no_row)
data_list = [["Player#", "targets", "catches", "TDs"], ["45", "43", "68", "4"], ["54", "1", "1", "1"]]
csv_file = open("/home/cdavis/PycharmProjects/udemy_course/csv_example.csv", "w", newline="")
csv_writer = csv.writer(csv_file, delimiter=",")
csv_writer.writerows(data_list)
csv_file.close()