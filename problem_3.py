# 3. Write a function that takes an arithmetic expression in string form (e.g. "5 x 6 / 3 + 1") and returns the 
#    numerical result. Assume the arithmetic expression only consists of DMAS (div/mul/add/sub) operations.

def is_operator(token):
    return token in ['+', '-', 'x', '/']

def precedence(token):
    if token in ['+', '-']:
        return 1
    return 2

def do_operator(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == 'x':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2

def evaluate(input):
    tokens = parse(input)

    operator_stack = []
    operand_stack = []

    for token in tokens:
        if is_operator(token):
            operator_stack.append(token)
        else:
            operand_stack.append(token)


    side_operator_stack = []
    side_operand_stack = []
    while operator_stack or side_operator_stack:
        precedence_differs = len(operator_stack)> 1 and precedence(operator_stack[-1]) < precedence(operator_stack[-2])
        if operator_stack and precedence_differs:
            side_operator_stack.append(operator_stack.pop())
            side_operand_stack.append(operand_stack.pop())
            continue
        elif side_operator_stack and (not operator_stack or  precedence(operator_stack[-1]) <= precedence(side_operator_stack[-1])):
            operator = side_operator_stack.pop()
            operand1 = side_operand_stack.pop()
            operand2 = operand_stack.pop()
        else:
            operator = operator_stack.pop()
            operand1 = operand_stack.pop()
            operand2 = operand_stack.pop()

        result = do_operator(operator, operand1, operand2)
        operand_stack.append(result)

    return operand_stack.pop()

def parse(input):
    parts = input.split()
    new_parts = []
    for token in parts:
        try:
            new_parts.append(int(token))
        except ValueError:
            new_parts.append(token)
    return new_parts
