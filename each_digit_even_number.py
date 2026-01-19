# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def main() -> list:
    result = []
    for i in range(1000, 3001):
        value = str(i)
        first_digit = int(value[0]) % 2
        second_digit = int(value[1]) % 2
        third_digit = int(value[2]) % 2
        forth_digit = int(value[3]) % 2
        if first_digit == 0 and second_digit == 0 and third_digit == 0 and forth_digit == 0:
            result.append(i)
    return result

result = main()
print(result)