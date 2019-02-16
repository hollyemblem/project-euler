#  Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


class sumSquares:
    def __init__(self, range_numbers, power):
        self.range_numbers = range_numbers
        self.power = power

    def sum_of_squares(self):
        sum_squares = []
        for i in self.range_numbers:
            sum_squares.append(i ** self.power)
        return sum_squares

    def square_of_sum(self):
        range = 0
        for j in self.range_numbers:
            range += j
        range = range ** self.power
        return range


a = sumSquares(range(1, 101, 1), 2)
print(a.square_of_sum() - sum(a.sum_of_squares()))
