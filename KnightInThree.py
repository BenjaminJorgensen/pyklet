from __future__ import annotations
from ast import JoinedStr
from typing import Callable
from pyklet import MSet, MList, lazy, Monoid
from pyklet.Prelude.Functions import PykletFunction, make_lazy, compose
from pyklet.Prelude.IO import putStrLn



class Pos():
    def __init__(self, x, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: Pos) -> Pos:
        self.x += other.x
        self.y += other.y
        return Pos(self.x, self.y)

    def __str__(self):
        return f"({chr(ord('A') + self.x)}, {self.y})"

def knightInThreeMoves(knight_dirs: MSet, f: Callable, knight_pos=Pos('B',3)):
    """
    Goal:
        Given a set of tuples `knight_dirs` which contains all directions a
        knight can move on a chessboard (x,y), print all the possible squares the
        knight can reach in 3 moves

    Note:
        Pos class has addition defined as element-wise tuple addition.
        eg. (A,2) + (1,-1) = (B, 1)
    """
    # The lazy function allows partial application
    # We can supply too few arguments and defer execution until later
    lazyAdd = f(lambda x, y: x + y)

    # Checks if position is valid on a chessboard
    def inBounds(position):
        return position.x in range(0,8) and position.y in range(0,8)

    def nextMove(pos: Pos) -> MSet[Pos]:
        """ Takes a position and returns a set of valid next moves"""

        # The '@' sytax is sugar for mapping a function to a datastruture (Functor)
        # Equivilant to `map(lazyadd(pos), knight_dirs)` (sort of)
        new_positions = lazyAdd(pos) @ knight_dirs

        return new_positions.filter(inBounds)

    # Monadic binding the nextMove function
    all_moves = (
            MSet(knight_pos) 
            >> nextMove 
            >> nextMove 
            >> nextMove 
            )
    print(str @ all_moves)

    # '(B, 0)', '(D, 1)', '(B, 1)', '(A, 3)', '(B, 3)', '(E, 0)',
    # '(C, 4)', '(B, 7)', '(A, 0)', '(B, 6)', '(A, 4)', '(C, 5)', 
    # '(D, 0)', '(C, 3)', '(B, 2)', '(C, 1)', '(A, 2)', '(C, 0)',
    # '(D, 3)', '(A, 1)', '(A, 5)', '(D, 2)

if __name__ == "__main__":
    # flip = lambda x : (x[1], x[0])

    # xmoves = MList[1,-1]
    # ymoves = MList[2,-2]

    # moves = lazy(lambda x, y: (x,y)) @ xmoves ^ ymoves
    # knight_deltas = moves.mappend(flip @ moves).fmap(lambda x: Pos(x[0], x[1]))
    # knight_deltas = MSet(knight_deltas)

    # start = Pos(3,3)
    # knightInThreeMoves(knight_deltas, PykletFunction, knight_pos=start)
    class Animal():
        def __init__(self, animal, colour, speed) -> None:
            self.animal = animal
            self.colour = colour
            self.speed = speed

    class All(Monoid):
        def __init__(self, value: bool) -> None:
            self.value = value

        def mappend(self, other: All) -> All:
            return All(self.value and other.value)

        @staticmethod
        def mempty() -> All:
            return All(True)

        def __str__(self):
            return f"{super().__str__()}({self.value})"

        def getAll(self) -> bool:
            return self.value

    def getAll(a: All):
        return a.getAll()


    # isSonic = lambda animal: predicates.foldMap(lambda pred: make_lazy | All | pred | animal).getAll()

    rover = Animal(animal='dog', colour='black', speed='fast')
    sonic = Animal(animal='hedgehog', colour='blue', speed='fast')


    def isHedg(x): return x.animal == 'hedgehog'
    def isFast(x): return x.speed == 'fast'
    def isBlue(x): return x.colour == 'blue'


    predicates = MList[
        isHedg, 
        isBlue,
        isFast,
    ]


    isSonic = lazy(getAll) | predicates.foldMap(compose(All))
    print(isSonic(sonic))
    print(isSonic(rover))

    # isBlueHedge = lambda x: allHedge.mappend(allBlue)(x)

    

    # print(isSonic(fido))    # False
    # print(isSonic(sonic))   # True

    # to_str = lambda x: str(x)
    # to_list = lambda x: list(x)
    # def rotate(x):
    #     for _ in range(len(x) // 2):
    #         x.insert(0, x.pop())
    #     return x

    # func = putStrLn | "-".join | rotate | to_list | to_str | 12345
    

