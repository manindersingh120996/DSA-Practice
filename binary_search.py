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

binary_search([11,13,45,55,78,112],45)
