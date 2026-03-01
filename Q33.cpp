class Solution {
public:
    int search(vector<int>& nums, int target) {
        int v_size = nums.size();
        cout<<v_size;
        for(int i =0;i<v_size;i++){
            if(nums[i]==target){
                return i;
            }
        }
        return -1;

    }
};
