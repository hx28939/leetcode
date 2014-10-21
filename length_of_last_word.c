//
//  huanwei.c
//  
//
//  Created by Hao Xin on 14-3-22.
//
//

#include <stdio.h>
#include<iostream>
using namespace std;

class Solution {
public:
    int lengthOfLastWord(const char *s) {
        
        int l=0;
        int j=0;
        int num_space = 0;
        while (s[j]!='\0')
        {
            
            if (s[j]==' ')
            {
                num_space++;
            }
            l++;
            j++;
            
        }
        
        int p[num_space+2];
        int p_s=1;
        p[0]=-1;
        p[num_space+1]=l;
        
        for (int i=0;i<l;i++)
        {
            if (s[i]==' ')
            {
                p[p_s]=i;
                p_s++;
            }
        }
        int n=0;
        for (int i=0;i<num_space+1;i++)
        {
            if (p[i]!=p[i+1]-1)
            n=p[i+1]-p[i]-1;
        }

        
        cout<<"after:"<<endl<<l<<endl<<p<<endl<<n<<endl<<"aa";
        
        return n;
        
    }
};

int main(){
    char *given="a ";
    Solution* solver=new Solution;
    solver->lengthOfLastWord(given);
    
    
}