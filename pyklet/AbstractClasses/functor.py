from __future__ import annotations
from typing import Callable, Generic, TypeVar
from abc import abstractmethod, ABC

T = TypeVar("T")


class Functor(Generic[T], ABC):
    # fmap :: (a -> b) -> f a -> f b
    @abstractmethod
    def fmap(self, f: Callable[..., T]) -> T:
        raise NotImplementedError

    def __xor__(self, f: Callable[..., T]) -> T:
        return self.fmap(f)
