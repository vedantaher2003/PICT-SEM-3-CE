class stdrno:
    def __init__(self):
        self.n=0
        self.lst=[]

    def input(self):
        self.n=int(input("no of students"))
        self.lst=list(map(int,input("Enter roll numbers followed by spaces").split()))

    def lins(self,a):
        for i in range (self.n):
            if self.lst[i]==a:
                return i

    def sents(self,a):
        #b=self.lst[-1]
        self.lst.append(a)
        i=0
        while self.lst[i]!=a:
            i+=1
        #self.lst[-1]=b
        if i<=(self.n-1):
            print(a,"is present")
        else:
            print(a,"is abscent")

    def bins(self,a):
        b=sorted(self.lst)
        last=b[-1]
        first=b[0]
        while last>=first:
            m=(last+first)/2
            if m<a:
                first=m+1
            elif m>a:
                last=m-1
            elif m==a:
                return m
            else:
                return -1

    def fibos(self,a):
        lst=sorted(self.lst)
        fib=[0,1]
        f0=0
        f1=1
        m=0
        for i in range(self.n):
            fm=f0+f1
            f0=f1
            f1=fm
            fib.append(fm)
            if fib[i]>=self.n:
                m=i
                break
        offset=-1
        while fib[m-2]>0:
            i=min(offset+fib[m-2],self.n-1)
            if lst[i]>a:
                m=m-2
            elif lst[i]<a:
                m=m-1
                offset=i
            else:
                return i+1

l=stdrno()
l.input()
print("Select the method for finding the number.")
print("press 1-for linear method")
print("press 2-for sentinel method")
print("press 3-for binary method")
print("press 4-for fibonacci search method")
i="yes"
while i=="yes":
    a=int(input("select the number to find:"))
    n=int(input("select the method for finding the number:"))
    if n==1:
        i=l.lins(a)
        if i==None:
            print(a,"is abscent")
        else:
            print(a,"is present at position:",i+1)
    if n==2:
        print(l.sents(a))
    if n==3:
        b=l.bins(a)
        if b==-1:
            print(a,"is abscent")
        else:
            print(a,"is present")
    if n==4:
        f=l.fibos(a)
        if f!=None:
            print(a,"present at position:",f)
        else:
            print(a,"is abscent")

    i=input("Do you want to continue?(yes/no)")
print("Thank You!!")

