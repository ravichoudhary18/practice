# input:  0100,0011,1010,1001

def main(string: str) -> str:
    number_list  = string.split(',')
    result = {}
    for i in number_list:
        if not int(i, 2) % 5:
            result[i] = int(i, 2)
    
    return result

input = '0100,0011,1010,1001'
result = main(input)
print(result)