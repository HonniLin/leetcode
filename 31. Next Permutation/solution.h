#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int len = nums.size();
        int i = len-2, ii = len-1, j = len-1;
        while(i >= 0)
        {
            if(nums[i] >= nums[ii])
            {
                i--;
                ii--;
            }
            else
            {
                for(int j = len-1; j >= 0; --j)
                {
                    if(nums[i] < nums[j])
                    {
                        swap(nums[i], nums[j]);
                        for(int a = ii, b = len-1; a < b; a++, b--)
                        {
                            swap(nums[a], nums[b]);
                        }
                        break;
                    }
                }
                break;
            }
        }

        if(i < 0)
        {
            sort(nums.begin(), nums.end());
        }
    }
};
