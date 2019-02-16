# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


class multiplyFinder():
    def __init__(self, multiplier_one, multiplier_two, start, end):
        self.multiplier_one = multiplier_one
        self.multiplier_two = multiplier_two
        self.start = start
        self.end = end

    def find_multipliers(self):
        num_list = []
        while self.start < self.end:
            if self.start % self.multiplier_one == 0:
                num_list.append(self.start)
            elif self.start % self.multiplier_two == 0:
                num_list.append(self.start)
            self.start += 1
        return (sum(num_list))


m = multiplyFinder(3, 5, 0, 1000).find_multipliers()
print(m)
