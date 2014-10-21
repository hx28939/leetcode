//
//  reorder_list.c
//  
//
//  Created by Hao Xin on 14-4-11.
//
//

#include <stdio.h>
#include <iostream>
using namespace std;

struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
  };

class Solution {
public:
    void reorderList(ListNode *head) {
        if (!head){return;}
        if (head->next==NULL){return;}
        ListNode *nn=head->next;
        ListNode *rr=head;
        int a[100];
        int count=0;
        while (rr->next!=NULL)
        {
            a[count]=rr->val;
            rr=rr->next;
            count++;
        }
        cout<<"aa is :"<<endl<<a[0]<<endl<<"count is :"<<endl<<count<<endl;

        head->next=nn;
        for (int i=0;i<count/2;i++)
        {
            rr=nn->next;
            nn->val=a[count-i];
            nn->next=rr;
            nn=rr;
        }
        cout<<"head next is :"<<endl<<head->next->val<<endl<<"count is :"<<endl<<count<<endl;

        
    }
};

int main(){
    ListNode *a1=new ListNode(1);
    ListNode *b=new ListNode(2);
    ListNode *c=new ListNode(3);
    ListNode *d=new ListNode(4);
    ListNode *e=new ListNode(5);
    a1->val=11;
    a1->next=b;
    b->next=c;
    c->next=d;
    d->next=e;
    cout<<"hhh"<<endl<<a1->val<<endl;
    Solution* solver=new Solution;
    solver->reorderList(a1);
    
}