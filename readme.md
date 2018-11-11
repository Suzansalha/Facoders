## Female Arab Coders Initiative
## مبادرة نساء مبرمجات

Name: Suzan Salha

*_week -1:_

    [Introduction to Git and GitHub](https://github.com/Suzansalha/udemy-git.git)

*_week -2:_

    Creating Markdown File



*_week -3:_

    Introduction to Python: Numbers and Strings

    print("hello "+input("Enter your name: "))




*_week -4:_

    Introduction to Python: If statement, While loop


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






**week-5: Lists and for loop


s1 =['ahmad',18,17,19.5,8,25]
s2 =['sami',20,20,19,9,28]
s3 =['faris',14.5,16,13,7,23]

s4=[s1[0],s2[0],s3[0]]

n=input("enter student's name : ")


if n == s1[0]:
    print('ahmad',float(sum(s1[1:6])))

if n == s2[0]:
    print('sami',float(sum(s2[1:6])))

if n == s3[0]:
    print('faris',float(sum(s3[1:6])))

if n not in s4:
    print("student's is not recorded , 0")
