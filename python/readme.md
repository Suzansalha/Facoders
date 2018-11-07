*week 4 : introduction to python : if statement, while loop.

**week 4-1:-

x=float(input("enter anumber:"))

if x % 2 == 0:
    print("number is even")
else:
    print("number is odd")





**week 4-2:-


print("number from 1 to 10")

n=3
x=int(input("guess the number:"))
if x == n:
    print('great! you did it!')
while x!=n:
    input("guess the number:")
    continue
    x += 1
