# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

def main(string: str) -> dict:
    result = {"LETTERS": 0, "DIGITS": 0}
    for i in string:
        if i.isalpha():
            result["LETTERS"] = result["LETTERS"] + 1
        if i.isdigit():
            result["DIGITS"] = result["DIGITS"] + 1
    return result

input = 'hello world! 123'
result = main(input)
print(result)