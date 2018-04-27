n,k = map(int,input().strip().split())
cont = []
cont_i = []
cont_l = []
luck = 0

for i in range(n):
    cont.append(list(map(int,input().strip().split())))

cont.append([0,1])

cont = sorted(cont, key = lambda x: x[1])

for i,j in enumerate(cont):
    if j[1] != 0:
        cont_i = cont[i:]
        cont_l = cont[:i]
        break

if cont_i:    
    cont_i = sorted(cont_i, key = lambda x: x[0])[::-1]

luck += sum(i[0] for i in cont_l)
luck += sum(i[0] for i in cont_i[:k])
luck -= sum(i[0] for i in cont_i[k:])

print(luck)
    
