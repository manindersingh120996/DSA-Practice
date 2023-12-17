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
# unique_element([11,15,22,15,22,11,3])

def uniqueOccurance(arr):
    """
    Input: arr = [1,2,2,1,1,3]
    Output: true
    Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
    """
    count = {}
    for num in arr:
        if num not in count.keys():
            count[num] = 1
        elif num in count.keys():
            count[num] += 1
    if len(set(count.values())) == len(count):
        print(True)
    else:
        print(False)

uniqueOccurance([1,2,1])
