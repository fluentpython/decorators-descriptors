from functools import wraps

def floatify(f):

    @wraps(f)
    def floated(n):
        result = f(n)
        return float(result)
    
    return floated

