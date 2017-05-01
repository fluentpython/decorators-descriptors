"""Simple decorator examples"""

def floatify(f):
    def floated(n):
        return float(f(n))
    return floated
