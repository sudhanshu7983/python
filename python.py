
# '''a=10
# b=12
# print(a,b,stp=',')'''


# #****
# '''print("hello ",end='')
# print("gla",end='')'''

# #****
# #print formating string 
# '''x=10
# print("value=%i"%x)'''


# #****

# '''name ='hiilinda'
# print('hi (%20s)'% name)'''


# #****
# '''num =12.3678
# print("the value is %.1f"%num)'''

# '''a= int(input("Enter first number"))
# b=int(input("enter second number "))
# avg =(a+b)/2
# print("a and b is",avg)
# n = int(input("enter a num a"))
# a=0 
# b=1
# if n<=0:
#     print("please enter a pos")
# else:
#     print(a,b)
#     for n in range(2,n):
#         c =a+b
#         a=b
#         b=c 
#         print(c)
#         num = int(input("enter a num"))
# rev=0
# wnum =num
# while(wnum>0):
#  digit=wnum%10
#  rev=rev*10+digit 
#  wnum =wnum//10
#  if(num==rev):
#   print("palindrome")
#  else:
#   ("print not palindrome")
#   """for num in range(100,200):
#     rem =0
#     for i in range (1,num+1):
#         if  num%i==0:
#             rem+=1

#     if rem==2:
#         print(num)"""


# """string =["sudhanshu","puneet","","fvjfvj"]
# for i in range [-1:0:-1]:
#  print(string)
 
# for i in range(1, 4):
#     print(i)
# else:  # Executed because no break in for
#     print("No Break")"""


# lst= list(map(int,input().split()))
# max =lst[1]
# for i in range (1,len(lst)):
#     if lst[i]>max:
#         max=lst[i]
# print("msdfgh",max)

#         a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
 
# HCF = 1
 
# for i in range(2,a+1):
#     if(a%i==0 and b%i==0):
#         HCF = i
 
# print("First Number is: ",a)
# print("Second Number is: ",b)
# print("HCF of the numbers is: ",HCF)
# for i in range(2,a+1):
#     if(a%i==0 and b%i==0):
#         HCF = HCF
 
# print("First Number is: ",a)
# print("Second Number is: ",b)
 
# LCM = int((a*b)/(HCF))
# print("LCM of the two numbers is: ",LCM)'''
# ######################################################
# '''
# l1=[], l2=[], l3=[  ] 
# for i in range (4):
#     a =list(map(int,input().split()))[0:3]
#     b =list(map(int,input().split()))[0:3]
#     l1.append(a)
#     l2.apeend(b)
# for i in range (3):
#     l3.append([])
#     for j in range(3):
#         l3[i].append(l1[i][j]+l2[i][j])
# for i in l3:
#     print(i)'''
#     #type of loops in python
# # 1. while 

# '''i=0
# while i<10:
#     print("yes "+ str(i))
#     i=i+1
#     print("done ")'''
# #*********************************
# '''i=1
# while i<=5:
#         print("harry")
#         i=i+1
      
# fruits =['banana','apple','grapes']
# i=0 
# while i<len(fruits):
#     print(fruits[i])
#     i=i+1'''

#     #************************
#     #FOR LOOPS
# '''fruits =['banana','apple','grapes']
# for item in fruits:
#     print(item)
# else:
#     print("DONE")
#     #***********************
# for i in range(2,12):
  
#   print(i)
# else:
#     print("done")'''
# #*************************
# #break
# '''for i in range(10):
#  print(i)
#  if i ==5:
#     break'''
# #******************
# #continue
# '''for i in range(10):
#     if i==3:
#         continue
#     print(i)
#      '''
# '''i =4
# if i>0:
#  pass
# while i>6:
#     pass
# print("sudhanshu is a very smart boy")'''
# #*****************
# '''num = int(input('enter the num'))
# for i in range(11,1):
#  print(str(num)+ "*" + str(i) + "=" + str(i*num))'''
#   #********************************
# '''list =["harry","sohan","sudhanshu","chashmish"] 
# for name in list:
#     if name.startswith("c"):
#         print("hello"+name)

#         #********************

