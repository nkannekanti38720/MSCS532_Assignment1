def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        while j > 0 and arr[j-1] < key:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = key

if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6]
    insertion_sort_desc(arr)
    print("Sorted array (decreasing):", arr)
