# selection_sort.py

# 首先在未排序序列中找到最小元素，存放到排序序列的起始位置
# 然后，再从剩余未排序元素中继续寻找最小元素，然后放到已排序序列的末尾。
# 以此类推，直到所有元素均排序完毕。
def selection_sort(arr):
    length = len(arr)
    # 外层循环控制遍历的次数，i的值从0 ~ length-2，共遍历length-1次
    for i in range(length - 1):
        index = i   # 保存未排序部分最小元素的索引
        # 内层循环在每次遍历中将未排序部分最小的元素放至未排序部分首位
        # 由于内层循环开始时index=i，因此j取i+1 ~ length-1
        for j in range(i + 1, length):
            if arr[j] < arr[index]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]


if __name__ == '__main__':
    test = [8, 62, 82, 28, 70, 55, 60, 49, 66, 65]
    selection_sort(test)
    print(test)
