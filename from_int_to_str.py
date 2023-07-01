def from_int_to_str(number: int):
    if number == 0:
        return 'zero'

    one_digit = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }
    two_digit = {
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'
    }

    tens = {
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety'
    }

    if len(str(number)) == 1:
        return one_digit[number]
    if len(str(number)) == 2:
        if number > 19:
            return tens[int(str(number)[0])] + ' ' + one_digit[int(str(number)[1])]
        else:
            return two_digit[number]
    if len(str(number)) == 3:
        result = ''
        result += one_digit[int(str(number)[0])] + ' hundred '
        if int(str(number)[1:]) != 0:
            result += from_int_to_str(int(str(number)[1:]))
        return result
    if len(str(number)) == 4:
        result = ''
        result += one_digit[int(str(number)[0])] + ' thousand ' + one_digit[int(str(number)[1])] + ' hundred '
        if int(str(number)[2:]) != 0:
            result += from_int_to_str(int(str(number)[2:]))
        return result
from_user = int(input('Enter the number:\n'))
print(from_int_to_str(from_user))