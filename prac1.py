# 1
fruitList = ["grape","orange","mango","apple","peach"]
# 2
for fruit in fruitList:
    if fruit == "apple":
        print ("I found it")
# 3
fruitList.append("pinapple")
fruitList.append("banana")
# 4
fruitLength = []
for fruit in fruitList:
    fruitLength.append(fruit + " has " + str(len(fruit)) + " letters " )
# 5
def half_squared(original):
    result = []
    for element in original:
        results = (element*element)/2.0
        result.append(results)
    return result

# print half_squared([3,3])
# 6
'''
scoreList=[]
score1 = int(input("please input the score:"))
score2 = int(input("please input the score:"))
score3 = int(input("please input the score:"))
scoreList.append(score1)
scoreList.append(score2)
scoreList.append(score3)

for score in scoreList:
    if(score<0 or score>100):
        print ("Please input the right score.")
    elif(score>=90):
        print ("A")
    elif(score<=60):
        print ("C")
    else:
        print ("B")
'''
# 7
def revSort(a,b,c):
    if (a>b>c):
        a,b,c=a,b,c
    if (a>c>b):
        b,c=c,b
    if (b>a>c):
        a,b=b,a
    if (b>c>a):
        a,b,c=b,c,a
    if (c>a>b):
        a,b,c=c,a,b
    if (c>b>a):
        a,c=c,a
    return a,b,c

# print revSort(12,4,32)

# 8
arrs = [[1,2,3],[4,5,6]]
for i in arrs:
    for j in i:
        print(j)

# 9
for i in range(1,100):
    if i ==sum(map(int,str(pow(i,3)))):
        print(i)

# 10
def exchange(a,b):
    a,b = b,a
    return a,b
import random
x=random.randint(1,10)
y=random.randint(1,10)
print (x,y)
print (exchange(x,y))

# 11
s = '*'
for i in range(1,8,2):
    print((s*i).center(7))
for i in reversed(range(1,6,2)):
    print ((s*i).center(7))

# 12
for i in range(1,7):
    for j in range(i,7):
        print(j,end="")
    for k in range(1,i):
        print(k,end="")
    print()

# 13
players = ['charles','martina','michael','florence','eli']
for elements in players:
    print(elements.title())
