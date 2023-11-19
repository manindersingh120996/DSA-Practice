#fibonacchi question
def fibonacci(length):
    n1 = 0
    n2 = 1
    temp = 0
    print(n1,end=' ')
    print(n2, end=' ')
    for x in range(length):
        temp = n1 + n2
        print(temp,end=' ')
        n1 = n2
        n2 = temp

fibonacci(5)