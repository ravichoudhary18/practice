# 9 * 8 * 7

def main(number):
    if number == 0:
        return 1
    result = 1
    for i in range(1, number+1):
        result = result * i
    return result


result = main(125)
print(result)