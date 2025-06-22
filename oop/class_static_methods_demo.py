class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: float, b: float) -> float:
        print("Using static method 'add'")
        return a + b

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

if __name__ == "__main__":
    print("--- Demonstrating Calculator Class Methods ---")

    sum_result = Calculator.add(10, 5)
    print(f"Sum: {sum_result}\n")

    product_result_class = Calculator.multiply(10, 5)
    print(f"Product (via class): {product_result_class}\n")

    my_calc = Calculator()
    sum_result_instance = my_calc.add(20, 3)
    print(f"Sum (via instance): {sum_result_instance}\n")

    product_result_instance = my_calc.multiply(20, 3)
    print(f"Product (via instance): {product_result_instance}\n")

    print(f"Accessing class attribute directly: {Calculator.calculation_type}")
