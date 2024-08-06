class Numbers:
    def __init__(self, value):
        self.value = value

    def ChkPrime(self):
        if self.value <= 1:
            return False
        for i in range(2, self.value):
            if self.value % i == 0:
                return False
        return True


    def Factors(self):
        factors = []
        for i in range(1, self.value):
            if self.value % i == 0:
                factors.append(i)
        return factors

    def SumFactors(self):
        factors = self.Factors()
        total = 0
        for factor in factors:
            total += factor
        return total

    @staticmethod
    def call_methods(value):
        num_obj = Numbers(value)
        print(f"Number: {value}")
        print(f"Is Prime: {num_obj.ChkPrime()}")
        print(f"Factors: {num_obj.Factors()}")
        print(f"Sum of Factors: {num_obj.SumFactors()}")
        print("\n")


# Example usage:
Numbers.call_methods(6)
Numbers.call_methods(28)
Numbers.call_methods(7)
Numbers.call_methods(12)
