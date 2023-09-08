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
input_file_name = 'example_data.txt'
output_file_name = 'output.tex'
# initialisation
array = []  # The array that will contain main data
comments = []
num_comments = 0
title = []
num_column = int


# body
# input process
def read_comments():
    """
    Purpose: calculate the number of lines of comments
    Returns: None
    """
    pass
    global input_file_name
    global num_comments
    global comments
    with open(f'{input_file_name}') as file:
        # calculates num_comments
        for line in file:
            pass
            test = line.split()[0]
            if test == '%':
                num_comments += 1

    with open(f'{input_file_name}') as file:
        # reading comments
        for num_lines, line in enumerate(file):
            if num_lines < num_comments:
                comments.append(line.strip('%\n '))


def read_data():
    pass
    global num_column
    global array
    global title
    with open(f'{input_file_name}') as file:
        # calculates num_column
        # returns n-D array (with n being the number of column)
        for num_lines, line in enumerate(file):
            if num_lines == num_comments - 1:
                break
        num_column = len(
            file.readline().split(delimiter)
        )
        array = [[] for i in range(num_column)]

    with open(f'{input_file_name}') as file:
        # reading actual data
        for num_line, line in enumerate(file):
            line = line.strip()
            if num_line == num_comments:
                title = line.split(delimiter)
            if num_line > num_comments:
                for i in range(0, num_column):
                    pass
                    array[i].append(line.split(delimiter)[i])


def input_process():
    pass
    read_comments()
    read_data()


# output process
def output_process():
    global output_file_name
    global array
    with open(f'{output_file_name}', 'r+') as file:
        # preamble
        file.write('\\documentclass{article} \n')
        file.write('\\usepackage{booktabs} \n')
        # document
        file.write('\\begin{document} \n')
        # table
        file.write('\\begin{table}[h] \n')
        file.write('\\centering\n')
        # tabular
        file.write(f'\\begin{{tabular}}{{*{{{num_column}}}cr}} \n')
        file.write('\\toprule[1.5pt]\n')
        # row title
        for i in range(len(title)):
            file.write('\\bfseries  ')
            file.write(f'{title[i]}&')
        file.write('\\\\ \n')
        file.write('\\midrule')
        # data
        for n in range(len(array[i])):
            pass
            for i in range(num_column):
                file.write(f'{array[i][n]}&')
            file.write('\\\\ \n')
        file.write('\\bottomrule[1.5pt]\n')
        file.write('\\end{tabular}\n')
        # comments
        file.write(f'\\caption{{{comments[1]}}}')
        file.write('\\end{table}\n')
        file.write('\\end{document} \n')


def open_pdf():
    pass
    # Replace 'MyApp' with the name of the application you want to open.
    app_name = "Texifier"
    # Use subprocess to open the application.
    subprocess.run(["open", "-a", app_name])


def main():
    pass
    input_process()
    output_process()
    open_pdf()


if __name__ == '__main__':
    main()
    print(array)
    print(title)
    print(num_comments)
    print(comments)

