from __future__ import annotations
from pyklet.Instances import MSet, MList
from pyklet.Prelude import lazy, filter
from pyklet.Prelude.io import putStrLn


class Pos:
    def __init__(self, x, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: Pos) -> Pos:
        return Pos(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({chr(ord('A') + self.x)}, {self.y})"

    def __repr__(self):
        return f"{self.x, self.y}"


def knightInThreeMoves(knight_dirs: MSet, knight_pos=Pos("B", 3)):
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

    # Checks if position is valid on a chessboard
    def inBounds(position):
        return position.x in range(0, 8) and position.y in range(0, 8)

    def nextMove(pos: Pos) -> MSet[Pos]:
        """Takes a position and returns a set of valid next moves"""

        # The '@' syntax is sugar for mapping a function to a data structure (Functor)
        # Equivalent to `map(lazyadd(pos), knight_dirs)` (sort of)
        new_positions = lazy(lambda x: pos + x) >> knight_dirs

        return filter / inBounds / new_positions

    # Monadic binding the nextMove function
    # all_moves = MSet(knight_pos).bind(nextMove).bind(nextMove).bind(nextMove)
    all_moves = MSet(knight_pos).bind(nextMove).bind(nextMove).bind(nextMove)
    return all_moves


if __name__ == "__main__":

    def flip(x):
        return (x[1], x[0])

    xmoves = MList[1, -1]
    ymoves = MList[2, -2]

    moves = lazy(lambda x, y: (x, y)) >> xmoves ^ ymoves
    knight_deltas = moves.mappend(flip >> moves).fmap(lambda x: Pos(x[0], x[1]))
    knight_deltas = MSet(knight_deltas)
    putStrLn / knight_deltas

    start = Pos(3, 3)
    _ = lazy(print) / knightInThreeMoves(knight_deltas, knight_pos=start)

    # def rotate(x:
    #     for _ in range(len(x) // 2):
    #         x.insert(0, x.pop())
    #     return x

    # func = makeLazy * "-".join * rotate * list * str / 12345
    # print(func)
