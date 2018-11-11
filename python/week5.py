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
