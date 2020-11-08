#接雨水
class Solution():
    def trap(self, height: list) -> 'int':
        length = len(height)
        if length < 3: return 0
        result, stack = 0, []
        for index in range(length):
            while len(stack) > 0 and height[index] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0:
                    break
                left = stack[-1]
                h = min(height[left], height[index]) - height[top]
                dist = index - left - 1
                result += (dist * h)
            stack.append(index)
            index += 1
        return result




#合并两个有序数组
class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = len(nums1) - 1;
        m-=1
        n-=1
        while n >= 0:
            while m >= 0 and nums1[m] > nums2[n]:
               nums1[i],nums1[m] = nums1[m],nums1[i]
               m-=1
               i-=1
            nums1[i],nums2[n] = nums2[n],nums2[n]
            n-=1
            i-=1



#移动零
class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        o,length = 0,len(nums)
        for i in range(length):
            if nums[o] == 0:
                nums.pop(o)
                nums.append(0)
            else:
                o+=1
