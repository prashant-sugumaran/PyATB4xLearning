class Calc:


    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


obj = Calc()
output_sum = obj.sum(3, 5)
output_sub = obj.sub(5, 3)
output_mul = obj.mul(4, 5)
output_div = obj.div(3, 1)

print(output_sum, output_sub, output_mul, output_div)
