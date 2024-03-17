# Arithmetic Formatter


def arithmetic_arranger(problems, show_answers=False):
    # Symbols allowed
    SYMBOLS = ["+", "-"]
    # Format structure
    first_row = []
    second_row = []
    lines = []
    results = []
    prueba = []

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        # Dividing the operation
        num1, symbol, num2 = problem.split(" ")

        # Validate problems
        if symbol not in SYMBOLS:
            return "Error: Operator must be '+' or '-'."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(num1) >= len(num2):
            space = len(num1) + 2
        else:
            space = len(num2) + 2

        # Formatting the lines
        frow = f"{num1.rjust(space)}"
        srow = f"{symbol} {num2.rjust(space - 2)}"
        line = f"{space * '-'}"
        first_row.append(frow)
        second_row.append(srow)
        lines.append(line)

        # Results
        result = int(num1) + int(num2) if symbol == "+" else int(num1) - int(num2)
        results.append(f"{str(result).rjust(space)}")

    if show_answers == True:
        text = f'{"    ".join(first_row)}\n{"    ".join(second_row)}\n{"    ".join(lines)}\n{"    ".join(results)}'
        return text

    text = f'{"    ".join(first_row)}\n{"    ".join(second_row)}\n{"    ".join(lines)}'
    return text


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')
print(f'\n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])}')
print(
    f'\n{arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)}'
)

"""
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
"""
