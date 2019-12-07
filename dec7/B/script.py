import itertools

def read():
    return [item.rstrip('\n').split(',') for item in open("input.txt", 'r')][0]

def write(item):
    open("output.txt", 'w').write(str(item))

def add(i,l,a=0,b=0):
    A = l[l[i+1]] if a == 0 else l[i+1]
    B = l[l[i+2]] if b == 0 else l[i+2]
    l[l[i+3]] = A + B

    i += 4
    return i,l

def mul(i,l,a=0,b=0):
    A = l[l[i+1]] if a == 0 else l[i+1]
    B = l[l[i+2]] if b == 0 else l[i+2]
    l[l[i+3]] = A * B

    i += 4
    return i,l

def jumpIfTrue(i,l,a=0,b=0):
    if a == 0 and l[l[i+1]] != 0:
        return jumpFunc(i,l,b)
    elif a != 0 and l[i+1] != 0:
        return jumpFunc(i,l,b)
    return i+3

def jumpIfFalse(i,l,a=0,b=0):
    if a == 0 and l[l[i+1]] == 0:
        return jumpFunc(i,l,b)
    elif a != 0 and l[i+1] == 0:
        return jumpFunc(i,l,b)
    return i+3

def lessThan(i,l,a=0,b=0):
    A = l[l[i+1]] if a == 0 else l[i+1]
    B = l[l[i+2]] if b == 0 else l[i+2]
    l[l[i+3]] = 1 if A < B else 0

    i += 4
    return i,l

def equalsToo(i,l,a=0,b=0):
    A = l[l[i+1]] if a == 0 else l[i+1]
    B = l[l[i+2]] if b == 0 else l[i+2]
    l[l[i+3]] = 1 if A == B else 0

    i += 4
    return i,l

def jumpFunc(i,l,b):
    if b == 0:
        return l[l[i+2]]
    return l[i+2]

def output(i,l,val,c=0):
    if c==0:
        val = str(l[l[i+1]])
    else:
        val = str(l[i+1])
    i += 2
    return i,l,val

def run(l):
    l = [int(x) for x in l]
    codes = [5,6,7,8,9]
    memL = [l.copy() for i in range(len(codes))]
    memI = [0] * len(codes)
    psyInit =  [True] * len(codes)
    values = []

    codes = itertools.permutations(codes, len(codes))
    for c in codes:
        stack = [0]
        memL = [l.copy() for i in range(len(c))]
        memI = [0] * len(c)
        psyInit =  [True] * len(c)
        while memI[len(c)-1] != -1:
            for i in range(len(c)):
                if psyInit[i]:
                    stack.append(int(c[i]))
                    psyInit[i] = False
                memI[i] = runAmp(memL[i],stack,memI[i])
        values.append(stack.pop())
    return(max(values))

def runAmp(l,stack,i=0):
    val = 0
    par = []
    while i < len(l):
        if l[i] == 99:
            return -1
        par = [0] * 5
        for j in range(len(str(l[i]))):
            par[4-j] = int(str(l[i])[len(str(l[i]))-j-1])
        if par[4] == 1:
            i,l = add(i,l,par[2],par[1])
        elif par[4] == 2:
            i,l = mul(i,l,par[2],par[1])
        elif par[4] == 3:
            l[l[i+1]] = stack.pop()
            i += 2
        elif par[4] == 4:
            i,l,val = output(i,l,val,par[2])
            stack.append(int(val))
            return i
        elif par[4] == 5:
            i = jumpIfTrue(i,l,par[2],par[1])
        elif par[4] == 6:
            i = jumpIfFalse(i,l,par[2],par[1])
        elif par[4] == 7:
            i,l = lessThan(i,l,par[2],par[1])
        elif par[4] == 8:
            i,l = equalsToo(i,l,par[2],par[1])
        else:
            print("Faulty input")
            return -1
    return val

if __name__ == '__main__':
    write(run(read()))
