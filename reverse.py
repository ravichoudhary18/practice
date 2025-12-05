# reverse

def main(string:str) -> str:
    empty = ''
    for ch in string:
        empty = ch + empty
    return empty


print(main('main'))

