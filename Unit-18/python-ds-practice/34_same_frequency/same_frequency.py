
def create_dicts_with_num(num_list):
    freqDict_num = dict()
    visited_num = set()
    for num in num_list:
        if num in visited_num:
            freqDict_num[num] = freqDict_num[num] + 1
        else:
            freqDict_num[num] = 1
            visited_num.add(num)
    return freqDict_num



def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
   
    num1_list = [int(num) for num in str(num1)] #convert the num1 and num2 into a list of the digits
    num2_list = [int(num) for num in str(num2)]

    freqdict_num1 = create_dicts_with_num(num1_list)
    freqdict_num2 = create_dicts_with_num(num2_list)

    if freqdict_num1 == freqdict_num2:
        return True
    else: 
        return False

