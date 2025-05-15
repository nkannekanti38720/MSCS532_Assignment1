def insertion_sort_desc(arr):
    # Traverse through 1 to len(arr) - 1
    for i in range(1, len(arr)):
        key = arr[i]  # Element to be inserted in the sorted portion
        j = i
        
        # Move elements of arr[0..i-1], that are less than key,
        # to one position ahead to make space for key
        while j > 0 and arr[j - 1] < key:
            arr[j] = arr[j - 1]  # Shift element rightwards
            j -= 1  # Move to previous element
        
        # Insert the key at its correct position
        arr[j] = key

if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6]
    insertion_sort_desc(arr)  # Sort the array in decreasing order
    print("Sorted array (decreasing):", arr)  # Output the sorted array
