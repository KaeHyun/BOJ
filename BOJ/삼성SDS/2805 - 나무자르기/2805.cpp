//2805번 -- 나무 자르기
#include <iostream>
#include <vector>
using namespace std;
long long treeNum, want, sum;
vector<int> trees;

int maxVal = 0;
int ans;

int main() 
{
  cin >> treeNum >> want;
  for(int i=0; i<treeNum; i++)
    {
      int temp;
      cin >> temp;
      trees.push_back(temp);//벡터에 tree 모두 추가 
      if(temp >= maxVal)
      {
        maxVal = temp;
      }
    }
  //printf("maxVal: %d", maxVal);
  //이분탐색 이용
  int left = 0;
  int right = maxVal;

  while(left <= right)
    {
      int mid = (left+right)/2;
      sum = 0;
      for(int i =0; i < treeNum; i++)
        {
          if( mid < trees[i])
            sum += trees[i]-mid;
        }
      if(sum >= want)
      {
        if(ans<mid)
        {
          ans = mid;
          }
        left = mid + 1;
      }
      else
      {
        right = mid -1;
      }
    }
  
  cout << ans;
}