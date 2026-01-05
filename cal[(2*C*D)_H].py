import re
import math

C = 50
H = 30

def patter_match(text:str) -> bool:
    return bool(re.fullmatch(r'\d+(,\d+)', text))

def main(list_of_number:list) -> list:
    return [round(math.sqrt((2 * C * int(i))/H)) for i in list_of_number]

text_input = input("Enter number with comma seprated: ")
text_validation = patter_match(text_input)
if not text_validation:
    print('input partern not match')
list_of_number = text_input.split(',')
result = main(list_of_number)
print(result)