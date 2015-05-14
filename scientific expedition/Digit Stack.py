def digit_stack(commands):
    stack = []
    sum = 0
    for command in commands:
        param = command.split()
        if param[0] == 'PUSH':
            stack.append(int(param[1]))
        if param[0] == 'POP':
                sum += stack.pop() if stack else 0
        if param[0] == 'PEEK':
                sum += stack[-1] if stack else 0
    return sum


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1",
                        "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
