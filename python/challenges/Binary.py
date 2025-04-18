import math

class Binary:
    def __init__(self, _bin):
        self.bin = _bin

    def single_invert(self, _bin):
        if _bin == '0':
            return '1'
        else:
            return '0'

    def invert(self):
        _bin = ''
        for b in self.bin:
            _bin += self.single_invert(b)
        self.bin = _bin

    def format(self, n):
        res = ''
        size = math.ceil(len(self.bin)/n)
        for i in range(size):
            # print(self.bin[8*n:8*(n+1)])
            res += "{} ".format(self.bin[n*i:n*(i+1)])
        print(res)

    def to_dec(self):
        res = 0
        for count, value in enumerate(self.bin):
            # print("{} {}".format(count, value))
            math = pow(2, len(self.bin) - (count + 1)) * int(value)
            res += math
        print(res)

    def print(self):
        print(self.bin)

b1 = Binary('010011001001000110010001011010100010011001011000101000101000110101001100101000101010001010001101')

# b1.print()
# b1.invert()
# b1.print()
# b1.to_dec()
#b1.format(8)