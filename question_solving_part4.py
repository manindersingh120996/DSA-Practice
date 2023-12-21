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


def findDuplicate(arr):
    """
    Sample Input 1:
                    
                    5
                    4 2 1 3 1

                    7
                    6 3 1 5 4 3 2
Sample Output 1:
                1
                3
"""
    n = len(arr)
    sum = ((n-1)*n)/2
    sum_arr = 0
    for ele in arr:
        sum_arr += ele
    return int(sum_arr-sum)

# findDuplicate([1,2,4,6,2,3,5])

def findDuplicates(self, nums):
    """
    LeetCode question 442
    Example 1:

    Input: nums = [4,3,2,7,8,2,3,1]
    Output: [2,3]
    Example 2:

    Input: nums = [1,1,2]
    Output: [1]
    Example 3:

    Input: nums = [1]
    Output: []

    """
    nums = sorted(nums)
    value = []
    for x in range(len(nums)-1):
        if nums[x] == nums[x+1]:
            value.append(nums[x])
    return value

def array_intersection(m,n,arr,brr):
        # Return a list containing all the common elements in arr and brr.
    inter = []
    for ind1 in range(n):
        for ind2 in range(m):
            if arr[ind1] == brr[ind2]:
                inter.append(arr[ind1])
                brr[ind2] = float(inf)
                break
    
    if len(inter) == 0:
        return [-1]
    else:
        return inter
    
def array_intersection_optimised(m,n,arr,brr):
    inter = []
    i = 0
    j = 0
    while(i<n and j<m):
        if arr[i] < brr[j]:
            i += 1
        elif arr[i] == brr[j]:
            inter.append(arr[i])
            i += 1
            j += 1
        elif arr[i] > brr[j]:
            j += 1

    
    if len(inter) == 0:
        return [-1]
    else:
        return inter
    
def pairSum(arr, s):
    """
    Sample Input 1:
    5 5
    1 2 3 4 5
    Sample Output 1:
    1 4
    2 3
    Explaination For Sample Output 1:
    Here, 1 + 4 = 5
        2 + 3 = 5
    Hence the output will be, (1,4) , (2,3).
"""
    first_index = 0
    second_index = 1
    lis = []
    # temp = []
    for first in range(len(arr)):
        for second in range(first+1,len(arr)):
            if arr[first] + arr[second] == s:
                temp = []
                temp.append(min(arr[first],arr[second]))
                temp.append(max(arr[first],arr[second]))
                lis.append(temp)
            # temp = []
    # print(lis)
    lis.sort()
    return lis

