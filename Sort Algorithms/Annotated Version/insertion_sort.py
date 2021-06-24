# insertion_sort.py

# 对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

# def insertion_sort(arr):
#     length = len(arr)
#     for i in range(1, length):
#         for j in range(i, 0, -1):
#             if arr[j - 1] > arr[j]:
#                 arr[j - 1], arr[j] = arr[j], arr[j - 1]

def insertion_sort(arr):
    length = len(arr)
    # 外层循环控制遍历的次数，也是该次遍历进行插入的元素的索引
    # 插入排序中i的取值范围为[1,length-1]
    # 1 第一个元素可认为已排序，从第二个元素开始插入
    for i in range(1, length):
        # key保存当前插入元素的值
        key = arr[i]
        # 内层循环将该次遍历要插入的元素arr[i]插入到指定位置
        # 由于比较时是arr[j]与arr[j+1]比较，因此j的取值范围为[0,i-1]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        # 找到适合插入的位置，进行插入
        arr[j + 1] = key


if __name__ == '__main__':
    test = [8, 62, 82, 28, 70, 55, 60, 49, 66, 65]
    insertion_sort(test)
    print(test)
