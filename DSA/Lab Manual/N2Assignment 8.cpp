#include<iostream>
using namespace std;

class node{
	public:
	int data;
	node*next;

	node(int d){
		data=d;
		next=NULL;
	}
};

void insert(node*&head,int d){
    if(head==NULL){
    node*temp=new node(d);
        head=temp;
    }
    else{

node*app=new node(d);
app->next=head;
head=app;
    }
}


void print(node*head){
node*temp=head;
while(temp!=NULL){
cout<<temp->data<<" ";
temp=temp->next;
}
cout<<endl;
}

void intersection(node*&head1,node*&head2){
	node*temp1=head1;
	node*temp2=head2;
    node*head3=NULL;

	while(temp1!=NULL){
		while(temp2!=NULL){
			if(temp1->data==temp2->data){
				insert(head3,temp1->data);
			
			}
			temp2=temp2->next;
		}
		temp2=head2;
		temp1=temp1->next;
	}

    cout<<"student like both "<<endl;
    print(head3);
}
bool ispresent(node*&head,int data){
    node*temp=head;

    while(temp!=NULL){
        if(temp->data==data){
            return 1;
        }
        temp=temp->next;
    }
    return 0;
}
node* union_(node*&head1,node*&head2){

	node*temp1=head1;
	node*temp2=head2;
    node*head3=NULL;
    
    while(temp1!=NULL){
       insert(head3,temp1->data);
        temp1=temp1->next;
    }
    while(temp2!=NULL){

        if(!ispresent(head3,temp2->data)){
            insert(head3,temp2->data);
        }
        temp2=temp2->next;
    }
    return head3;
    
}

node* diff(node*&head1,node*&head2){
    node*temp1=head1;
    node*temp2=head2;
    node*head3=NULL;
    while(temp1!=NULL){
        if(!ispresent(head2,temp1->data)){
            insert(head3,temp1->data);
        }
        temp1=temp1->next;
    }
    return head3;
    }

int main(){

node*head0=NULL;
node*head1=NULL;
node*head2=NULL;
// node*head3=NULL;
// node*head4=NULL;
// node*head5=NULL;


int n,v,b;

cout<<"no. of student in se4"<<endl;
cin>>n;

cout<<"no. of student like vanilla"<<endl;
cin>>v;

cout<<"no of student like butterscotch"<<endl;
cin>>b;


cout<<"enter no. of student in se4"<<endl;

for(int i=0;i<n;i++){
     int x;
    cin>>x;
    insert(head0,x);
}

cout<<"enter no. of student like vanilla"<<endl;
for(int i=0;i<v;i++){
    int x;
    cin>>x;
    insert(head1,x);
}
cout<<"enter no of student like butterscpotoh"<<endl;
for(int i=0;i<b;i++){
    int x;
    cin>>x;
    insert(head2,x);
}

// insert(head1,2);
// insert(head1,3);
// insert(head1,5);
// insert(head1,1);
// insert(head2,2);
// insert(head2,10);
// insert(head2,5);
// insert(head2,9);
cout<<"student like vanilla"<<endl;
 print(head1);
 cout<<"student like butterscotoh"<<endl;
print(head2);


intersection(head1,head2);



//cout<<"union of two ll"<<endl;
//node*head3=union_(head1,head2);


cout<<" student like vanilla or butterscotoh or not both"<<endl;
node*head3=diff(head1,head2);
node*head4=diff(head2,head1);
node*head5=union_(head3,head4);
print(head5);


cout<<"number of student who like nither vanilla nor butterscotoh"<<endl;
node*head7=union_(head1,head2);
node*head6=diff(head0,head7);
print(head6);

}