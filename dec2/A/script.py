def input():
    return [item.rstrip('\n').split(',') for item in open("input.txt", 'r')][0]

def output(item):
    open("output.txt", 'w').write(str(item))

def run(l):
    l = [int(x) for x in l]
    l[1] = 12
    l[2] = 2
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
    output(run(input()))
