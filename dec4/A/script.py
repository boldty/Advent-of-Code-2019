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
    sameFollow = False
    d0 = 0
    d1 = 0
    for i in range(len(val)-1):
        d0 = val[i]
        d1 = val[i+1]
        if d0 > d1:
            return False
        elif d0 == d1:
            sameFollow = True
    return sameFollow


if __name__ == '__main__':
    output(run(input()))
