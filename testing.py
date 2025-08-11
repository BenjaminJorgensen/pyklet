from __future__ import annotations
from typing import TypeVar, Generic, Callable
from pyklet import Monoid, Monad

G = TypeVar('G', bound=Monoid)
class Logger(Monad['Logger'], Generic[G]):
    def __init__(self, value, l: G) -> None:
        self.log = l
        self.value = value

    @staticmethod
    def pure(value, moniodType: type[G]) -> Logger: # pyright: ignore
        return Logger(value, moniodType.mempty())

    # bind :: m a -> (a -> m b) -> m b
    def bind(self, f: Callable[[Any], Logger[G]]) -> Logger[G]:
        mb = f(self.value)
        self.log = self.log.mappend(mb.log)
        self.value = mb.value
        return Logger(self.value, self.log)

    def tell(self, moniod: G) -> Logger[G]:
        return Logger(self.value, self.log.mappend(moniod))

    def fmap(self, f: Callable) -> Logger[G]:
        return Logger(f(self.value), self.log)

    def ap(self, other: Logger) -> Logger:
        return self

    def __str__(self) -> str:
        return f"Result: {self.value}\n\nLog:\n{self.log}"

# V = TypeVar('V')
# class MList(list, Monad, Monoid, Foldable, Generic[V]):
#     def __init__(self, arg: List[V] | V) -> None:
#         if isinstance(arg, list):
#             return super().__init__(arg)
#         return super().__init__([arg])

#     # NOTE: Moniod
#     @staticmethod
#     def mempty() -> MList: return MList([])

#     def mappend(self, other: MList) -> MList:
#         return MList(self + other)

#     def fmap(self, f: Callable) -> MList:
#         return MList(list(map(f, self)))

#     # NOTE: Monad
#     @staticmethod
#     def pure() -> MList:
#         return MList([]);

#     # bind :: m a -> (a -> m b) -> m b
#     def bind(self, f: Callable[..., MList]) -> MList:
#         return MList([y for x in self for y in f(x)])

#     # NOTE: Applicative
#     # <*> :: f ( a -> b ) -> f a -> f b
#     def ap(self, other: MList) -> MList:
#         return MList([f(b) for f in self for b in other])

#     def __str__(self):
#         return list.__str__(self)



# class Any(Monoid):
#     def __init__(self, value: bool) -> None:
#         self.value = value

#     def mappend(self, other: Any) -> Any:
#         return Any(self.value or other.value)

#     @staticmethod
#     def mempty() -> Any:
#         return Any(False)

#     def getAny(self) -> bool:
#         return self.value

#     def __str__(self):
#         return f"{super().__str__()}({self.value})"

#     # (.) :: (b -> c) -> (a -> b) -> a -> c
#     def __ror__(self, t) -> Callable:
#         # lambda predicate : Any(predicate(x))
#         return lambda f: Any(f(t))



def zipWith(f, a, b):
    print(list(zip(a,b)))
    return list(map(lambda x: f(x[0],x[1]), zip(a,b)))

def repeat(val):
    while True:
        yield val

if __name__ == "__main__":
    print("hello world")
