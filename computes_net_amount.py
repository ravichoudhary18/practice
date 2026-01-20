total_amount = 0

def main(type_, amount):
    global total_amount  # fix 1

    if not amount.isdigit() or type_ not in ['D', 'W']:
        return

    amount = int(amount)

    if type_ == 'D':
        total_amount += amount
    elif type_ == 'W':
        total_amount -= amount


input_ = """
D 3000
W 2000
D 6000
W 2000
D 1000
"""

for line in input_.split('\n'):
    line = line.strip()
    if not line:   # fix 3
        continue

    value = line.split()
    main(value[0], value[1])

print(total_amount)
