# bubble_sort.py

def bubble_sort(arr):
    length = len(arr)
    for i in range(length - 1, 0, -1):  # 遍历未排序部分数组
        exchange = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                exchange = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not exchange:
            break


if __name__ == '__main__':
    test = [2, 8, 2, 7, 1, 5, 6, 4, 7, 9]
    bubble_sort(test)
    print(test)
