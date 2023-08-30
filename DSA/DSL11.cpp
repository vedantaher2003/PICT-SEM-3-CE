#include <bits/stdc++.h>
using namespace std;

class que
{
private:
    int size;
    int *job;
    int rear, front;

public:
    que(int s)
    {
        size = s;
        job = new int[s];
        front = -1; rear = -1;
    }

    bool ismt()
    {
        if(front == -1 && rear == -1)
            return true;
        else
            return false;
    }

    bool isful()
    {
        if(rear == size - 1)
            return true;
        else
            return false;
    }

    void enq(int j)
    {
        if(ismt())
        {
            front++;
            rear++;
            job[rear] = j;
        }
        else if(isful())
        {
            cout<<"List is Full..."<<endl;
        }
        else
        {
            rear++;
            job[rear] = j;
        }
    }

    void delq()
    {
        if(ismt())
        {
            cout<<"Empty..\n";
        }
        else if(front == rear)
        {
            cout<<"Deleting the only remaining element.."<<endl;
            job[front] = 0;
            front = -1;
            rear = -1;
        }
        else if(ismt())
            cout<<"Queue Aready empty.."<<endl;
        else
            front++;
    }

    void display()
    {
        if(ismt())
            cout<<"Queue Empty."<<endl;
        else
        {
            cout<<"Queue: ";
            int i = front;
            while(i-1 != rear)
            {
                cout<<job[i]<<" ";
                i++;
            }
            cout<<endl;
        }
    }

};


int main()
{
    int si;
    cout<<"Size of Queue: ";
    cin>>si;
    que joe(si);
    while(true)
    {
        int cho;
        cout<<"Queue Operations:\n1: EnQueue\n2: Delete element from Queue\n3: Display\nr: Exitt\n";
        cin>>cho;
        if(cho == 1)
        {
            if(joe.isful())
                cout<<"Queue Full.."<<endl;
            else
            {
                int in;
                cout<<"Input element: ";
                cin>>in;
                joe.enq(in);
            }
        }
        else if(cho == 2)
            joe.delq();
        else if(cho == 3)
            joe.display();
        else
        {
            cout<<"\nBEe BEe\n";
            break;
        }
    }
    return 0;
}