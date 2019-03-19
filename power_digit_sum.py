## Problem 16. A nice easy one to get back into things!


class powerDigitSum():
    def __init__(self, value_power):
        self.value_power = value_power

    def sum_build(self):
        value = map(int, str(self.value_power))
        return sum(value)


power = powerDigitSum(2 ** 1000).sum_build()
print(power)
