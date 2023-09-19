#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    void rotate(vector <int>& nums, int k) {
        int length = nums.size();
        int temp1;
        for(int i = 0; i < k; i++)
        {
            temp1 = nums[length];
            for(int j = length; j > 0; j++)
            {
                nums[j] = nums[j-1];
            }

            nums[0] = temp1;
        }
    }
};


int main(){
	vector<int> vec;  
	for(int i=0; i<10;i++)
	{
		vec.push_back(i);
	  }    	
  	Solution test;
  	test.rotate(vec,5);
  	for (int i = 0; i < vec.size(); i++)  
  	{  
    	cout << vec[i] << " ";   
  	}  

}