
# 位1的个数
class Solution:
    def hammingWeight(self, n: int) -> int:
        sum= 0
        while n!=0:
            n&=n-1
            sum+=1
        return sum

# 2的幂
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        return n&(n-1) == 0


# N皇后 II  位运算
class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        def dfs(row,col,pie,na):
            nonlocal count
            if row == n:
                count+=1
                return
            bits = ~(col | pie | na) & ((1 << n) - 1)
            while bits>0:
                pick = bits&-bits
                dfs(row + 1, col | pick, (pie | pick) << 1, (na | pick) >> 1)
                bits&=bits-1
        dfs(0,0,0,0)
        return count

# 翻转对
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(nums, left, right):
            if left >= right: return 0
            mid = (right + left) // 2
            count = merge_sort(nums, left, mid) + merge_sort(nums, mid + 1, right)
            cache = []
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if nums[i] > nums[j] * 2:
                    j += 1
                    count += (mid - i + 1)
                else:
                    i += 1
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if nums[i] < nums[j]:
                    cache.append(nums[i])
                    i += 1
                else:
                    cache.append(nums[j])
                    j += 1

            while i <= mid:
                cache.append(nums[i])
                i += 1
            while j <= right:
                cache.append(nums[j])
                j += 1

            nums[left:right + 1] = cache

            return count

        if len(nums) == 0: return 0
        return merge_sort(nums, 0, len(nums) - 1)