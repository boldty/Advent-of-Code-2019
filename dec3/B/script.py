def input():
    return [item.rstrip('\n').split(',') for item in open("input.txt", 'r')]

def output(item):
    open("output.txt", 'w').write(str(item))

def run(data):
    l1, d1 = makeLines(data[0])
    l2, d2 = makeLines(data[1])
    con = []
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0

    for i in range(1,len(l1)):
        x1 = l1[i-1][0]
        x2 = l1[i][0]
        y1 = l1[i-1][1]
        y2 = l1[i][1]
        if x1 == x2:
            for j in range(1,len(l2)):
                if min(y1,y2) < l2[j][1] and max(y1,y2) > l2[j][1] and min(l2[j-1][0],l2[j][0]) < x1 and max(l2[j-1][0],l2[j][0]) > x1:
                    extraDist = abs(abs(l2[j-1][0]) - abs(x1)) + abs(abs(y1) - abs(l2[j-1][1]))
                    con.append((i,j,extraDist))
        elif y1 == y2:
            for j in range(1,len(l2)):
                if min(x1,x2) < l2[j][0] and max(x1,x2) > l2[j][0] and min(l2[j-1][1],l2[j][1]) < y1 and max(l2[j-1][1],l2[j][1]) > y1:
                    extraDist = abs(abs(l2[j-1][0]) - abs(x1)) + abs(abs(y1) - abs(l2[j-1][1]))
                    con.append((i,j,extraDist))

    return minDist(con,d1,d2)

def minDist(con,d1,d2):
    return min([d1[item[0]-1] + d2[item[1]-1] + item[2] for item in con])

def makeLines(list):
    dir = ''
    dist = 0
    distList = [0]
    x = 0
    y = 0
    ret = [(x,y)]

    for i in range(len(list)):
        dir = list[i][0]
        dist = int(list[i][1:])
        distList.append(distList[i] + dist)

        if dir == 'R':
            x += dist
        elif dir == 'L':
            x -= dist
        elif dir == 'U':
            y += dist
        elif dir == 'D':
            y -= dist
        ret.append((x,y))
    return ret, distList



if __name__ == '__main__':
    output(run(input()))
