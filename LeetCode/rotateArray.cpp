#include <iostream>

using namespace std;

class Solution {
public:
    void rotate(int nums[], int n, int k) {
        int solution[n];
        for(int i = 0; i < n; i++){
            if(i < k){
                solution[i] = nums[i + (n - k)];
            } else {
                solution[i] = nums[i - k];
            }
        }
    }
};

int main(int argc, char** argv){
    Solution sol;
    int nums[] = {1, 2};
    sol.rotate(nums, 2, 1);
    cout << "[";
    for(int num : nums){
        cout << num << ",";
    }
    cout << "]" << endl;
    return 0;    
}