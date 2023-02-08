from __future__ import annotations

from .base import Magnitude
from .constants import BINARY
from .constants import DECIMAL

b = bit = Magnitude.create_magnitude("b")
Kib = Kibibit = Magnitude.create_magnitude("Kib", base_magnitude=bit, base=BINARY, order=10)
Mib = Mebibit = Magnitude.create_magnitude("Mib", base_magnitude=bit, base=BINARY, order=20)
Gib = Gibibit = Magnitude.create_magnitude("Gib", base_magnitude=bit, base=BINARY, order=30)
Tib = Tebibit = Magnitude.create_magnitude("Tib", base_magnitude=bit, base=BINARY, order=40)
Pib = Pebibit = Magnitude.create_magnitude("Pib", base_magnitude=bit, base=BINARY, order=50)
B = Byte = Magnitude.create_magnitude("B", base_magnitude=bit, base=BINARY, order=3)
KiB = KibiByte = Magnitude.create_magnitude("KiB", base_magnitude=Byte, base=BINARY, order=10)
MiB = MebiByte = Magnitude.create_magnitude("MiB", base_magnitude=Byte, base=BINARY, order=20)
GiB = GibiByte = Magnitude.create_magnitude("GiB", base_magnitude=Byte, base=BINARY, order=30)
TiB = TebiByte = Magnitude.create_magnitude("TiB", base_magnitude=Byte, base=BINARY, order=40)
PiB = PebiByte = Magnitude.create_magnitude("PiB", base_magnitude=Byte, base=BINARY, order=50)
Kb = Kilobit = Magnitude.create_magnitude("Kb", base_magnitude=bit, base=DECIMAL, order=3)
Mb = Megabit = Magnitude.create_magnitude("Mb", base_magnitude=bit, base=DECIMAL, order=4)
Gb = Gigabit = Magnitude.create_magnitude("Gb", base_magnitude=bit, base=DECIMAL, order=5)
Tb = Terabit = Magnitude.create_magnitude("Tb", base_magnitude=bit, base=DECIMAL, order=6)
Pb = Petabit = Magnitude.create_magnitude("Pb", base_magnitude=bit, base=DECIMAL, order=7)
KB = KiloByte = Magnitude.create_magnitude("KB", base_magnitude=Byte, base=DECIMAL, order=3)
MB = MegaByte = Magnitude.create_magnitude("MB", base_magnitude=Byte, base=DECIMAL, order=4)
GB = GigaByte = Magnitude.create_magnitude("GB", base_magnitude=Byte, base=DECIMAL, order=5)
TB = TeraByte = Magnitude.create_magnitude("TB", base_magnitude=Byte, base=DECIMAL, order=6)
PB = PetaByte = Magnitude.create_magnitude("PB", base_magnitude=Byte, base=DECIMAL, order=7)


__all__ = [
    "b",
    "Kib",
    "Mib",
    "Gib",
    "Tib",
    "Pib",
    "B",
    "KiB",
    "MiB",
    "GiB",
    "TiB",
    "PiB",
    "Kb",
    "Mb",
    "Gb",
    "Tb",
    "Pb",
    "KB",
    "MB",
    "GB",
    "TB",
    "PB",
    "bit",
    "Kibibit",
    "Mebibit",
    "Gibibit",
    "Tebibit",
    "Pebibit",
    "Byte",
    "KibiByte",
    "MebiByte",
    "GibiByte",
    "TebiByte",
    "PebiByte",
    "Kilobit",
    "Megabit",
    "Gigabit",
    "Terabit",
    "Petabit",
    "KiloByte",
    "MegaByte",
    "GigaByte",
    "TeraByte",
    "PetaByte",
]
