a_num = int(input("Введите число a"))
asd = (input("Введите операцию"))
b_num = int(input("Введите число b"))

if asd == "+":
    print(a_num + b_num)
elif asd == "-":
    print(a_num - b_num)
elif asd == "*":
    print(a_num * b_num)
elif asd == "/":
    print(a_num / b_num)
else:
    print("Вы ввели не операцию")

