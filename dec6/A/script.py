def read():
    return [item.rstrip('\n').split(')') for item in open("input.txt", 'r')]

def write(item):
    open("output.txt", 'w').write(str(item))

def run(data):
    dic = {i[1] : i[0] for i in data}
    it = iter(dic.keys())
    tot = 0
    for i in it:
        j = 0
        while i != "COM":
            i = dic.get(i)
            j += 1
        tot += j
    return tot

if __name__ == '__main__':
    write(run(read()))
