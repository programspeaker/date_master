from exceptions import *

month_constants = {
    1:'Januvary',
    2:'Februvary',
    3:'March',
    4:'April',
    5:'May',
    6:'June',
    7:'July',
    8:'August',
    9:'September',
    10:'October',
    11:'November',
    12:'December'
}

def check_params_keys(params):
    result = True
    if type(params) == dict:
        for item in params:
            if item == 'date' or item == 'order' or item == 'format' or item == 'split_by':
                    pass
            else:
                result = 'Invalid date_master parameter' 
    else:
        result = 'Invalid date_master parameter' 
    return result
    

# Function for check value is integer
def isinteger(value):
    if isinstance(value, int):
        return True
    else:
        return 0


# Function for checking the limit
def checklimit(value, order_string):
    if order_string == 'DD':
        if 1 <= value <= 31:
            return True
        else:
            return 0
    if order_string == 'MM':
        if 1 <= value <= 12:
            return True
        else:
            return 0
    if order_string == 'YYYY':
        if 1000 <= value <= 9999:
            return True
        else:
            return 0
    else:
        return 0


# Function for checking the date
def date_validation(date):
    try:
        if len(date) == 3:
            for item in range(len(date)):
                if item == 0:
                    if isinteger(date[item]) and checklimit(date[item], 'DD') == True:
                        pass
                    else:
                        result = 'Invalid Day'
                        break
                elif item == 1:
                    if isinteger(date[item]) and checklimit(date[item], 'MM') == True:
                        pass
                    else:
                        result = 'Invalid Month'
                        break
                elif item == 2:
                    if isinteger(date[item]) and checklimit(date[item], 'YYYY') == True:
                        return True
                    else:
                        result = 'Invalid Year'
                        break
        else:
            result = 'Invalid Date'
        return result

    except Exception as e:
        return e


# Function for checking the format
def format_validation(format):
    result = True

    if len(format) == 3 and type(format)==list:
        for item in format:
            if item == 'int' or item =='str':
                pass
            else:
                result = 'Invalid format'
                break
    else:
        result = 'Invalid format'
    return result


# Function for checking the order data
def order_validation(order):
    result = True

    if len(order) == 3 and type(order)==list:
        order = [x.upper() for x in order]        
        for item in order:
            if item == 'MM' or item == 'DD' or item == 'YYYY':
                pass
            else:
                result = 'Invalid order '
    else:
        result = 'Invalid order'
    return result


# Function for checking the split
def split_validation(split):
    result = True

    if len(split) == 1 and type(split)==list and  type(split[0]) == str:        
        pass
    else:
        result = 'Invalid split'
    return result