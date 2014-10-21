#include <stdio.h>
#include<iostream>
#include <vector>

using namespace std;


class Solution {
public:
    int longestConsecutive(vector<int> &num) {
        int length=1;
        vector<int>::iterator next;
        
        for (vector<int>::iterator iter=num.begin();iter!=num.end();iter++)
        {
            for (vector<int>::iterator j=iter;j!=num.end();j++)
            {
                if((*j-*iter)==1)
                {
                    length++;
                    next=
                }
            }
        }
        
    }
};

int main(){
    
    vector<int> *p = new vector<int>();
    int a=5,b=7;
    p->push_back(a);
    p->push_back(b);
    vector<int>::iterator iter=p->begin();
    while(iter!=p->end())
        cout<<*iter++<<endl;
    
    system("pause");
    return 0;
    
    /*
    vector <int> *rray;
    rray->at(0)=1;
   // rray[1]=22;
    //rray[2]=12;
    Solution* solver=new Solution;
    //solver->reverseWords(given,l);
    cout<<"after:"<<endl<<rray->at(0)<<""<<endl;
     */
    
}