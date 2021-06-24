# bubble_sort.py

# 比较相邻的元素。如果前面的比后面的大，就交换它们，然后比较下一对元素。
# 从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
# 针对所有未排序部分的元素重复以上的步骤。
# 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

def bubble_sort(arr):
    length = len(arr)
    # 外层循环控制遍历的次数
    # 冒泡排序中i的取值为[0~length-2]
    # -2 原因有以下两点：1.待排序数组索引的最大值为length-1。2.冒泡排序中如果length-1个元素已被排序，则整个序列有序
    for i in range(length - 1):
        # 如果某次遍历没有发生元素交换，那么序列有序
        # swapped 用于标识在某次遍历中是否发生了相邻元素的交换
        swapped = False
        # 内层循环在某次遍历中将最大的元素交换至未排序部分末尾
        # 冒泡排序中j的取值范围为[0~length-2-i]
        # i  表示当前已排序部分元素的个数
        # -2 原因有以下两点：1.待排序数组索引的最大值为length-1。2.在进行相邻两元素的比较时是arr[j]与arr[j+1]进行比较，j+1不能越界。
        for j in range(0, length - 1 - i):
            if arr[j] > arr[j + 1]:
                # 如果发生交换，那么设置swapped标识为True
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        # 如果某次遍历没有发生相邻元素的交换，那么序列有序
        if not swapped:
            break


if __name__ == '__main__':
    test = [8, 62, 82, 28, 70, 55, 60, 49, 66, 65]
    bubble_sort(test)
    print(test)
