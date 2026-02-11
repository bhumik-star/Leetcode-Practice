#include<iostream>
#include<vector>
using namespace std;

int maxArea(vector<int>& height) {
    int left = 0;
    int right = height.size() -1;
    int max_area = 0;
    while(left<right){
    int distance = right - left;
    int min_height = min(height[left],height[right]);
    int area = distance * min_height;
    if(area>max_area){
        max_area = area;
    }
    if(height[left]<height[right]){
        left++;
    }
    else{
        right--;
    }
    }
    return max_area;
}

int main(){
    vector<int> height= {1,5,4,3,5,7,2,3,5,2};//Change height vector all you want
    cout<<maxArea(height);
}