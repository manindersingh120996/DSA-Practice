def pattern1(n):
    """
    ###
    ###
    ###
    """
    for row in range(n):
        for column in range(n):
            print('#',end=' ')
        print('\n')

def pattern2(n):
    """
    1 1 1
    2 2 2
    3 3 3
    """
    for row in range(1,n+1):
        for column in range(1,n+1):
            print(row,end=' ')
        print('\n')

def pattern3(n):
    """
    1 1 1 1 
    2 2 2
    3 3
    4
    """
    for row in range(1,n+1):
        for column in range(1,n+1):
            if row <= column :
                print(row,end=' ')
        print('\n')
pattern3(4)


