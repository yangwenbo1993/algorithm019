学习笔记

```
位运算
左移、右移
按位或｜， 按位与&， 按位取反～， 按位异或^
异或：相同为0，不同为1
x^0=x, x^1s=~x(1s=~0), x^~x=1s, x^x=0
不利用额外变量交换两个整数：c = a^b, a = a^c, b = b^c (c可以表明a和b各个位之间的关系)
指定位置的位运算
将x右边的n位清零： x & (~0<<n)
获取x的第n位值：(x >>n) & 1
获取x的第n位的幂值：x & (1<<n)
将第n位设置为1: x | (1<<n)
将第n位设置为0: x & ~(1<<n)
将x最高位至第n位清零： x & ((1<<n)-1)
位运算实战要点：
判断奇偶：x & 1 == 1(奇数)， x & 1 == 0(偶数)
x>>1 -> x/2
清零最低位的1: x = x & (x-1)
得到最低位的1: x & -x
##8.2 布隆过滤器 一个很长的二进制向量和一系列随机映射函数，可以用于检验一个元素是否在一个集合中
优点：空间效率和查询时间都远远超过一般的算法 缺点：有一定的误识别率和删除困难
```

```
LRU cache（least recently used）
两个要素：大小、替换策略；
替换算法有点类似于推荐算法    
利用双向链表进行实现，锻炼双向链表的写法
```

```
快速排序
def quick_sort(begin, end, nums):
    if begin >= end:
        return
    pivot_index = partition(begin, end, nums)
    quick_sort(begin, pivot_index-1, nums)
    quick_sort(pivot_index+1, end, nums)
    
def partition(begin, end, nums):
    pivot = nums[begin]
    mark = begin
    for i in range(begin+1, end+1):
        if nums[i] < pivot:
            mark +=1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[begin], nums[mark] = nums[mark], nums[begin]
    return mark
```

```
归并排序

def mergesort(nums, left, right):
    if right <= left:
        return
    mid = (left+right) >> 1
    mergesort(nums, left, mid)
    mergesort(nums, mid+1, right)
    merge(nums, left, mid, right)

def merge(nums, left, mid, right):
    temp = []
    i = left
    j = mid+1
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i +=1
        else:
            temp.append(nums[j])
            j +=1
    while i<=mid:
        temp.append(nums[i])
        i +=1
    while j<=right:
        temp.append(nums[j])
        j +=1
    nums[left:right+1] = temp
```

