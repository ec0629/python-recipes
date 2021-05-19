from typing import Callable, Dict, Iterable, List, Optional, Tuple


def total(xs: List[float]) -> float:
    return sum(xs)


# for Callable the first param is a list of the param types
# in this case a str followed by an int
# the second param is the return value in this case a str
def twice(repeater: Callable[[str, int], str], s: str) -> str:
    return repeater(s, 2)


def comma_repeater(s: str, n: int) -> str:
    n_copies = [s for _ in range(n)]
    return ', '.join(n_copies)


assert twice(comma_repeater, "type hints") == "type hints, type hints"


# needed to turn Pylance type checking mode on
# total(['s', 's', 's']) # will show an error
total([7.8, 9.8])

x: int = 5

values: List[int] = []
best_so_far: Optional[float] = None  # allowed to be a float or None
counts: Dict[str, int] = {'data': 1, 'science': 2}

lazy: bool = True

if lazy:
    evens: Iterable[int] = (x for x in range(10) if x % 2 == 0)
else:
    evens = [0, 2, 4, 6, 8]

triple: Tuple[int, float, int] = (10, 2.3, 5)
