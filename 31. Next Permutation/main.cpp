#include <iostream>
#include "main.h"

using namespace std;

int main()
{
    cout << "Hello world!" << endl;
    Solution sol;
    vector<int> vec{1,2,4,5,3};
    sol.nextPermutation(vec);
    for(int i = 0; i < vec.size(); ++i)
    {
        cout << vec[i] << "";
    }
    cout << endl;
    return 0;
}
