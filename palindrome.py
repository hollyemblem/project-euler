# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009
# Find the largest palindrome made from the product of two 3-digit numbers.


class palindrome():
    def __init__(self, multiplier_a, range_numbers):
        self.multiplier_a = multiplier_a
        self.range_numbers = range_numbers

    def palindrome_build(self):
        multiplier_b = 0
        for i in self.range_numbers:
            for j in self.range_numbers:
                multiplier = (i * j)
                if str(multiplier) == (str(multiplier)[::-1]):
                    multiplier_b = multiplier
                if multiplier_b > self.multiplier_a:
                    self.multiplier_a = multiplier_b
        return self.multiplier_a


range_build = range(1, 999, 1)
multi = 9009

p = palindrome(multi, range_build).palindrome_build()

print(p)
