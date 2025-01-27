x=input("Enter a number:")
l=len(x)
n=False
if x[-1]== x[0]:
    if len(x)%2==1:
               y=0
               while len(x)/2>y:
                   if x[y]==x[l-1]:
                       n=True
                   else:
                       n=False
                       break
                   y+=1
                   l-=1
else:
    print("The ", x, " is not Palindrome")
if n==1:
    print("The ",x," is Palindrome")
else:
    print("The ",x," is not Palindrome")



