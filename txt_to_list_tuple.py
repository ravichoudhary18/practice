import re

def pattern_match(text: str) -> bool:
    # matches: 1,2,3 or 10,20,30
    return bool(re.fullmatch(r'\d+(,\d+)*', text))


def main(text: str):
    if not pattern_match(text):
        return ("Pattern Not Match",)

    list_ = text.split(",")
    tuple_ = tuple(list_)
    return list_, tuple_


text = input("Enter list of number with comma separated: ")

result = main(text)
for i in result:
    print(i)
