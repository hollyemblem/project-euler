# WIP!

# Requires optimisation and tidy of OO methods.

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN,
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.

# What is the total of all the name scores in the file?


class FileManagement:
    def __init__(self):
        pass

    def file_open(self, file_name):
        file_list = []
        with open(file_name) as f:
            for line in f:
                return line

    def file_cleaner(self, file_version):
        file_list = []
        file_version = file_version.replace('"', '')
        file_list = file_version.split(',')
        file_list.sort()
        return file_list


class NamesManagement:

    def __init__(self):
        pass

    def position_calculator(self, file_version):
        for i in file_version:
            return (int(file_version.index(i)) + 1)

    def alphabet_calculator(self, file_version, index_value):
        sum = 0
        for i in file_version[index_value]:
            print(i)
            position_build = ord(i) - 64
            sum = position_build + sum
        return (sum * (index_value + 1))


m = FileManagement().file_open('names.txt')
n = FileManagement().file_cleaner(m)
position = NamesManagement().position_calculator(n)

sum = 0
i = 0
while i < len(n):
    sum = NamesManagement().alphabet_calculator(n, i) + sum
    i = i + 1
print(sum)
