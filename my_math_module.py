import module.math_utils as my_math_utils

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))


result_of_add = my_math_utils.add(number1, number2)
print(f"Addition of {number1} and {number2} is {result_of_add}")

result_of_sub = my_math_utils.sub(number1, number2)
print(f"Subract of {number1} and {number2} is {result_of_sub}")

result_of_mul = my_math_utils.mul(number1, number2)
print(f"Multiplication of {number1} and {number2} is {result_of_mul}")

result_of_div = my_math_utils.div(number1, number2)
print(f"Division of {number1} and {number2} is {result_of_div}")


# Utilizing Modules:

from module.math_utils import add, div

def main():
    num1 = 15
    num2 = 3

    sum_result = add(num1, num2)
    division_result = div(num1, num2)

    print(f"The sum of {num1} and {num2} is {sum_result}")
    print(f"The division of {num1} and {num2} is {division_result}")


if __name__ == "__main__":
    main()