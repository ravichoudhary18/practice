def main(string:str) -> dict:
    count = {}
    string = string.lower().replace(' ', '')
    for alphabet in string:
        if alphabet in count:
            count[alphabet] = count.get(alphabet, 0) + 1
    return count

string = 'Ravi Choudhary'
print(main(string))