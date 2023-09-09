"""
06/09/23 haozepangthegoat
This file is a practice to write data into a python list. I endeavor to avoid using numpy.
args: ROW_ONLY
"""
# TODO: Fine tuning LaTeX code
# TODO: Fine tuning this process
import subprocess


class File:
    # initialisation
    num_comments = 0
    comments = []
    num_column = 0
    array = []  # The array that will contain main data
    title = []

    def __init__(self, INPUT_FILE_NAME='example_data.txt', DELIMITER=', ', OUTPUT_FILE_NAME='output.tex'):
        self.input_file_name = INPUT_FILE_NAME
        self.delimiter = DELIMITER
        self.output_file_name = OUTPUT_FILE_NAME

    # body
    # input process
    def cal_num_comments(self):
        """
        Purpose: calculate the number of lines of comments
        Returns:

        """
        with open(f'{self.input_file_name}') as file:
            # calculates num_comments
            for line in file:
                pass
                test = line.split()[0]
                if test == '%':
                    self.num_comments += 1

    def read_comments(self):
        """
        Purpose: read comments
        Returns: None
        """
        self.cal_num_comments()
        with open(f'{self.input_file_name}') as file:
            for num_lines, line in enumerate(file):
                if num_lines < self.num_comments:
                   self.comments.append(line.strip('%\n '))

    def read_data(self):
        """
        Purpose: read data
                 read the title of each column
        Returns: None
        """
        with open(f'{self.input_file_name}') as file:
            # read num_column
            # returns n-D array (with n being the number of column)
            for num_lines, line in enumerate(file):
                if num_lines == self.num_comments - 1:
                    break
            self.num_column = len(
                file.readline().split(self.delimiter)
            )
            self.array = [[] for i in range(self.num_column)]

        with open(f'{self.input_file_name}') as file:
            # reading actual data
            for num_line, line in enumerate(file):
                line = line.strip()
                if num_line == self.num_comments:
                    self.title = line.split(self.delimiter)
                if num_line > self.num_comments:
                    for i in range(0, self.num_column):
                        pass
                        self.array[i].append(line.split(self.delimiter)[i])

    def input_process(self):
        """
        Purpose: read data from a file
        Returns: None
        """
        pass
        self.read_comments()
        self.read_data()

    def output_process(self):
        """
        Purpose: write data into a LaTeX file
        Returns: None
        """
        with open(f'{self.output_file_name}', 'r+') as file:
            # preamble
            file.write('\\documentclass{article} \n')
            file.write('\\usepackage{booktabs} \n')
            # document
            file.write('\\begin{document} \n')
            # table
            file.write('\\begin{table}[h] \n')
            file.write('\\centering\n')
            # tabular
            file.write(f'\\begin{{tabular}}{{*{{{self.num_column}}}cr}} \n')
            file.write('\\toprule[1.5pt]\n')
            # row title
            for i in range(len(self.title)):
                file.write('\\bfseries  ')
                file.write(f'{self.title[i]}&')
            file.write('\\\\ \n')
            file.write('\\midrule')
            # data
            for n in range(len(self.array[0])):
                pass
                for i in range(self.num_column):
                    file.write(f'{self.array[i][n]}&')
                file.write('\\\\ \n')
            file.write('\\bottomrule[1.5pt]\n')
            file.write('\\end{tabular}\n')
            # comments
            file.write(f'\\caption{{{self.comments[1]}}}')
            file.write('\\end{table}\n')
            file.write('\\end{document} \n')

    def open_app(self):
        """
        Purpose: opens an app
        Returns: None
        """
        # Replace 'MyApp' with the name of the application you want to open.
        app_name = "Texifier"
        # Use subprocess to open the application.
        subprocess.run(["open", "-a", app_name])

    def make_table(self):
        """
        Purpose: make a table from the data
        Returns:

        """
        self.input_process()
        self.output_process()
        self.open_app()
