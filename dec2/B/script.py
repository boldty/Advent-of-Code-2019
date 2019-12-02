import copy

def input():
    return [item.rstrip('\n').split(',') for item in open("input.txt", 'r')][0]

def output(item):
    open("output.txt", 'w').write(str(item))

def run(list, goal):
    list = [int(x) for x in list]
    numA = 0
    numB = 0

    val = runWithParam(copy.copy(list),0,0)
    difA = runWithParam(copy.copy(list),1,0) - val
    difB = runWithParam(copy.copy(list),0,1) - val
    while val != goal:
        if difA > difB and val + difA <= goal:
            numA += 1
            val += difA
        elif difA > difB and val + difA > goal:
            numB += 1
            val += difB
        elif difA < difB and val + difB <= goal:
            numB += 1
            val += difB
        elif difA < difB and val + difB > goal:
            numA += 1
            val += difA
    return f'{numA:02}' + f'{numB:02}'

def runWithParam(l, a, b):
    l[1] = a
    l[2] = b
    for i in range(0, len(l), 4):
        if l[i] == 1:
            l[l[i+3]] = l[l[i+1]] + l[l[i+2]]
        elif l[i] == 2:
            l[l[i+3]] = l[l[i+1]] * l[l[i+2]]
        elif l[i] == 99:
            break
        else:
            print("Faulty input")
            return -1
    return l[0]

if __name__ == '__main__':
    output(run(input(),19690720))
