def find_duplicate(arr):
    # 层级1：外层循环
    for i in range(len(arr)):
        # 层级2：内层循环（比外层多4个空格）
        for j in range(i + 1, len(arr)):
            # 层级3：if判断（比内层多4个空格）
            if arr[i] == arr[j]:
                # 层级4：if成立时返回True（比if多4个空格）
                return True
    # 层级1：所有循环结束后，无重复则返回False（和外层for同级）
    return False

# 函数外部：测试代码
arr = [1, 2, 3, 4, 5]
print(find_duplicate(arr))  # 输出：False
arr2 = [1, 2, 3, 2, 5]
print(find_duplicate(arr2)) # 输出：True