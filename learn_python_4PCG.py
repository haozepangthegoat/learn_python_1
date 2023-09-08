"""
06/09/23 haozepangthegoat
This file is a practice to write data into a python list. I endeavor to avoid using numpy.
args: ROW_ONLY
"""
# TODO: Fine tuning LaTeX code
# TODO: Fine tuning this process
import subprocess
# parameters
delimiter = ', '
file_name = 'example_data.txt'
# initialisation
array = [] # The array that will contain main data
comments = []
title = []
num_comments = 0
num_column = int

# body
# input process
with open(f'{file_name}') as file:
    # returns the number of lines of comments
    for line in file:
        pass
        test = line.split()[0]
        if test == '%':
            num_comments += 1

with open(f'{file_name}') as file:
    # reading comments
    for num_lines, line in enumerate(file):
        if num_lines < num_comments:
            comments.append(line.strip('%\n '))

with open(f'{file_name}') as file:
    # calculates num_column
    # returns n-D array (with n being the number of column)
    for num_lines, line in enumerate(file):
        if num_lines == num_comments - 1:
            break
    num_column = len(
        file.readline().split(delimiter)
    )
    array = [[] for i in range(num_column)]

with open(f'{file_name}') as file:
    # reading actual data
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

# output process
with open('output.tex', 'r+') as file:
    file.write('\\documentclass{article} \n')
    file.write('\\usepackage{booktabs} \n')
    file.write('\\begin{document} \n')
    file.write('\\begin{table}[h] \n')
    file.write('\\centering\n')
    # tabular
    file.write(f'\\begin{{tabular}}{{*{{{num_column}}}cr}} \n')
    file.write('\\toprule[1.5pt]\n')
    # writing title
    for i in range(len(title)):
        file.write('\\bfseries  ')
        file.write(f'{title[i]}&')
    file.write('\\\\ \n')
    file.write('\\midrule')
    # writing data
    for n in range(len(array[i])):
        pass
        for i in range(num_column):
            file.write(f'{array[i][n]}&')

        file.write('\\\\ \n')

    file.write('\\bottomrule[1.5pt]\n')
    file.write('\\end{tabular}\n')
    # writing comments
    file.write(f'\\caption{{{comments[1]}}}')
    file.write('\\end{table}\n')
    file.write('\\end{document} \n')
# Replace 'MyApp' with the name of the application you want to open.
app_name = "Texifier"
# Use subprocess to open the application.
subprocess.run(["open", "-a", app_name])
