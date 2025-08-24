# fido = Animal(animal='dog', colour='black', speed='fast')
# sonic = Animal(animal='hedgehog', colour='blue', speed='fast')

# isHedg = lambda x: x.animal == 'hedgehog'
# isFast = lambda x: x.speed == 'fast'
# isBlue = lambda x: x.colour == 'blue'

# predicates = MList([
#     isHedg,
#     isBlue,
#     isFast,
# ])

# isSonic = lambda animal: predicates.foldMap(lambda pred: All(pred(animal))).getAll()

# print(isSonic(fido))    # False
# print(isSonic(sonic))   # True


# def succ(x):
#     return x + 1


# function = map succ [1,2,3,4,5]

# ex = "something"

# print(ex.capitalize())


# **
# *, /, //, %,
# >>, <<
# &
# |
