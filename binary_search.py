def binary_search(arr,element):
    arr_len = len(arr)
    first_index = 0
    last_index = int(arr_len)
    found = 0
    mid_element_index = int((first_index + last_index) / 2)
    # print(arr[mid_element_index],'_-______')
    while(first_index!=last_index):
        if arr[mid_element_index] == int(element):
            found = 1
            print(f"Element found at {mid_element_index} index position")
            break
        if element > arr[mid_element_index]:
            first_index = mid_element_index+1
            mid_element_index = int((first_index + last_index) / 2)
        else:
            last_index = mid_element_index
            mid_element_index = int((first_index + last_index) / 2)
        
    if found == 0:
        print("element not found")

# binary_search([11,13,45,55,78,112],45)

def first_occurance(arr,element):
    start_index = 0
    last_index = len(arr)
    arr_len = len(arr)
    ans = -1
    while(start_index < last_index):
        mid_index = int((start_index+last_index)/2)
        if arr[mid_index] == element:
            ans = mid_index
            last_index = mid_index
        if arr[mid_index] < element:
            start_index = mid_index + 1
        elif arr[mid_index] > element:
            last_index = mid_index
    
    if ans == -1:
        print(f"Element {element} is not found in the given list.")
    else:
        print(f"Element {element} occurs at index position of {ans}")

first_occurance([1,2,3,4,4,4,5,6,6,6,6,7],4)

def last_occurance(arr,element):
    first_index = 0
    last_index = len(arr)
    arr_len = len(arr)
    ans = -1
    while last_index > first_index:
        mid_index = int((first_index+last_index)/2)
        if arr[mid_index] == element:
            ans = mid_index
            first_index = mid_index + 1
        if arr[mid_index] < element:
            first_index = mid_index + 1
        elif arr[mid_index] > element:
            last_index = mid_index
    
    if ans == -1:
        print(f"Element {element} does not exists in the list")
    else:
        print(f"Element {element} exists at index position of {ans}")

last_occurance([1,2,3,4,4,4,5,6,6,6,6,7],4)
