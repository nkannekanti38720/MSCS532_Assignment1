def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6]
    insertion_sort_desc(arr)
    print("Sorted array (decreasing):", arr)
