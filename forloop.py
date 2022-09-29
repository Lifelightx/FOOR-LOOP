
# for i in range(0,100,3):
#     print(i)



from cgi import print_arguments


lst1 = ["America","Delhi","Chenaai","pune"]
for i in lst1:
    print(i)




lst = [10,20,25,30,35]
sum = 0
for i in lst:
    print(i)
    sum = sum+i
print(sum)


num = 0
while num<10:
    num = 1+num
    print(num)
#arithmetic progression
sum = 0 
for i in range(1,101):
    sum = sum + i
print(sum)

n = 100
sum1 = n*(n+1)/2
print(sum1)

lst1 = [10,20,30,40,50]
sum = 0
for i in lst1:
    print(i)
    sum = sum + i
print("sum = ",sum)

#nested loop
for i in range(5):
    for j in range(6):
        print("i=",i,'\t'"j=",j)

for i in range(3):
    for j in range(2):
        for k in range(3):
            print("i=",i,"\t""j=",j,"\t""k=",k)
rows =5
for i in range(rows):
    for j in range(i+1):
        print(" * ",end='')
    print()

#pallindrum
x = input("Enter a word: ")
uper = x.upper()
y = uper[::-1]
print(y)
if uper ==y:
    print("The word is pallindrum")
else:
    print("The word is not pallindrum")

for i in range(10):
    print("*"*(i))

n = 40
for i in range(15):
    print(" "*n,end='')
    print("* " * (i))
    n = n-1

max = int(input("Enter a number: "))
for i in range(2,max+1):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(i)


for i in range(2,10):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print("The prime numbers are ",i)

for i in range(2,2):
    print(i)
#even numbers
for i in range(0,11,2):
    print(i)
for i in range(10):
    if i%2 == 0:
        print(i)
#odd numbers
for i in range(1,11,2):
    print(i)

for i in range(20):
    if i%2 != 0:
        print(i)
#obtaining sum
sum = 0
for i in range(11):
    sum = sum + i
print("sum = ",sum)    
#printin sum of even numbers
sum = 0
for i in range(11):
    if i%2 == 0:
        sum = sum + i
print("sum = ",sum)



for i in range(21):
    x = i**2
    print(f'square of {i} = {x} ')


sum = 0
for i in [15,20,30,40,50]:
    sum = i + sum
    lent = len([15,20,30,40,50])
avrg = sum/lent
x = int(avrg)
print("The average of the list = ",x)

#if else in a for loop
for i in range(21):
    if i%2 == 0:
        print(f"{i} is an even number")
    elif i%2 != 0:
        print(f"{i} is an odd number")

#break for a loop
for i in range(20):
    if i>15:
        break
    print(i)

#continue statement/pass statement
count = 0
name = "mariya mennen"
for i in name:
    if i != 'm':
        continue
    else:
        count = count+1
print(count)

num = [1,2,3,4,5]
for i in num:
    pass
else:
    print("done")

#In this example, We are printing print only the first two numbers out of 5, and after that, we use the break statement to stop the loop. Because the loop is terminated abruptly, the else block will not execute
for i in range(11):
    if i >2:
        break
    else:
        print(i)
print("done")

#reverse  the for loop
lst = [1, 2, 3, 4, 5, 6]
for i in reversed(lst):
    print(i)

#Reverse for loop using range()
for i in range(10,0,-1):
    print(i)

# Reverse a list using a loop
lst1 = [10, 20, 30, 40, 50]
x = lst1[::-1]
for i in x: 
    print(i)

#printin a pyramid using nested for loop 
for i in range(5):
    for j in range(i+1):
        print("*",end='')
    print()

'''The while loop is an entry-controlled loop, and a for loop is a count-controlled loop'''
m = int(input("Enter a number: "))
for i in range(1,11):
    res = i*m
    print(f"{m} X {i} = {res}")


for i in range(1,25):
    print('Multiplication table of:', i)
    count = 1
    while count < 11:
        m2 = i * count
        print(f"{i} X {count} = {m2}")
        count = count + 1
    print('\n')

for i in range(1,6):
    print("multiplication table of:",i)
    count = 1
    while count< 11:
        print(i*count,end=' ')
        count = count +1
    print('\n')    

num = [1, 4, 7, 8, 15, 20, 35, 45, 55]
for i in num:
    if i>15:
        break
    print(i)

x = int(input("Enter a number: "))
mul = 1
while mul< 11:
    n = mul * x
    print(f'{mul} X {x} = {n}')
    mul = 1+ mul

#for loop in one line
odd = [1, 3, 5, 7, 9]
for i in odd:
    m = i+1
    print([m])

even = [i+1 for i in odd]
print(even)

# num = [2,4,6,8,10]
# for i, v in enumerate(num):
#     print

x = str(123)
en = [ i for i in x]
print(en)
print(type(en))