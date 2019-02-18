# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# This object oriented approach is massively convoluted for what is essentially a very simple solution.
# However! The purpose of this hobby was to flex OO, so I stuck with it.

class largeSum:

    def __init__(self, text_file, slice_required):
        self.text_file = text_file
        self.slice_required = slice_required

    def list_traverser(self):
        new_list = []
        for line in self.text_file:
            new_list.append(int(line))
        summed_list = sum(new_list)
        return int(str(summed_list)[:self.slice_required])


class fileConnector:

    def __init__(self, file_name, file_behaviour):
        self.file_name = file_name
        self.file_behaviour = file_behaviour

    def file_return(self):
        # file_object = open(self.file_name, self.file_behaviour)
        with open(self.file_name, self.file_behaviour) as f:
            my_file = f.readlines()
        return my_file


file_build = fileConnector('euler-sum.txt', 'r').file_return()
m = largeSum(file_build, 10).list_traverser()
print(m)
