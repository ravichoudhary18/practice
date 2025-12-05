def main(string:str, match:str) -> list:
    len_of_string = len(string)
    len_of_match = len(match)
    index = []
    for i in range(len_of_string):
        if string[i: i + len_of_match] == match:
            index.append(i)
    
    return index

string = 'abcdefabcd'
match = 'cd'
result = main(string, match)
print(result)