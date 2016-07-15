import sys

x = 223336226

k = map(int, str(x))

g1=[]
for i in range(len(k)-1):
    g=[]

    if k[i]==k[i+1]:
        g = k[:i]+k[i+1:]
    if len(g)!=0:
        g = ''.join(str(n) for n in g)
        g1.append(int(g))

print g1
print max(g1)