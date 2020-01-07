l = input().split(' ')
c = []
d={}
def longone(l):
    for i in l:
        c.append(len(i))
    temp = c.index(max(c))
    temp_min = c.index(min(c))
    print(l[temp])
    print(l[temp_min])
    d['longest'] = l[temp]
    d['shortest'] = l[temp_min]
    print(d)
i = longone(l)