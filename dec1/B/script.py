def input():
    return [item.rstrip('\n') for item in open("input.txt", 'r')]

def output(item):
    open("output.txt", 'w').write(str(item))

def run(list):
    return sum([fuelCalc(int(item)) for item in list])

def fuelCalc(val):
    val = int(val / 3) - 2
    return 0 if val <= 0 else val + fuelCalc(val)
    return val

if __name__ == '__main__':
    output(run(input()))
