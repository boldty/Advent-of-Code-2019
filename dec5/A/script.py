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

def output(i,l,val,c=0):
    if c==0:
        val = str(l[l[i+1]])
        print("Output: " + val)
    else:
        val = str(l[i+1])
        print("Output: " + val)
    i += 2
    return i,l,val

def run(l):
    l = [int(x) for x in l]
    i = 0
    val = 0
    par = []
    while i < len(l):
        if l[i] == 99:
            break
        par = [0] * 5
        for j in range(len(str(l[i]))):
            par[4-j] = int(str(l[i])[len(str(l[i]))-j-1])
        if par[4] == 1:
            i,l = add(i,l,par[2],par[1])
        elif par[4] == 2:
            i,l = mul(i,l,par[2],par[1])
        elif par[4] == 3:
            l[l[i+1]] = int(input("Enter ID: "))
            i += 2
        elif par[4] == 4:
            i,l,val = output(i,l,val,par[2])
        else:
            print("Faulty input")
            return -1
    return val

if __name__ == '__main__':
    write(run(read()))
