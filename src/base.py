from __future__ import annotations

from _decimal import Decimal
from functools import reduce
from functools import total_ordering
from operator import mul
from typing import Any
from typing import List
from typing import Type
from typing import cast


@total_ordering
class Magnitude:
    base_magnitude: Type[Magnitude] | None
    base: int
    order: int
    value: Any

    def __init__(self, value: Any = 1):
        self.value = value

    def __rmul__(self, other) -> Magnitude:
        if not isinstance(other, (int, float, Decimal)):
            return NotImplemented

        return self.__class__(self.value * other)

    @classmethod
    def get_minor_unit_class(cls) -> Type[Magnitude]:
        """Recursively get minor unit class"""
        if cls.is_minor_unit():
            return cls

        return cls.base_magnitude.get_minor_unit_class()

    @classmethod
    def is_minor_unit(cls) -> bool:
        return cls.base_magnitude is None

    def bases_are_comparable(self, other) -> bool:
        return (
            isinstance(other, Magnitude)
            and self.get_minor_unit_class() is other.get_minor_unit_class()
        )

    def __eq__(self, other) -> bool:
        if not self.bases_are_comparable(other):
            return NotImplemented

        return self.to_minor_units().value == other.to_minor_units().value

    def __lt__(self, other) -> bool:
        if not self.bases_are_comparable(other):
            return NotImplemented

        return self.to_minor_units().value < other.to_minor_units().value

    def __str__(self) -> str:
        return f"{self.value} {self.__class__.__name__}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.value})"

    @classmethod
    def get_base_magnitudes(cls) -> List[Magnitude]:
        bases = [cls]
        base = cls.base_magnitude
        while base is not None:
            bases.append(base)
            base = base.base_magnitude

        return bases

    @classmethod
    def get_multiplier(cls):
        multipliers = (magnitude.base**magnitude.order for magnitude in cls.get_base_magnitudes())
        return reduce(mul, multipliers, 1)

    def to_minor_units(self):
        minor_unit = self.get_minor_unit_class()
        return minor_unit(self.value * self.get_multiplier())

    @classmethod
    def from_minor_units(cls, value) -> Magnitude:
        minor_unit_class = cls.get_minor_unit_class()
        if cls is minor_unit_class:
            return cls(value)

        return cls(Decimal(value) / Decimal(cls.get_multiplier()))

    def convert_to(self, magnitude: Magnitude | Type[Magnitude]) -> Magnitude:
        if isinstance(magnitude, Magnitude):
            magnitude = type(magnitude)

        in_minor_units = self.to_minor_units()
        return magnitude.from_minor_units(in_minor_units.value)

    @classmethod
    def create_magnitude(
        cls,
        name: str,
        base_magnitude: Type[Magnitude] | None = None,
        base: int | None = 1,
        order: int | None = 0,
    ) -> Type[Magnitude]:
        new_type = type(
            name,
            (Magnitude,),
            dict(base_magnitude=base_magnitude, base=base, order=order),
        )
        return cast(Type[Magnitude], new_type)
