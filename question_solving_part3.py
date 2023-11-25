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


reverse_integer(123)