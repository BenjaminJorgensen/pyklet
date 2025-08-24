from typing import Callable, TypeVar
from .pyklet_function import lazy
from inspect import signature

# External imports
from pyklet.AbstractClasses import Monoid, Functor, Applicative, Monad, Foldable


# Monoid
@lazy
def mempty(m1: Monoid) -> Monoid:
    return m1.mempty()


@lazy
def mappend(m1: Monoid, m2: Monoid) -> Monoid:
    return m1.mappend(m2)


# Functor
@lazy
def fmap(f: Callable, functor: Functor) -> Functor:
    return functor.fmap(f)


# Applicative
@lazy
def ap(a1: Applicative, a2: Applicative) -> Applicative:
    return a1.ap(a2)


# NOTE:
# Not calling lazy bind and see what happens
def bind(m1: Monad, f: Callable) -> Monad:
    return m1.bind(f)


# TODO:
# Turn this into a PykletFunction
def binds(binding_param: str) -> Callable[..., Callable]:
    def bindable_func(func: Callable) -> Callable:
        sig = signature(func)
        param_names = sig.parameters.copy()
        if binding_param not in param_names.keys():
            raise ValueError(
                f'Parameter "{binding_param}" not found in function "{func.__name__}"'
            )

        def wrapper(*args, **kwargs) -> Callable:
            if param_names.get(binding_param):
                param_names.pop(binding_param)
            if kwargs.get(binding_param):
                kwargs.pop(binding_param)
            bound_args = dict(zip(param_names, args))
            bound_args |= kwargs
            if len(args) + len(kwargs) != len(param_names):
                return func(*args, **kwargs)
            return lambda a: func(**bound_args, **{binding_param: a})

        return wrapper

    return bindable_func


# Foldable
@lazy
def filter(f: Callable[..., bool], foldable: Foldable) -> Foldable:
    return foldable.filter(f)


T = TypeVar("T", bound=Monoid)


@lazy
def foldMap(f: Callable[..., T], foldable: Foldable) -> T:
    return foldable.foldMap(f)
