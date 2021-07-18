def most_frequent(li):
    l1=sorted(li)
    s1=set(l1)
    a=len(s1)
    f={}
    for i in l1:
        if i in f:
            f[i]=f[i]+1
        else:
            f[i]=1
    f1=sorted(f.keys(),reverse=False)
    f2=sorted(f.values(),reverse=False)
    for i in range (0,a):
        print(f1[i],"=",f2[i])
print("Enter the String:",end=" ")
a=input()
most_frequent(a)