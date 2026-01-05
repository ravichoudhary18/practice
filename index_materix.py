'''  [[0 0 0 0 0]
      [0 1 2 3 4]
      [0 2 4 6 8]]'''


def main(row: int, column: int) -> list:
    output = [[0 for col in range(column)] for row in range(row)]
    for i in range(row):
        for j in range(column):
            output[i][j] = i*j
    return output


if __name__ == "__main__":
    row = int(input("Enter a row: "))
    column = int(input("Enter a column: "))
    result = main(row, column)
    print(result)