from __future__ import annotations
from typing import Callable, Generic, TypeVar
from abc import abstractmethod, ABC
from ..Prelude.Functions import lazy

T = TypeVar('T')
class Functor(Generic[T], ABC):
    # fmap :: (a -> b) -> f a -> f b
    @abstractmethod
    def fmap(self, f: Callable[..., T]) -> T:
        raise NotImplementedError

    def __rmatmul__(self, f: Callable[..., T]) -> T:
        return self.fmap(f)

@lazy
def fmap(f: Callable, functor: Functor) -> Functor:
    return functor.fmap(f)
