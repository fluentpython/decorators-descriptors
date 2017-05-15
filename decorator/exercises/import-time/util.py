print('<A>')

def deco(f):
    print('<B>')
    def inner():
        print('<C>')
        f()
    return inner

print('<D>')    
