# bubble_sort.py

def bubble_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        swapped = False
        for j in range(0, length - 1 - i):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            break


if __name__ == '__main__':
    test = [8, 62, 82, 28, 70, 55, 60, 49, 66, 65]
    bubble_sort(test)
    print(test)
