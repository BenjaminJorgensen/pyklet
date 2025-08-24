from __future__ import annotations
from typing import Generic, Iterable, TypeVar, List, Callable

from pyklet.AbstractClasses import Monad, Monoid, Foldable

V = TypeVar("V")


class MonadicSet(set, Monad, Monoid, Foldable, Generic[V]):
    def __init__(self, arg: List[V] | V) -> None:
        if isinstance(arg, Iterable):
            return super().__init__(arg)
        return super().__init__([arg])

    # Moniod
    @staticmethod
    def mempty() -> MonadicSet:
        return MonadicSet([])

    def mappend(self, other: MonadicSet) -> MonadicSet:
        return MonadicSet(self.union(other))

    def fmap(self, f: Callable) -> MonadicSet:
        return MonadicSet(map(f, self))

    # Monad
    @staticmethod
    def pure() -> MonadicSet:
        return MonadicSet([])

    # bind :: m a -> (a -> m b) -> m b
    def bind(self, f: Callable[..., MonadicSet]) -> MonadicSet:
        return MonadicSet((y for x in self for y in f(x)))

    """
     Applicative
    <*> :: f ( a -> b ) -> f a -> f b
    """

    def ap(self, other: MonadicSet) -> MonadicSet:
        return MonadicSet((f(b) for f in self for b in other))

    def __str__(self):
        return set.__str__(self)


class __monadic_set_constructor__:
    def __getitem__(self, *args, **kwargs):
        return MonadicSet(*args, **kwargs)


MSet = MonadicSet
