from __future__ import annotations
from typing import TypeVar, Callable
from abc import abstractmethod
from inspect import signature

# Custom imports 
from .Applicative import Applicative

T = TypeVar('T')
class Monad(Applicative[T]):
    @staticmethod
    @abstractmethod
    def pure() -> T: # type: ignore
        raise NotImplementedError

    # bind :: m a -> (a -> m b) -> m b
    def __rshift__(self, f: Callable) -> T:
        return self.bind(f)

    @abstractmethod
    def bind(self, f: Callable) -> T:
        raise NotImplementedError
