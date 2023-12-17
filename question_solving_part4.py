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
    

