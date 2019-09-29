t=int(input())
for i in range(0,t):
    s=int(input())
    n=bin(s)
    n=n[2:][::-1]
    if n.count('1')==1:
        pos=n.find('1')+1
        print(pos)
    else:
        print('-1')
        t-=1