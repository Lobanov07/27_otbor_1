f=open('27_A_Lobanov_2.txt')
n=int(f.readline())
mas=[]
for i in range(n):
    s=f.readline().split()
    mas.append([int(s[0]),int(s[1])])
mas.sort()
k=0
dictionary={}
for i in range(n):
    id=mas[i][0]
    time=str(mas[i][1])
    if id in dictionary:
        dictionary[id].append( time )
    else:
        dictionary[id]=[]
        dictionary[id].append( time )
for x,y in dictionary.items():
    if len(y) >= 3:
        for i in range(2,len(y)):
            if (int(y[i]) - int(y[i-2])) <=1440:
                k+=1
                break
print(k)
