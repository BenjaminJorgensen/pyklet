from __future__ import annotations
from typing import Generic, Iterable, TypeVar, List, Callable

from pyklet.AbstractClasses.Monad import Monad
from pyklet.AbstractClasses.Foldable import Foldable
from pyklet.AbstractClasses.Monoid import Monoid

V = TypeVar('V')
class MonadicList(list, Monad, Monoid, Foldable, Generic[V]):
    def __init__(self, arg: List[V] | V) -> None:
        if isinstance(arg, Iterable):
            return super().__init__(arg)
        return super().__init__([arg])

    # Moniod
    @staticmethod
    def mempty() -> MonadicList: return MonadicList([])

    def mappend(self, other: MonadicList) -> MonadicList:
        return MonadicList(self + other)

    def fmap(self, f: Callable) -> MonadicList:
        return MonadicList(map(f, self))

    # Monad
    @staticmethod
    def pure() -> MonadicList:
        return MonadicList([]);

    # bind :: m a -> (a -> m b) -> m b
    def bind(self, f: Callable[..., MonadicList]) -> MonadicList:
        return MonadicList((y for x in self for y in f(x)))

    """
     Applicative
    <*> :: f ( a -> b ) -> f a -> f b
    """
    def ap(self, other: MonadicList) -> MonadicList:
        return MonadicList((f(b) for f in self for b in other))

    def __str__(self):
        return list.__str__(self)

class __monadic_list_constructor__():
    def __getitem__(self, *args, **kwargs):
        return MonadicList(*args, **kwargs)

MList = __monadic_list_constructor__()
