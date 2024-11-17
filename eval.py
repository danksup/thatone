from functools import reduce

def OneElmt(L):
    return len(L) == 1

def eval(expression, steps=False):
    if isinstance(expression, list):    
        expr = expression
    else:
        expr = expression.split(' ')

    def op_search(op):
        after_op = expr.index(op) + 1 
        before_op = expr.index(op) - 1 

        ret = float(expr[before_op]), float(expr[after_op])

        return list(ret), before_op, after_op

    exp = '^'
    mul = '*'
    add = '+'
    sub = '-'
    div = '/'

    result = ''

    while len(expr) > 1: 
        if  not any(item in expr for item in [exp]):
            break;
        if steps:
            print(expr)
        if exp in expr:
            search, before, after = op_search(exp)
            result = reduce(lambda x, y: x ** y, search)
            expr[before:after+1] = [str(result)]

    while len(expr) > 1: 
        if  not any(item in expr for item in [mul, div]):
            break;
        if steps:
            print(expr)

        if mul in expr or div in expr:
            if mul in expr:
                search, before, after = op_search(mul)
                result = reduce(lambda x, y: x * y, search)
                expr[before:after+1] = [str(result)]
            elif div in expr:
                search, before, after = op_search(div)
                if search[1] == 0:
                    return "you cant divide by zero silly :3"
                result = reduce(lambda x, y: x / y, search)
                expr[before:after+1] = [str(result)]

    while len(expr) > 1: 
        if  not any(item in expr for item in [add, sub]):
            break;
        if steps:
            print(expr)

        if add in expr:
            search, before, after = op_search(add)
            result = reduce(lambda x, y: x + y, search)
            expr[before:after+1] = [str(result)]
        elif sub in expr:
            search, before, after = op_search(sub)
            result = reduce(lambda x, y: x - y, search)
            expr[before:after+1] = [str(result)]

    return result

# print(eval('12 + 9 + 9 - 9 * 2 - 10 - 19 ^ 2', True)) 
