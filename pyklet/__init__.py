
# NOTE: 
"""
Class hierarchy goes like this
    Monad -> Applicative -> Functor -> Moniod -> Foldable

    If you're looking an instance of a particular class
    check the highest applicable class in the hierarchy.

    E.g MonadicList -> Monad
"""

# Abstract Classes
from .AbstractClasses.Monad import Monad
from .AbstractClasses.Applicative import Applicative
from .AbstractClasses.Functor import Functor
from .AbstractClasses.Monoid import Monoid
from .AbstractClasses.Foldable import Foldable

# Monad Instances
from .Instances.Monad.MonadicList import MList, MonadicList
from .Instances.Monad.MonadicSet import MSet, MonadicSet

# Applicative Instances

# Functor Instances

# Moniod Instances

from .Prelude.Monadic import binds
from .Prelude.Functions import lazy, make_lazy, compose
