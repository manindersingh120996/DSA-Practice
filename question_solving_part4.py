def swap_alternate_elements(arr):
    """
    input = [1,2,3,4,5,6,7]
    output =  [2, 1, 4, 3, 6, 5, 7]
    """
    n = len(arr)
    pos = 1
    while pos < n:
        temp1 =  arr[pos-1]
        temp2 = arr[pos]
        arr[pos] = temp1
        arr[pos-1] = temp2
        
        pos+=2
    print(arr)

# swap_alternate_elements([1,2,3,4,5,6,7])
    
def unique_element(arr):
    """
    input = array of size 2m + 1
    output = 1 unique element
    example: input = [11,15,22,15,22,11,3]
    output = 3
    """
    ans = 0
    for element in arr:
        ans = ans^element
    print("Unique element in array is : ",ans)
unique_element([11,15,22,15,22,11,3])

