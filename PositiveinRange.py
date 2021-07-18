n=int(input("Please Enter the number of elements: "))
l1=[]
for i in range(0,n):
    a=int(input())
    l1.append(a)
print("The original list is:",end=" ")
print(l1)
l2=[]
for i in l1:
    if i>0:
        l2.append(i)
print("The list of positive numbers is:",end=" ")
print(l2)