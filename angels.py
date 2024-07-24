# --- Imports --- #

from typing import Self
from enum import IntEnum, auto
from dataclasses import dataclass, field

__all__ = ("AngelType", "Angel")


# --- AngelType Enum --- #

class AngelType(IntEnum):
    """The 9 different types of Angels according to the Bible"""
    GUARDIAN = auto()
    ARCHANGEL = auto()
    PRINCIPALITIES = auto()
    POWERS = auto()
    VIRTUES = auto()
    DOMINIONS = auto()
    OPHANIM = auto()
    CHERUBIM = auto()
    SERAPHIM = auto()

    def __str__(self) -> str:
        return self.name.replace("_", " ").title()


# --- Angel Class --- #

@dataclass(repr=True, unsafe_hash=True, slots=True)
class Angel:
    """An Angel according to the Bible"""
    name: str
    type: AngelType

    def __str__(self) -> str:
        return f"{self.type} {self.name}".rstrip()


if __name__ == "__main__":
    def main():
        Michael = Angel("Michael", AngelType.ARCHANGEL)
        Seraphim = Angel("", AngelType.SERAPHIM)
        Michael2 = Angel("Michael", AngelType.ARCHANGEL)
    
        print(Michael == Seraphim)
        print(Michael.type > Seraphim.type)
        print(Michael.type < Seraphim.type)
        print(Michael == Michael2)
        print(Michael, Seraphim, sep="\n")

    main()
