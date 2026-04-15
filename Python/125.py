def find_duplicate(arr):
    # 双重循环查找重复元素，时间复杂度 O(n²)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

# 测试数据
numbers = [1, 2, 3, 4, 5, 2]
print(find_duplicate(numbers))