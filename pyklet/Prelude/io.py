from .pyklet_function import lazy


# TODO:
# Put into proper IO monad?
@lazy
def putStrLn(x):
    print(x)
    return x
