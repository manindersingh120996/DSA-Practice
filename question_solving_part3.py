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
    

def base_10_complement(number):
    """
    Taking input as integer making it complement in binary form
    and converting that complement back to integer
    example : input = 5
    output = 2
    explanation : 5 in binary "101", it's complement is "010" which is integer 2
    """
    position = 0
    value = 0
    while number != 0:
        bin_val = number & 1
        if bin_val == 0:
            bin_val = 1
        elif bin_val == 1 :
            bin_val = 0
        number = number >> 1
        value = value + (bin_val * (2**(position)))
        position += 1 
    print(value)

base_10_complement(2)
