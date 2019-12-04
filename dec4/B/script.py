def input():
    return [item.rstrip('\n').split('-') for item in open("input.txt", 'r')][0]

def output(item):
    open("output.txt", 'w').write(str(item))

def run(data):
    val = int(data[0])
    end = int(data[1])
    i = 0
    while val <= end:
        if checkIfTrue(val):
            i += 1
        val += 1
    return i

def checkIfTrue(val):
    val = [int(d) for d in str(val)]
    sameTwo = set()
    sameMore = set()
    d0 = 0
    d1 = 0
    d2 = 0
    for i in range(len(val)-2):
        d0 = val[i]
        d1 = val[i+1]
        d2 = val[i+2]
        s = set()
        if d0 > d1 or d1 > d2:
            return False
        elif d0 == d1:
            sameTwo.add(d0)
        elif d1 == d2:
            sameTwo.add(d1)
        if d0 == d1 and d1 == d2:
            sameMore.add(d0)
    return False if len((sameTwo^sameMore)) == 0 else True


if __name__ == '__main__':
    output(run(input()))
