# Count the number inversions from the list of numbers in the given input file
  
# Helper Function for Inversion Count
def mergeSort(arr, n):

    # To store sorted array in merge function
    temp_arr = [0]*n
    return _mergeSort(arr, temp_arr, 0, n - 1)
  
# Function using MergeSort to count inversions
def _mergeSort(arr, temp_arr, left, right):
  
    # Store inversion counts in each recursive call
    inv_count = 0
  
    # Recursive call if and only if we have more than one elements
    if left < right:
  
        # Divide the array into two subarrays
        mid = (left + right) // 2
  
        # Calculate inversion counts in the left subarray
        inv_count += _mergeSort(arr, temp_arr, left, mid)
  
        # Calculate inversion counts in right subarray
        inv_count += _mergeSort(arr, temp_arr, mid + 1, right)
  
        # Merge two subarrays in a sorted subarray
        inv_count += merge(arr, temp_arr, left, mid, right)

    return inv_count
  
# Merge two subarrays in a single sorted subarray
def merge(arr, temp_arr, left, mid, right):
  
    # Starting index of left subarray
    i = left     
  
    # Starting index of right subarray
    j = mid + 1 
  
    # Starting index of to be sorted subarray
    k = left     
    inv_count = 0
  
    # Check subarray limits
    while i <= mid and j <= right:
  
        # No inversions if arr[i] <= arr[j]
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:

            # Handle Inversions
            temp_arr[k] = arr[j]
            inv_count += (mid-i + 1)
            k += 1
            j += 1
  
    # Copy the remaining elements of left subarray into temporary array
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1
  
    # Copy the remaining elements of right subarray into temporary array
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1
  
    # Copy the sorted subarray into Original array
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]
          
    return inv_count
  

# Read the numbers from input.txt
arr = []

f = open('input.txt')

for line in f.readlines():
    arr.append(float(line))

f.close()

n = len(arr)

# Call the function mergeSort to find the number of inversions
result = mergeSort(arr, n)
print("Number of inversions are", result)