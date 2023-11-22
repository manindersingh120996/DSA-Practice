#fibonacchi question
def fibonacci(length):
    "0 1 1 2 3 5 8 13 21 34 55 89 "
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

# fibonacci(10)

def prime_number(num):
    if num == 1:
        print('Entered number 1 is neither nor Composite number.')
    else:
        halfnum = int(num/2)
        count = 0
        for value in range(1,halfnum+1):
            if num % value == 0:
                count +=1 
        if count == 1:
            print(f"Entered number {num} is a Prime Number.")
        if count >= 2:
            print(f"Entered number {num} is not a prime Number.")
# prime_number(24)

def leetcode_question1(num):
    """
    input n = 234
    output = 15
    explanation:
    product of digits = 2*3*4 = 24
    sum of digit = 2+3+4 =  9
    resutl = 24 - 9
    """
    sumv = 0
    product = 1
    for x in str(num):
        sumv += int(x)
        product *= int(x)
    print(f"Output : {product - sumv}")

leetcode_question1(4421)