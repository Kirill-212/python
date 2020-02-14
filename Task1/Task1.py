import  random

def retListElex(a,b,c):
    return  a+b+c
#Task1_1
print("Task1_1")
Num=(int)(input("Введите число:"))
i=1
col=0
while i<=Num:
    m=1
    for m in range(i):
        col+=1
        if col>Num:
            break;
        print(i,end=" ")
    i+=1


#Task1_4
print("\nTask1_4")
Num=(int)(input("\nВведите размер матрицы NxN:"))

matrix=[[random.randrange(0,1) for y in range(Num)] for x in range(Num)]

i=1
z=Num//2
k=1

while k<=z:
    if (Num**2)*2*Num<k:
        break;

    j=k-1
    while j<Num-k+1:
        matrix[k-1][j]=i
        i+=1
        j+=1


    j=k
    while j<Num-k+1:
        matrix[j][Num-k]=i
        i+=1
        j+=1

    j=Num-k-1
    while j>=k-1:
        matrix[Num-k][j]=i
        i+=1
        j-=1

    j=Num-k-1
    while j>=k:
        matrix[j][k-1]=i
        i+=1
        j-=1
    k+=1

if Num%2==1:
    matrix[Num//2][Num//2]=Num*Num
print()
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j],end=" ")
    print()

#Task1_3
print("Task1_3")
print()
matrix=[
    ["1 2 3 4 end"],
    ["5 4 10 4 end"],
    ["3 7 4 4 end"]
    ]
for i in range(len(matrix)):
    s=matrix[i][0]
    matrix[i][0]=matrix[i][0][:(int)(len(matrix[i][0])-3)]
    matrix[i]=matrix[i][0].split(' ', maxsplit=3)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j]=int(matrix[i][j])
        print(matrix[i][j],end="   ")
    print()

#складываем углы матрицы
q=int(len(matrix[0]))-1
w=int(len(matrix))-1
b=matrix[0][0]
c=matrix[0][q]
d=matrix[w][0]
e=matrix[w][q]
matrix[0][0]=retListElex(c,d,b)
matrix[0][q]=retListElex(b,c,e)
matrix[w][0]=retListElex(b,d,e)
matrix[w][q]=retListElex(d,e,c)
#складываем верхние,нижние,правые и левый границы кроме углов
i=0
j=0
matrix1=matrix
while i<len(matrix):
    j=0
    while j<len(matrix[0]):
        if i==0:
            if j==int(len(matrix[0]))-1:
                j += 1
                continue
        elif i==int(len(matrix))-1:
            if j==0:
                j += 1
                continue
        elif i==0:
            if j==0:
                j += 1
                continue
        elif i==int(len(matrix))-1:
            if j==int(len(matrix[0]))-1:
                j += 1
                continue
        elif i==0:
            b=matrix[i][j]
            c=matrix[int(len(matrix))-1][j]
            matrix[i][j]=b+c
            matrix[int(len(matrix))-1][j]=b+c
        elif j==0:
            b = matrix[i][j]
            c = matrix[i][int(len(matrix[0]))-1]
            matrix[i][j] = b + c
            matrix[i][int(len(matrix[0]))-1] = b + c
        elif j!=0 and i!=0 and j!=int(len(matrix[0]))-1 and i!=int(len(matrix))-1:

            b=matrix1[i-1][j]
            b+=matrix1[i][j-1]
            b+=matrix1[i+1][j]
            b+=matrix1[i][j+1]
            matrix[i][j]=b
        j+=1
    i+=1

print()
lst=[]
for i in range(len(matrix)):
    str1=""
    str1=str(matrix[i])+" end"
    lst.append(str1)


for i in range(len(lst)):
    lst[i]=lst[i].replace(']',' ')
    lst[i]=lst[i].replace('[', ' ')
    lst[i]=lst[i].replace(',', ' ')
for i in range(len(lst)):
    print(lst[i])

#Task1_2
print("Task1_2")
flag=False
matrix=list(map(int,input("Введите последовательность через пробел").split()))
Num=int(input("Введите число для поиска:"))
for i in range(len(matrix)):
    if matrix[i]==Num:
        flag=True
        print(i,end=" ")

if flag==False:
    print("Отсуствует")