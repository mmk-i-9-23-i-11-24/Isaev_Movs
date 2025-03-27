def interpret_expression(expression):
    parts = expression.split()
    a = int(parts[0])
    operator = parts[1]
    b = int(parts[2])
    if operator == "plus":
        return a + b
    elif operator == "minus":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return a // b
    else:
        raise ValueError("Неизвестный оператор")

while 1 > 0:
    input_expression = input("Введите выражение (например, '45 plus 8'): ")
    result = interpret_expression(input_expression)
    print(result)