#  num = int(input("enter the rows"))
# for i in range (num):
#  print("*" * num)
#  print(" " * (num-i-1), end="")
#  print("*"* (2*i+1), end="")
#  print(" " * (num-i-1) ) '''
#  #**********************
# #print('hello puneet')
# # a=input('enter')
# # b=input('enter')
# # c=a+b
# # print(c)
# # a=int(input('enter'))
# # b=float(input('enter'))
# # c=a+b
# # print(c)
# # a=int(input('enter'))
# # b=int(input('enter'))
# # c=a*b
# # print(c)
# # a=int(input('enter'))
# # b=int(input('enter'))
# # c=a*b
# # p=2*(a+b)
# # print(c)
# # print(p)
# # a=int(input('enter'))
# # b=int(input('enter'))
# # c=a//b
# # print(c)
# # a=float(input('enter'))
# # b=3.14*(a**2)
# # c=2*(3.14*a)
# # print(c)
# # print(b)
# # a=int(input('enter'))
# # h=int(input('enter'))
# # r=(a//3.14)**0.5
# # t=(2*3.14*r)*(r+h)
# # print(r)
# # print(t)
# # important
# # a=int(input('enter'))
# # b=int(input('enter'))
# # c=a/b
# # print(f'divides{c}')
# # a=float(input('length'))
# # b=float(input('breadth'))
# # c=float(input('length'))
# # d=float(input('bradth'))
# # floor=a*b
# # tile=c*d
# # print('no of tiles',floor//tile)
# # m=int(input('enter'))
# # d=(m<=7)*((m%2)+30)+(m>7)*((m%2==0)+30)-(m==2)*2
# # print(d)
# # a=10
# # b=5
# # print(a,'divides',b,'=',a//b)
# # a=10
# # b=5
# # print(a,'divides',b,'=',a//b,sep='\n')
# # a=10
# # b=5
# # print(a,end='/')
# # print(b,end='=')
# # print(a//b)
# # a=10
# # b=5
# # print(a)
# # print(b)
# # print(a//b)
# # a=10
# # b=3
# # print(a)
# # print(b)
# # print(a/b
# # a=10
# # b=5
# # print('{0} divide {1}is {2}'.format(a,b,a/b))
# # a=10
# # b=5
# # print(f'{a} divide {b}is {a/b}')
# # a=10
# # b=5
# # print(f'{a} divide {b}is {a/b}')
# # print('%d divide %d is %.2f'%(a,b,a/b))
# #take side of triangle from user and make them, to a isoscacles,equilateral,invalid
# # a=int(input("enter the 1st side"))
# # b=int(input("enter the 2nd side"))
# # c=int(input("enter the 3rd side"))
# #if(a=b and b=c and a=c):
# #     print('equi')
# # if(a!=b and b!=c and c!=a):
# #     print("scalene triangle")
# # elif((a==b) or (b==c) or (c==a)):
# #     print("isosceles triangle")
# # elif((a==((b*b+c*c)**(1/2))) or (b==((a*a+c*c)**(1/2))) or (c==((b*b+a*a)**(1/2)))):
# #     print("right angle triangle ")
# # elif(a>(b+c) or b>(a+c) or c>(a+b)):
# #     print("invalid")
# # a=int(input('enter the n0.'))
# # b=int(input('enter the no.'))
# # c=int(input('enter the no.'))
# # if(a>b and a>c):
# #   print(a)
# # elif(b>a and b>c):
# #   print(b)
# # elif(c>a and c>b):
# #   print(c)
# # a=int(input('enter the point'))
# # b=int(input('enter the point'))
# # if(a>0 and b>0):
# #  print('1st quad')
# # elif(a>0 and b<0):
# #  print('2nd quad')
# # elif(a<0 and b>0):
# #   print('4th quad')
# # elif(a<0 and b<0):
# #   print('3rd quad')
# # elif(a==0 and b==0):
# #   print('origin')
# # elif(a==0 and b!=0):
# #   print('y axis')
# # elif(a!=0 and b==0):
# #   print('x aXIS')
# '''ake coordinates of center of cicle and coordinates of an arbitary point from user and check it lies inside or outside the circle'''
# # a=int(input('coordinate 1'))
# # b=int(input('coordinate 2'))
# # ar=int(input('area'))
# # c1=int(input('arbitary coordinate 1'))
# # c2=int(input('arbitary coordinate 1'))
# # r=(ar*(7/22))**(1/2)
# # d=((a-c1)*(2)+(b-c2)**(2))**(1/2)
# # if(d<r):
# #   print('inside the circle')
# # elif(d==r):
# #   print('on boundary')
# # else:
# #   print('outside')
# ''' perfect number'''
# # a=int(input())
# # b=0
# # for i in range(1,a):
# #   if(a%i==0):
# #     b+=i
# #   print(b)
# # if(b==a):
# #       print('perfect')
# # else:
# #     print('not')
# ''' prime number
# a=int(input())
# for i in range(2,a):
#    if a%i==0:
#      print("not prime")
#      break
#    else:
     
