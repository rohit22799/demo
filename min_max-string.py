l = input().split(' ')
c = []
def longone(l):
    for i in l:
        c.append(len(i))
    temp = c.index(max(c))
    temp_min = c.index(min(c))
    print(l[temp])
    print(l[temp_min])
i = longone(l)