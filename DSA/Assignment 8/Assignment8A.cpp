#include<iostream>
using namespace std;
class SLL_Node
{
	public:
    int start;
    int end;
    int min;
    int max;
    int flag;
    SLL_Node *next;
   public:
   SLL_Node(){
    next=NULL;
   };
   friend class SLL;
};

class SLL
{
	SLL_Node *head,*last;
    public:
    SLL(){
    	head=NULL, last=NULL;
    }
    void create_Shedule();
    void display_Shedule();
    void book_App() ;
    void cancel_App() ;
    void sort_App();
};

int main(){
	int ch;
    char ans;
    SLL S;
    do{
        cout<<"\n\n *** Menu ***";
        cout<<"\n 1. Create Appointment Schedule";
        cout<<"\n 2. Display Free Slots";
        cout<<"\n 3. Book an Appointment";
        cout<<"\n 4. Cancel an Appointment";
        cout<<"\n 5. Sort slots based on Time";

        cout<<"\n\n Enter your choice: ";
        cin>>ch;

        switch(ch){
            case 1: S.create_Shedule();
                    break;
            case 2: S.display_Shedule();
                    break;
            case 3: S.book_App();
                    break;
            case 4: S.cancel_App();
                    break;
            case 5: S.sort_App();
                    break;
            default: cout<<"\n\t Wrong choice!!!";
        }
        cout<<"\n\n\tDo you want to continue? (y/n) : ";
        cin>>ans;
    }while(ans=='y');
}

void SLL :: create_Shedule(){
    SLL_Node *temp; 
    int size;
    cout<<"\n\n\tEnter appointments slots: ";
    cin>>size;
    for(int i=0;i<=(size-1);i++){
        temp=new SLL_Node();
        cout<<"\n\n\tEnter start time: ";
        cin>>temp->start;
        cout<<"\n\tEnter end time: ";
        cin>>temp->end;
        cout<<"\n\n\tEnter minimum duration: ";
        cin>>temp->min;
        cout<<"\n\tEnter maximum duration: ";
        cin>>temp->max;
        temp->flag=0;
        temp->next=NULL;
        if(head==NULL){
            head=temp;
            last=head;
        }
        else{
            last->next=temp;
            last=last->next;
        }
    }
}

void SLL :: display_Shedule(){
	SLL_Node *temp;
    int cnt=0;
    cout<<"\n\n\tAppointment Schedule";
    cout<<"\n\n\t Sr.no.\tStart\tEnd\tMin_Dur\tMax_Dur\tStatus";
    temp=head;
    while(temp!=NULL){
        cout<<"\n\n\t "<<cnt;
        cout<<"\t "<<temp->start;
        cout<<"\t "<<temp->end;
        cout<<"\t "<<temp->min;
        cout<<"\t "<<temp->max;
        if(temp->flag){
            cout<<"\tBooked";
        }
        else{
            cout<<"\tFree";
        }
        temp=temp->next;
        cnt++;
    }
}

void SLL :: book_App(){
	SLL_Node *temp;
    int start;
    cout<<"\n\n\tPlease enter appointment time: ";
    cin>>start;
    temp=head;
    while(temp!=NULL){
        if(start==temp->start){
            if(temp->flag==0){
                cout<<"\n\n\tAppointment Slot is Booked";
                temp->flag=1;
            }
            else{
                cout<<"\n\n\tAppointment Slot is not Available!!!";
            }
        }
        temp=temp->next;
    }
}

void SLL :: cancel_App(){
	SLL_Node *temp;
    cout<<"\n\n\tPlease enter Appointment time to Cancel:";
    int start;
    cin>>start;
    temp=head;
    while(temp!=NULL){
        if(start==temp->start){
            if(temp->flag==1){
                cout<<"\n\n\tYour Appointment Slot is Canceled!!!";
                temp->flag=1;
            }
            else
            cout<<"\n\n\tYour Appointment was not Booked!!!";
        }
        temp=temp->next;
    }
}

void SLL :: sort_App(){
    int size;
	SLL_Node *temp;
    for(int i=0;i<(size-1);i++){
        temp=head;
        while(temp->next!=NULL){
            if(temp->start > temp->next->start){
                int val=temp->start;
                temp->start=temp->next->start;
                temp->next->start=val;

                val=temp->end;
                temp->end=temp->next->end;
                temp->next->end=val;

                val=temp->min;
                temp->min=temp->next->min;
                temp->next->min=val;

                val=temp->max;
                temp->max=temp->next->max;
                temp->next->max=val;
            }
            temp=temp->next;
        }
    }
    cout<<"\n\n\t The Appointments got Sorted!!!";
}

