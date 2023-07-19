f=open('27_A_Lobanov.txt')
n,k=map(int, f.readline().split())
mas=[]
for i in range(n):
    s=f.readline().split()
    snils=s[0]
    snils=snils[:3]+snils[-2:]
    sum=int(s[1])+int(s[2])+int(s[3])+int(s[4])
    mas.append([sum,int(s[1]),int(s[2]),int(s[3]),int(s[4]),snils])
mas.sort(reverse=True)
math,inf,rus=mas[k-1][1],mas[k-1][2],mas[k-1][3]
ans=mas[k-1][-1]
for i in range(k,n):
    if mas[i][1]==math and mas[i][2]==inf and mas[i][3]==rus:
        ans=mas[i][-1]
    else:
        break
print(ans)
