# selection_sort.py

# 首先在未排序序列中找到最小元素，存放到排序序列的起始位置。
# 然后，再从剩余未排序元素中继续寻找最小元素，然后放到已排序序列的末尾。
# 以此类推，直到所有元素均排序完毕。
def selection_sort(arr):
    length = len(arr)
    # 外层循环控制遍历的次数
    # 选择排序中i的值从[0~length-2]
    # -2 原因有以下两点：1.待排序数组索引的最大值为length-1。2.选择排序中如果length-1个元素已被排序，则整个序列有序
    for i in range(length - 1):
        # index用于保存未排序部分最小元素的索引
        index = i
        # 内层循环在每次遍历中将未排序部分最小的元素放至未排序部分首位
        # 选择排序中j的取值范围为[i+1~length-1]
        # i+1 由于内层循环开始时index=i，因此j最小取i+1
        # -1 length-1是待排序部分最后一个元素的索引
        for j in range(i + 1, length):
            # 遍历未排序部分，如果找到更小的元素就保存其索引
            if arr[j] < arr[index]:
                index = j
        # 将未排序部分最小的元素交换至未排序部分的首位
        arr[i], arr[index] = arr[index], arr[i]


if __name__ == '__main__':
    test = [8, 62, 82, 28, 70, 55, 60, 49, 66, 65]
    selection_sort(test)
    print(test)
