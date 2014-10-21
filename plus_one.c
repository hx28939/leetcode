class Solution {
public:
    vector<int> plusOne(vector<int> &digits) {
        int w = digits.size()-1;
        int ss=0;
        while (ss==0)
        {
            if (digits[w]==9)
            {
                digits[w] = 0;
                w--;
                
            }
            else
            {
                ss=1;
            }
            
        }
        
        if (w==-1)
        {
            vector<int>newb(digits.size()+1);
            newb[0] = 1;
            return newb;
            
        }
        else
        {
            digits[w]++;
            return digits;
            
        }
        
    }
};

