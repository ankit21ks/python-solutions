from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
            length = len(nums)
            
            nums[:] = [x for x in nums if x!= 0]
            
            diff = length - len(nums)
            
            for i in range(0,diff):
                nums.append(0)
            nums[:] = nums   
            return nums

if __name__ == "__main__":
    s = Solution()
    print(s.moveZeroes([1,0,2,3]))
