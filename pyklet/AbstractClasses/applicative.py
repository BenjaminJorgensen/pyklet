from __future__ import annotations
from typing import TypeVar
from abc import abstractmethod

# Local imports
from .functor import Functor

T = TypeVar("T")


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
