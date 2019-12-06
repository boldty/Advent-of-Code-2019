def read():
    return [item.rstrip('\n').split(')') for item in open("input.txt", 'r')]

def write(item):
    open("output.txt", 'w').write(str(item))

def run(data):
    dic = {i[1] : i[0] for i in data}
    route1 = routeToCentre(dic,"YOU")
    route2 = routeToCentre(dic,"SAN")
    route1 = list(set(route1)^set(route2))
    return len(route1)

def routeToCentre(dic,pos):
    temp = dic.get(pos)
    route = [temp]
    while temp != "COM":
        temp = dic.get(temp)
        route.append(temp)
    return route

if __name__ == '__main__':
    write(run(read()))
