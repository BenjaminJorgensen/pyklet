from __future__ import annotations
from typing import Callable, Any, List
from inspect import signature
from pyklet.AbstractClasses import Monoid


# Takes Exactly one function
class PykletFunction(Monoid):
    def __init__(self, f):
        self.function = f
        # args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations = (
        #     getfullargspec(f)
        # )

        # # Check Error States
        # # TODO: include kwargs
        # if len(args) > 1 or varargs or varkw:
        #     raise ValueError("PykletFunction Functions must only take a single argument")

    def __call__(self, arg) -> PykletFunction | Any:
        # return PykletFunction(partial(self.function, arg))
        return self.function(arg)

    def apply(self, x) -> PykletFunction | Any:
        return self(lazy(x))

    def reverseApply(self, x) -> PykletFunction | Any:
        return lazy(x(self))

    def compose(self, other) -> PykletFunction | Any:
        return PykletFunction(lambda x: self(other(x)))

    def reverseCompose(self, other) -> PykletFunction | Any:
        return PykletFunction(lambda x: other(self(x)))

    def __or__(self, x) -> PykletFunction | Any:
        return self.apply(x)

    def __ror__(self, x) -> PykletFunction | Any:
        return self.reverseApply(x)

    def __truediv__(self, x) -> PykletFunction | Any:
        return self.apply(x)

    def __rtruediv__(self, x) -> PykletFunction | Any:
        return self.reverseApply(x)

    def __mul__(self, x) -> PykletFunction | Any:
        return self.compose(x)

    def __rmul__(self, x) -> PykletFunction | Any:
        return self.reverseCompose(x)

    # Monoid
    # Only Monoid if Function return type is also Monoid
    def mappend(self, other):
        # mappend f g = \x -> f x `mappend` g x
        def f(x):
            v1 = self.function(x)
            v2 = other(x)
            if not isinstance(v1, Monoid) or not isinstance(v2, Monoid):
                raise ValueError("Both return values must be Monoid instances")
            return v1.mappend(v2)

        return PykletFunction(f)

    @staticmethod
    def mempty():
        return PykletFunction(identity)

    def __str__(self) -> str:
        return f"PykletFunction({self.function})"

    def __repr__(self) -> str:
        return f"PykletFunction(\n{self.function}\n)\n"


def identity(x):
    return x


makeLazy = PykletFunction(identity)


def __lazy(func, parameters, index, args: List) -> PykletFunction:
    if index == len(parameters):
        return func(*args)
    return PykletFunction(lambda x: __lazy(func, parameters, index + 1, args + [x]))


# Lazy should construct a nest of PykletFunctions
def lazy(func) -> PykletFunction:
    if not callable(func) or isinstance(func, PykletFunction):
        return func
    parameters = list(signature(func).parameters.keys())
    return __lazy(func, parameters, 0, [])


@lazy
def compose(f: Callable, g: Callable):
    return PykletFunction(lambda x: f(g(x)))
