//22. Generate Parentheses
//2017.8.22
//µ›πÈ µœ÷

class Solution {
public:
    void work(vector<string> &vec, string src, int n, int lcnt, int rcnt)
    {
        if(lcnt == n && rcnt == n)
        {
            vec.push_back(src);
        }
        else
        {
            if(lcnt < n)
            {
                work(vec, src + '(', n, lcnt+1, rcnt);
            }
            if(lcnt > rcnt)
            {
                work(vec, src + ')', n, lcnt, rcnt+1);
            }
        }
    }
    vector<string> generateParenthesis(int n) {
        vector<string> vec;
        work(vec, "(", n, 1, 0);
        return vec;
    }
};