#      print("prime")'''
# '''armstrong nuber'''
# # n=int(input())
# # s=0
# # l=len(str(n))
# # for i in str(n):
# #   s=s+(int(i)**l)
# # if s==n:
# #   print("arm")
# # else:
# #   print("not")
# '''factorial no.'''
# # n = input("Enter a number: ")
# # factorial = 1
# # if int(n) >= 1:
# #  for i in range (1,int(n)+1):
# #   factorial = factorial * i
# # print("Factorail of ",n , " is : ",factorial)
# ''' strong number'''
# # sum1=0
# # num=int(input("Enter a number:"))
# # temp=num
# # while(num):
# #     i=1
# #     f=1
# #     r=num%10
# #     while(i<=r):
# #         f=f*i
# #         i=i+1
# #     sum1=sum1+f
# #     num=num//10
# # if(sum1==temp):
# #     print("The number is a strong number")
# # else:
# #     print("The number is not a strong number")           
# '''OR'''
# # n=int(input())
# # s=0
# # for i in str(n):
# #   f=1
# #   for j in range(1,int(i)+1):
# #     f=f*j
# #   s=s+f
# # if s==n:
# #   print("strong")
# # else:
# #   print("not")
# '''    *
#       **
#      ***
#     ****
#    ***** 
#      '''
# # n=int(input())
# # for i in range(1,n+1):
# #   print(' '*(n-i)+'*'*i)
  
# ''' a
#    ab
#    abc
#    abcd
#    abcde
#   '''
# # n=int(input())
# # for i in range(1,n+1):
# #   for j in range(i):
# #     print(chr(65+j),end='')
# #   print()
# ''' out put dekh liyo   
# n=int(input())
# for i in range(1,n+1):
#    print(''*i+' '*(2(n-i))+'*'*i)
#  panagram '''
# # s=input()
# # c=65
# # e=0
# # l=s.upper()
# # n=[*l]
# # for i in range(26+1):
# #   d=chr(c)
# #   if d in n:
# #     n.remove(d)
# #     e+=1
# #     c+=1
# # print('yes') if e==26 else print('no')    
# '' 'or'''
# # s=input()
# # s1=s.lower()
# # for i in range(97,123):
# #   if chr(i) not in s1:
# #     print("not")
# #     break
# # else:
# #   print("pana")
# ''' anagram'''
# # s=input()
# # a=[*s]
# # n=input()
# # b=[*n]
# # c=0
# # for i in a:
# #   if i in b:
# #     c+=1
# # if c==len(a):
# #   print("yes")
# # else:
# #   print("no")
# '''sorted method'''
# # s=input()
# # l=sorted(s)
# # l1=sorted(s,reverse=True)
# # print(l)
# # print(l1)
# # s1=' '.join(l)
# # s2=' '.join(l1)
# # print(s1)
# # print(s2)
# '''or''' 
# # s1=input().upper()
# # s2=input().upper() 
# # if sorted(s1)==sorted(s2):
# #   print("ana")
# # else:
# #   print('not')
# '''slicing'''
# # s="abhimanyu"
# # print(s[-8:8])
# # print(s[::-1])
# # print(s[-9])
# # print(s[8:-8:-1])
# '''to take list from user and print their sum '''
# # l=list(map(int,input().split()))[0:]
# # print(sum(l))
# # print(max(l))
# # print(len(l))
# '''take list from user and take odd number '''
# # n=int(input())
# # l=list(map(int,input().split()))[0:n]
# # b=[]
# # c=[]
# # for i in range(n):
# #   if i%2==0:
# #     b.append(i)
# #   else:
# #     c.append(i)
# # print("even=",b)
# # print("odd=",c)
# '''merge the list'''
# # l1=list(map(int,input().split()))[0:]
# # l2=list(map(int,input().split()))[0:]
# # print(l1+l2)
# '''remove the duplicacy also of union '''
# # l1=list(map(int,input().split()))[0:]
# # l2=list(map(int,input().split()))[0:]
# # l3=l1+l2
# # s=set(l3)
# # l=list(s)
# # print(l)
# '''W.A.P.P to remove duplicacies of each element in list'''  
# '''l=list(map(int,input().split()))[0:]
# i=0
# n=len(l)
# while(i<n):
#    if l[i] in l[i+1:]:
#     del l[i]
#     i-=1
#     n-=1
#    i+=1
# print(l)'''  
# '''frequency of each element in given string'''
# # s=input()
# # re=' '
# # for i in s:
# #   if i not in re:
# #     print(f'{i}={s.count(i)}')
# #     re+=i

