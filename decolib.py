"""Simple decorator example"""

def floatify(f):
    def floated(n):
        result = f(n)
        return float(result)
    return floated