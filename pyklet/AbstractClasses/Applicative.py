from __future__ import annotations
from typing import TypeVar
from abc import abstractmethod
from ..Prelude.Functions import lazy

# Custom imports
from .Functor import Functor

T = TypeVar('T')
class Applicative(Functor[T]):
    # pure :: a -> f a
    @staticmethod
    @abstractmethod
    def pure(_) -> T:
        raise NotImplementedError

    # <*> :: f ( a -> b ) -> f a -> f b
    def __xor__(self, other: T) -> T:
        return self.ap(other)

    @abstractmethod
    def ap(self, other: T) -> T:
        raise NotImplementedError

@lazy
def ap(a1: Applicative, a2: Applicative) -> Applicative:
    return a1.ap(a2)
