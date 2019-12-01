def input():
    return [item.rstrip('\n') for item in open("input.txt", 'r')]

def output(item):
    open("output.txt", 'w').write(str(item))

def run(list):
    return sum([int(int(item) / 3) - 2 for item in list])

if __name__ == '__main__':
    output(run(input()))
