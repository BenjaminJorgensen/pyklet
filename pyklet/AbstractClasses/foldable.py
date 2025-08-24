from __future__ import annotations
from typing import Callable, Generic, TypeVar, Iterable
from abc import ABC
from functools import reduce

from .monoid import Monoid


V = TypeVar("V")
T = TypeVar("T", bound=Monoid)
C = TypeVar("C", bound="Foldable")


class Foldable(Generic[V, T], ABC):
    # foldMap :: Monoid m => (a -> m) -> t a -> m
    def foldMap(self, f: Callable[..., T]) -> T:
        if not isinstance(self, Iterable):
            raise NotImplementedError(
                f"{self.__class__.__name__} does not have foldMap or a valid iterable defined"
            )
        return reduce(lambda x, acc: acc.mappend(x), map(f, self.__iter__()))

    # filter :: (a -> Bool) -> [a] -> [a]
    def filter(self: C, f: Callable[..., bool]) -> C:
        if not isinstance(self, Iterable):
            raise NotImplementedError(
                f"{self.__class__.__name__} does not have filter or a valid iterable defined"
            )
        return type(self)((x for x in self.__iter__() if f(x)))  # type: ignore
