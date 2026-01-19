# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def main(string: str) -> dict:
    result = {'UPPER CASE': 0, 'LOWER CASE': 0}
    for i in string:
        if i.isalpha():
            if i.isupper():
                result['UPPER CASE'] = result['UPPER CASE'] + 1
            else:
                result['LOWER CASE'] = result['LOWER CASE'] + 1
        else:
            pass
    
    return result

input = 'Hello World!'
result = main(input)
print(result)