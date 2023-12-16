def reverse_integer(number):
    """
    input = 123
    output = 321

    input = -123
    output = -321
    """
    def reversing_logic(num,value):
        num = abs(num)
        while num != 0:
            # print('quotient: ',int(num/10))
            # print('remainder: ',int(num%10))
            value = value + str(int(num%10))
            num = int(num/10)
        return int(value)

    
    if number > 0:
        value = ''
        print('Reversed Input number is : ',reversing_logic(number,value))
    elif number < 0:
        value = '-'
        print('Reversed Input number is : ',reversing_logic(number,value))
    else:
        print('No Reverse for input digit 0.')

def reverse_integer_2nd_way(number):
    # if number < 0:
    #     value = -0
    # elif number > 0:
    #     value = 0
    value = 0
    # number = abs(number)
    if number > 0 :
        while number != 0:
            remainder = int(number%10)
            value = (value * 10) + remainder
            number = int(number/10)
        print('Reversed Input number is : ',value)
    elif number < 0:
        number = abs(number)
        while number != 0:
            remainder = int(number%10)
            value = (value * 10) + remainder
            number = int(number/10)
        print('Reversed Input number is : ',-1*value)
    else:
        print('No Reverse for input digit 0.')
    

def base_10_complement(n):
    """
    Taking input as integer making it complement in binary form
    and converting that complement back to integer
    example : input = 5
    output = 2
    explanation : 5 in binary "101", it's complement is "010" which is integer 2
    """
    position = 0
    value = 0
    if n == 0:
        # print('inside if')
        print(f"Complement of input {n} is : {1}")
    elif n !=0:
        while n != 0:
            bin_val = n & 1
            if bin_val == 0:
                bin_val = 1
            elif bin_val == 1 :
                bin_val = 0
            n = n >> 1
            value = value + (bin_val * (2**(position)))
            position += 1 
        print(f"Complement of input {n} is : {value}")
import math
def power_of_two(n):
    """
    return True if input number is power of two
    example : input = 1
    output = true
    explanation 2^0 = 1
    leet code question: 231
    """
    if n<=0:
        print(bool(0))
    value = math.log(n) / math.log(2)
    # print(value)
    if 2**value == n:
        print(bool(1))
    else:
        print(bool(0))

power_of_two(3)




