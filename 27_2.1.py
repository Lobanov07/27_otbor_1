f=open('27_B_Lobanov_2.txt')
n=int(f.readline())
mas=[]
for i in range(n):
    s=f.readline().split()
    mas.append([int(s[0]),int(s[1])])
mas.sort()
k,kt,flag=0,1,0
for i in range(1,n):
    if mas[i-1][0]==mas[i][0]:
        kt+=1
    else:
        kt=1
        flag=0
    if kt>=3 and flag==0:
        if (mas[i][1] -mas[i-2][1]) <= 1440:
            k+=1
            flag=1
print(k)