# ''' good
# s=input()
# l=s.split()
# for i in range(len(l)):
#   l[i]=l[i][::-1]
# s=' '.join(l)
# print(s)
# alag code 
# num=345
# c=0
# for i in  range(0,10):
#   print(i)'''

# '''
# s=['my','india','is','great']
# s.insert(0,"sudh")
# print(s)'''
# '''s='Puneet Bhardwaj us very good'
# a=s.split(' ')
# print(a)'''

# '''s=input()
# c=s.split()
# print(c[::-1]
# lst='hello python programming'.split()
# slc=lst[-1:0:-1]
# print(slc,type(slc))'''

# #o=int(input())
# #for i in range(o,-1,-1):
#  #   print('*'*i+' '*(2*o-2*i)+'*'*i)


#  #new topic module
# # there are two type
# #lib
# ##############
# '''n = int(input())
# l=[[n,
#     i,n*i] for i in range (1,11)]
# for i in l:
#     print(i)
#     ####dictonary####
# d={ }
# n = int(input( ))
# for i in range(n):
#    k=input()
#    x= input()
#    d[k]=x
# print(d)   









# with open('abc.txt', 'r') as file:
#   lines = file.readlines()
#   print('First',  'lines:')
#   for i in lines [:1] :
#        print(i.strip())
#   print('Last',  'lines:')
#   for line in lines[-1:]:
#        print(line.strip())



# t=input()
# a=open('file.txt','r')
# print(a.read())
# b=open('abc.txt','r') 
# print(b.read())


# with open('file.txt','r') as f:
#         l=f.read()
#         print(f.read())
# with open('file.txt','w') as f:
    # f.write(l)
   
# # #4
# a=[]
# b=[]
# d={}
# with open('abc.txt','r') as f:
#     a=(f.read()).split()
# for i in a:
#     if i not in b:
#         b.append(i)
#         d[i]=a.count(i)
# print(d)

# # #5
# a=list(map(eval,input().split()))
# b=list(map(eval,input().split()))
# d={}
# for i in range(len(a)):
#     d[a[i]]=b[i]
# print(d)
# '''
# # #6
# # m=0
# # d={}
# # for i in range(int(input('enter total keys='))):
# #     a=eval(input('enter key='))
# #     b=eval(input('enter value='))
# #     d[a]=b
# # for i in d:
# #     if m<len(d[i]):
# #         m=len(d[i])
# # print(m)

# # 7
# '''
# def fun(a,b):
#     r={**a,**b}
#     return r
# a=eval(input())
# b=eval(input())
# print(fun(a,b))
# '''
# # #8
# '''
# def fun(a,b):
#     a=a.update(b)
# a=eval(input())
# b=eval(input())
# fun(a,b)
# print(a)

# # #9
# try:
#   a=int(input())  
#   b=int(input())
#   print(a/b)
#   print(a+b+'abc')
# except (ZeroDivisionError,ValueError,TypeError) as e:
#    print(e)


# import os

# if os.path.exists("abc.txt"):
#     os.remove("abc.txt")
  
#     # Print the statement once
#     # the file is deleted 
#     print("File deleted !") 
  
# else:
  
#     # Print if file is not present 
#     print("File doesnot exist !") 

# out =print("hello") or print("python")
# print(out,type(out))
# ''' 

#  ########################
# """for num in range(100,200):
#     rem =0
#     for i in range (1,num+1):
#         if  num%i==0:
#             rem+=1

#     if rem==2:
#         print(num)"""


# """string =["sudhanshu","puneet","","fvjfvj"]
# for i in range [-1:0:-1]:
#  print(string)
#  for num in range(100,200):
#     rem =0
#     for i in range (1,num+1):
#         if  num%i==0:
#             rem+=1

#     if rem==2:
#         print(num)


