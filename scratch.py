answer_file = open("hello.txt", "a")
num1 = float(input("enter a number: "))
num2 = float(input("enter second number: "))
operator = input("enter operation: ")
if operator == "+":
    answer_file.write(", ")
    answer_file.write(str(num1 + num2))
elif operator == "*":
    answer_file.write(", ")
    answer_file.write(str(num1 * num2))
elif operator == "-":
    answer_file.write(", ")
    answer_file.write(str(num1 - num2))
elif operator == "/":
    answer_file.write(", ")
    answer_file.write(str(float(num1 / num2)))
else:
    print("enter a valid operator: ")
