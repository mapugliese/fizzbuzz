def fizz_buzz(num_range, type='list'):
    '''
    Prints a list or string containing numbers to a given value, replacing the
    value with 'fizz' if it is divisable by three, 'buzz' if it is divisible
    by five, and 'fizzbuzz' if it is divisible by both
    '''
    if type == 'string':
        string = ''
        for num in range(1, num_range+1):
            if num%3 == 0 and num%5 == 0:
                string += 'fizzbuzz '
            elif (num%3) == 0:
                string += 'fizz '
            elif (num%5) == 0:
                string += 'buzz '
            else:
                string += f'{num} '
        return string
    if type == 'list':
        num_list = []
        for num in range(1, num_range+1):
            if num%3 == 0 and num%5 == 0:
                num_list.append('fizzbuzz')
            elif (num%3) == 0:
                num_list.append('fizz')
            elif (num%5) == 0:
                num_list.append('buzz')
            else:
                num_list.append(str(num))
        return num_list
    elif type not in ['list', 'string']:
        return TypeError
