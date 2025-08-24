# NOTE:
"""
Class hierarchy goes like this
    Monad -> Applicative -> Functor -> Moniod -> Foldable

    If you're looking an instance of a particular class
    check the highest applicable class in the hierarchy.

    E.g MonadicList -> Monad
"""

# Abstract Classes
from . import AbstractClasses
from . import Instances
from . import Prelude


__all__ = ["Prelude", "Instances", "AbstractClasses"]
