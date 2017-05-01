print('<1>')

registry = []

def register(func):
    print('<2>')
    registry.append(func)
    return func

@register
def f1():
    print('<3>')

if __name__ == '__main__':
    print('<4>')
    f1()
