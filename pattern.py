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


def pattern4(n):
    """
    1 2 3 4 5

    1 2 3 4 5

    1 2 3 4 5

    1 2 3 4 5

    1 2 3 4 5
    """
    for row in range(1,n+1):
        for column in range(1,n+1):
            print(column,end=" ")
        print('\n')

def pattern5(n):
    """
    6 5 4 3 2 1 

    6 5 4 3 2 1

    6 5 4 3 2 1

    6 5 4 3 2 1

    6 5 4 3 2 1

    6 5 4 3 2 1
    """
    for row in range(1,n+1):
        for column in range(1,n+1):
            print(n+1-column,end=' ')
        print('\n')

def pattern6(n):
    """
    1 

    2 3

    4 5 6

    7 8 9 10
    """
    temp = 1
    for row in range(n):
        for column in range(n):
            if column <= row:
                print(temp,end=' ')
                temp += 1
        print('\n')

def pattern7(n):
    # temp = 1
    """
    1 

    2 3

    3 4 5

    4 5 6 7
    """
    for row in range(n):
        temp = row
        for column in range(n):
            if column <= row:
                temp += 1   
                print(temp,end=' ')

        print('\n')

pattern7(4)
#https://youtu.be/dr-pLeJBr38?list=PLDzeHZWIZsTryvtXdMr6rPh4IDexB5NIA&t=885


