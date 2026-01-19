# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


def main(input_: int) -> int:
    string = []
    for i in range(1, 5):
        string.append('a' * i)
    string = '+'.join(string)
    string = string.replace('a', str(input_))
    result = eval(string)
    return result

input_ = 9
result = main(input_)
print(result)