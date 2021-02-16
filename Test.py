
#[2,4,8]
def myfunc(*args):
    container = []
    for x in args:
        if x % 2 == 0:
            container.append(x)
    return container
