from __future__ import annotations
from typing import  Callable
from inspect import signature
from functools import partial
from ..AbstractClasses.Monoid import Monoid


class PykletFunction(Monoid):
    def __init__(self, f):
        # The function to be called
        self.function = f
        params = signature(f).parameters

        # How many remaining arguments there are
        self.remaining_args = len(params)

    def __call__(self, *args, **kwargs) -> PykletFunction:
        if self.remaining_args <= len(args) + len(kwargs):
            return self.function(*args, **kwargs)
        return PykletFunction(partial(self.function, *args, **kwargs))

    # (|) :: (b -> c) -> (a -> b) -> a -> c
    def __or__(self, ab) -> PykletFunction:
        bc = self.function
        if not callable(ab): return bc(ab)
        ab = lazy(ab)
        return PykletFunction(lambda *args, **kwargs: bc(ab(*args, **kwargs)))

    # (|) :: (b -> c) -> (a -> b) -> a -> c
    def __ror__(self, ab) -> PykletFunction:
        bc = self.function
        if not callable(ab): return bc(ab)
        ab = lazy(ab)
        return PykletFunction(lambda *args, **kwargs: ab(bc(*args, **kwargs)))

    # Monoid
    # Only Monoid if Function return type is also Monoid
    def mappend(self, other):
        # mappend f g = \x -> f x `mappend` g x
        def f(x):
            v1 = self.function(x)
            v2 = other(x)
            if not isinstance(v1, Monoid) or not isinstance(v2, Monoid):
                raise ValueError(f"Both return values must be Monoid instances")
            return v1.mappend(v2)
        return PykletFunction(f)

    @staticmethod
    def mempty():
        return PykletFunction

def lazy(func: Callable) -> PykletFunction:
    return func if isinstance(func, PykletFunction) else PykletFunction(func)

make_lazy = PykletFunction(lambda x: x)

@lazy
def compose(f: Callable, g: Callable):
    return PykletFunction(lambda x: f(g(x)))
