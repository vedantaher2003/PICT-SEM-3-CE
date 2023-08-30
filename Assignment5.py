
class Sort:
    def __init__(self):
        self.students=[]
        
    def getpercentage(self,t):
        for i in range(t):
            percentage=int(input("Enter percentage of student: "))
            self.students.append(percentage)
        
    def insertion(self,t):
        for i in range(0,t):
            for j in range(i,0,-1):
                if(self.students[j]<self.students[j-1]):
                    temp=self.students[j]
                    self.students[j]=self.students[j-1]
                    self.students[j-1]=temp
        print("The top five scores are: ")
        for i in range(t-1,t-6,-1):
            print(self.students[i])
            
    def shell(self,t):
        interval=t//2
        while interval>0:
            for i in range(interval,t):
                temp=self.students[i]
                j=i
                while j>=interval and self.students[j-interval]>temp:
                    self.students[j]=self.students[j-interval]
                    j-=interval
                    
                self.students[j]=temp
            interval//=2
        print("The top five scores are: ")
        for i in range(t-1,t-6,-1):
            print(self.students[i])
                
        
        
def menu():
    print("*******MENU*******")
    print("1)Insertion Sort")
    print("2)Shell Sort")
    print("3)To exit the program")
    
s=Sort()
total=int(input("Enter total number of students: "))
s.getpercentage(total)
menu()

while True:
    choice=int(input("Enter your choice:"))
    if choice==1:
        s.insertion(total)
        menu()
       
        
    elif choice==2:
        s.shell(total)
        menu()
       
        
    elif choice==3:
        break
    
    else:
        print("Enter a valid choice")
        menu()
        
        