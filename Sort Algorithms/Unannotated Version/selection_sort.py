# selection_sort.py


def selection_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        index = i
        for j in range(i + 1, length):
            if arr[j] < arr[index]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]


if __name__ == '__main__':
    test = [8, 62, 82, 28, 70, 55, 60, 49, 66, 65]
    selection_sort(test)
    print(test)
