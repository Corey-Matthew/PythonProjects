#!/usr/bin/env python3
file = open('new_file2.txt', 'w')
my_content = ["this is data 4", "This is data 5", "This is data 6"]
for line in my_content:
    file.write(line + "\n")
file.close()
readable = open("new_file.txt")
print(readable.mode)
data_list = readable.readlines()
data_str = readable.read()
print(data_list)
readable.seek(0)
print(*readable.readlines())

