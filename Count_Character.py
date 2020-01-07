inp = input()
d ={}
for i in inp:
    d.update({i:inp.count(i)})
print(d)