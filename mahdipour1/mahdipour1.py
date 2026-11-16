num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2

print("Addition:", sum_result)
print(type(sum_result))

print("Subtraction:", sub_result)
print(type(sub_result))

print("Multiplication:", mul_result)
print(type(mul_result))

if num2 != 0:
    div_result = num1 / num2
    print("Division:", div_result)
    print(type(div_result))
else:
    print("Division by zero is not possible.")