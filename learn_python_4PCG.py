"""
06/09/23 haozepangthegoat
This file is a practice to write data into a python list. I endeavor to avoid using numpy.
args: ROW_ONLY
"""
# initialisation
delimiter = ', '
array = [] # The array that will contain main data
comments = []
title = []
num_comments = 0
num_column = int

# body
with open('example_data.txt') as file:
    # returns the number of lines of comments
    for line in file:
        pass
        test = line.split()[0]
        if test == '%':
            num_comments += 1

with open('example_data.txt') as file:
    pass
    for num_lines, line in enumerate(file):
        pass
        if num_lines < num_comments:
            pass
            comments.append(line)

with open('example_data.txt') as file:
    # calculates the number of column
    # returns an n dimension array with n being the number of column
    for num_lines, line in enumerate(file):
        if num_lines == num_comments - 1:
            break
    num_column = len(
        file.readline().split(delimiter)
    )
    array = [[] for i in range(num_column)]

with open('example_data.txt') as file:
    for num_line, line in enumerate(file):
        line = line.strip()
        if num_line == num_comments:
            title = line.split(delimiter)
        if num_line > num_comments:
            for i in range(0, num_column):
                pass
                array[i].append(line.split(delimiter)[i])

print(array)
print(title)
# print(num_comments)
print(comments)
