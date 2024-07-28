# f    = (x^2)*y * cos((z^2)*y)
# dx   = 2xy*cos((z^2)y)
# dxy  = 2xy*(-sin((z^2)y) * (z^2)) - ((2x) * (cos((z^2)y)))
# dxyz = 2xy*((-sin((z^2)y) * (2z)) - ((-cos((z^2)y)*(2zy)) * (z^2)) - ((2x) * (-sin((z^2)y) * (2zy))))



# input_func = list(input("equation: "))
input_func = "12*((34+5)+9)-(6/7)+89"

def test_if_int(var):
    try:
        int(var)
        return True
    except:
        return False

def test_if_const(sub_func, *args):
    """
    Checks if all elements in sub_func are constants

    Args:
        *args: Charicters (not intigers) that should be treated as constants

    Returns:
        bool: True if all elements in sub_func are contants, False otherwise.
    """
    print(args)
    for var in sub_func:
        if not all(var == "(" or 
                   var == ")" or 
                   var == "+" or
                   var == "-" or
                   var == "*" or
                   var == "/" or
                   var == "^" or
                   var in args for var2 in sub_func):
            if not test_if_int():
                return False
    return True


def list_to_str(lyst):
    ret_str = ""
    for i in lyst:
        ret_str += i
    return ret_str

def break_down(func, filter_char):
    close_paren = 0
    while close_paren >= 0:
        sub_func = ""
        close_paren = func.find(")")
        if close_paren >= 0:                                # if a ')' exists
            for open_paren in range(close_paren, -1, -1):
                if func[open_paren] == "(":                 # find the closest '(' 
                    func = list(func)
                    for i in range(open_paren, close_paren+1):
                        sub_func += (func.pop(open_paren))  # pop out the content within the parens
                    func = list_to_str(func)
                    further_break_down(sub_func)
                    break
    print(func)

def further_break_down(sub_func):   # do more of the other rules like product quotient and chain rule
    print("sub func =", sub_func)
    test_if_const()
                


break_down(input_func, ")")

print("\n",input_func)

