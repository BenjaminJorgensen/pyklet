from pyklet import lazy, make_lazy

@lazy
def putStrLn(x):
    print(x)
    return x
