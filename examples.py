from pyklet.Prelude import lazy, makeLazy
from pyklet.Instances import MList

if __name__ == "__main__":

    @lazy
    def story(person: str, action: str, place: str) -> str:
        return f"{person} did {action} at {place}"

    # New function application
    # Equivalent to story("Benjamin", "swim", "beach")
    holiday = story / "Benjamin" / "Swim" / "beach"
    print(holiday)  # "Benjamin did swim at beach"

    # Partial function application,
    david_runs = story / "David" / "run"

    # Can be used later
    marathon = david_runs / "France"
    print(marathon)  # -> "David did ran at France"

    # Can map functions to lists
    # Equivalent to map(david_runs, ["Gym", "School", "Train Station"])
    running_jornal = david_runs >> MList["Gym", "School", "Train Station"]
    print(
        running_jornal
    )  # ["David did run at Gym", "David did run at School", "Train Station"]

    # Function Composition
    to_digits = lazy(list) * str
    print(to_digits / 123)  # -> ['1', '2, '3']

    # Works with native functions (including strings)
    def rotate(x):
        for _ in range(len(x) // 2):
            makeLazy / x.insert / 0 / x.pop()
        return x

    rotated_pin = makeLazy * "-".join * rotate * list * str / 123456
    print(rotated_pin)  # -> 4-5-6-1-2-3
