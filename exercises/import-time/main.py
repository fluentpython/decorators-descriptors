from util import deco

print('<1>')

@deco
def first():
    print('<2>')

@deco
def second():
    third()
    print('<3>')

def third():
    print('<4>')

if __name__=='__main__':
    first()
    second()
    print('<6>')
