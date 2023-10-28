#! /usr/bin/python3


from typing import List


class Jet():
    def __init__(self, order: List[str]) -> None:
        self.order = list(order)
        self.current_id = 0

    @property
    # pylint: disable=C0116
    def current(self) -> str:
        direction = self.order[self.current_id % len(self.order)]
        self.next()
        return direction

    # pylint: disable=C0116
    def next(self) -> None:
        self.current_id += 1
