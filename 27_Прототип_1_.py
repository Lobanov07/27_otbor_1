f=open('27_B_Lobanov.txt')
n,k=map(int, f.readline().split())  #Cчитываем входные данные
mas=[] 
for i in range(n):
    s=f.readline().split()
    snils=s[0]
    snils=snils[:3]+snils[-2:] # создаём из снилса комбинацию, нужную для ответа
    sum=int(s[1])+int(s[2])+int(s[3])+int(s[4])
    mas.append([sum,int(s[1]),int(s[2]),int(s[3]),int(s[4]),snils])
    #заполняем массив в порядке, удобном для сортировки
mas.sort(reverse=True)
math,inf,rus,ID=mas[k-1][1],mas[k-1][2],mas[k-1][3],mas[k-1][4]
#запоминаем результаты егэ и ИД у человека, занявшего последнее бюджетное место
# на случай полного совпадения результата
ans=mas[k-1][-1] # запоминаем снилс у человека, занявшего последнее бюджетное место

for i in range(k,n):
    if mas[i][1]==math and mas[i][2]==inf and mas[i][3]==rus and mas[i][4]==ID:
        ans=mas[i][-1]
    else:
        break
    # С помощью цикла проверяем есть люди с полным совпадением баллов 
print(ans)


