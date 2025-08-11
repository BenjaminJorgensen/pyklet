from .PykletFunction import PykletFunction
from typing import Callable

def lazy(func: Callable) -> PykletFunction:
    return func if isinstance(func, PykletFunction) else PykletFunction(func)

make_lazy = PykletFunction(lambda x: x)

@lazy
def compose(f: Callable, g: Callable):
    return PykletFunction(lambda x: f(g(x)))
