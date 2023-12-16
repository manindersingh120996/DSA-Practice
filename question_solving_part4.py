def swap_alternate_elements(arr):
    n = len(arr)
    pos = 1
    while pos < n:
        temp1 =  arr[pos-1]
        temp2 = arr[pos]
        arr[pos] = temp1
        arr[pos-1] = temp2
        
        pos+=2
    print(arr)

swap_alternate_elements([1,2,3,4,5,6,7])

