#排序算法比较
a = [45,78,12,3,6,78,415,1,5,7]

# def countingSort(nums):  #计数排序
#     bucket = [0] * (max(nums) + 1) # 桶的个数
#     for num in nums:  # 将元素值作为键值存储在桶中，记录其出现的次数
#         bucket[num] += 1
#     i = 0  # nums 的索引
#     for j in range(len(bucket)):
#         while bucket[j] > 0:
#             nums[i] = j
#             bucket[j] -= 1
#             i += 1
#     return nums
# print(countingSort(a))

def selectionSort(nums):  #插入排序
    for i in range(len(nums) - 1):  # 遍历 len(nums)-1 次
        minIndex = i
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[minIndex]:  # 更新最小值索引
                minIndex = j  
        nums[i], nums[minIndex] = nums[minIndex], nums[i] # 把最小数交换到前面
    return nums