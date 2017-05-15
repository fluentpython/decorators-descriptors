registry = []

def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')

if __name__ == '__main__':
    print('running top level of module')
    print('registry: ', registry)
    f1()
