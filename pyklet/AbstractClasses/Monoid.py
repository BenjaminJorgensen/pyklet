from __future__ import annotations
from typing import TypeVar, Generic
from abc import abstractmethod, ABC
from ..Prelude.Functions import lazy

T = TypeVar('T')
class Monoid(Generic[T], ABC):
    @abstractmethod
    def mappend(self, other: T) -> T:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def mempty() -> T:
        raise NotImplementedError

    def __str__(self):
        return self.__class__.__name__


# Standalone definitions
@lazy
def mappend(m1: Monoid, m2: Monoid) -> Monoid:
    return m1.mappend(m2)
