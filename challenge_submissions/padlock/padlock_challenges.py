def challenge_1():
    """
    Padlock Hint: code = 1 + 2 + 3 + 4 + … + 38 + 39 + 40
    """
    code = 0
    for i in range(1, 41):
        code += i

    return code


def challenge_2():
    """
    Padlock Hint: code = Total number of 3-digit combinations where digit1 < digit2 < digit3

    e.g. 123 and 358 count as valid combinations whereas 321 or 011 are invalid combinations.
    """
    code = 0
    for digit1 in range(0, 10):
        for digit2 in range(0, 10):
            for digit3 in range(0, 10):
                if digit1 < digit2 < digit3:
                    code += 1

    return code


def challenge_3():
    """
    Padlock Hint: code = Total number of 3-digit combinations where digit1, digit2 and digit3 are all even numbers

    e.g. 024 and 886 count as valid combinations whereas 124 or 456 are invalid combinations.
    """
    code = 0
    for digit1 in range(0, 10):
        for digit2 in range(0, 10):
            for digit3 in range(0, 10):
                if (digit1 % 2 == 0) and (digit2 % 2 == 0) and (digit3 % 2 == 0):
                    code += 1

    return code


def challenge_4():
    """
    Padlock Hint: code = Total number of 3-digit combinations where the sum of all three digits (digit1 + digit2 + digit3) is an odd number

    e.g. 034 and 555 count as valid combinations whereas 123 or 468 are invalid combinations.
    """
    code = 0
    for digit1 in range(0, 10):
        for digit2 in range(0, 10):
            for digit3 in range(0, 10):
                if (digit1 + digit2 + digit3) % 2 != 0:
                    code += 1

    return code


def challenge_5():
    """
    Padlock Hint: code = Total number of 3-digit combinations where at least two digits are equal.

    e.g. 030 and 558 count as valid combinations whereas 123 or 468 are invalid combinations.
    """
    code = 0
    for digit1 in range(0, 10):
        for digit2 in range(0, 10):
            for digit3 in range(0, 10):
                if (digit1 == digit2) or (digit1 == digit3) or (digit2 == digit3):
                    code += 1

    return code


if __name__ == "__main__":
    code_1 = challenge_1()
    print(f"Unlock code for challenge 1: {code_1}")

    code_2 = challenge_2()
    print(f"Unlock code for challenge 1: {code_2}")

    code_3 = challenge_3()
    print(f"Unlock code for challenge 3: {code_3}")

    code_4 = challenge_4()
    print(f"Unlock code for challenge 4: {code_4}")

    code_5 = challenge_5()
    print(f"Unlock code for challenge 5: {code_5}")