# string =["sudhanshu","puneet","","fvjfvj"]
# for i in range [-1:0:-1]:
#  print(string)
 
# for i in range(1, 4):
#     print(i)
# else:  # Executed because no break in for
#     print("No Break")


# lst= list(map(int,input().split()))
# max =lst[1]
# for i in range (1,len(lst)):
#     if lst[i]>max:
#         max=lst[i]
# print("msdfgh",max)
 
# for i in range(1, 4):
#     print(i)
# else:  # Executed because no break in for
#     print("No Break")


# lst= list(map(int,input().split()))
# max =lst[1]
# for i in range (1,len(lst)):
#     if lst[i]>max:
#         max=lst[i]
# print("msdfgh",max)"""


# """import numpy as np
# a =np.array[[[0,1,0],[1,0,1]]]
# a+=3
# b=a+3
# print(a[1,2]+b[1,2])
# """
# n ={"sudh":5,"1234":'India' }
# print(n)
# k=input('Enter key=')
# v=input('enter value=')
# n.update(k=v)
# n[k]=v
# print(n)

# a={(2,3):'harsg',4:'aaa',1:'sjs',5:'shsh'}
# b=a[2,3]
# print(b)
# print(a.get(2,3))


# arr={}
# arr[1]=1
# arr["1"]=2
# arr[1]+=4

# sum = 0
# for k in arr:
#     sum +=arr[k]
# print(sum)

# wap to join to dictionary by value and keys value is the sum and keys should be same 

# dict1={1:('a','b'),2:('b','c')}
# for x in dict1:
#  w=dict1[1]
#  print(w)
# for y in dict1:
#  z=dict1[2]
# #  print(z)

# n="s3wexd3ssrtfy"
# a=list(n)
# count=0
# for i in range(1,len(a)):
#     for j in range(2,len(a)):
#         if(a[i]==a[j]):
#             count+=1
#             temp=a[i]
#             a[i]=a[j]
#             a[j]=temp
# print(count)


# dict={"roll no":(61,"ankiashe"),"roll no ":(62,"sty"),"roll no": (63,"dfgh")}
# l1=sorted(dict)
# print(l1)
# w= dict["roll no"]
# print(w)
# y=sorted(w)
# print(y)


# special=['@','$','#']
# n = input("enter the paasword ")
# if len(n)>10 and len(n)<11:
#  print()

# else:
#     print("lenth of paasword is not in certain range ")

# if not any(char.isupper() for char in n):
#     print("please inpt at least one character in uppeer cae ")
# if not any(char in special for char in n):
#     print("please enter a special charter in your pass")
# else
#     print("your lock paasword is ",n) 



# l =[1,2,3,4,5,6,7,8,9]
# y= [i*i for i in l if i%2!=0] 
# print(y)

# string=input("")
# output={}
# for i in string:
#     keys=output.keys
#     if i  not in  keys:
#         output[i]=1
#     else:
#         output[i]+=1
# print(output)

# dict={'sudh':1323,"sdfijckdj":232,"dsf":4}
# x=sorted(dict)
# print(x,end=" ")
# with open('file.txt','r') as f:
#        l=f.read()
#        print(f.read())
# with open('file.txt','w') as f:
#         f.write(l)
#         f.close()
# import numpy as np
#     # Create the original large random int array with specified shape (8x3)
# arr = np.random.randint(low=10, high=35, size=(8, 3))
    
#     # Split the array horizontally at position 3 vertically 
# left_arr, right_arr = np.hsplit(arr, [3])
    
    # Print info on both halves of the new arrays
# for i, half_array in enumerate([left_arr, right_arr]):
#         print("Array {}:".format(i+1))
#         print("\tShape:", half_array)
     
# import numpy as np
 
# R = int(input("Enter the number of rows:"))
# C = int(input("Enter the number of columns:"))
 
 
# print("Enter the entries in a single line (separated by space): ")
 
# User input of entries in a 
# single line separated by space
# entries = list(map(int, input().split()))
# entries1 = list(map(int, input().split()))
# # For printing the matrix
# matrix = np.array(entries,entries1).reshape(R, C)

 
# result=np.dot(entries,entries1)  
# print(result) 
try:
    try:
        raise TypeError
    except ValueError:
        print("inner Exception handled ")
    print("next command")
except TypeError:
    print("outer Exception handled")
else:
    print("no Exceptions")