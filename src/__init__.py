from __future__ import annotations

from src.base import Magnitude
from src.constants import BINARY
from src.constants import DECIMAL

b = bit = Magnitude.create_magnitude("bit")
Kib = Kibibit = Magnitude.create_magnitude("Kibibit", base_magnitude=bit, base=BINARY, order=10)
Mib = Mebibit = Magnitude.create_magnitude("Mebibit", base_magnitude=bit, base=BINARY, order=20)
Gib = Gibibit = Magnitude.create_magnitude("Gibibit", base_magnitude=bit, base=BINARY, order=30)
Tib = Tebibit = Magnitude.create_magnitude("Tebibit", base_magnitude=bit, base=BINARY, order=40)
Pib = Pebibit = Magnitude.create_magnitude("Pebibit", base_magnitude=bit, base=BINARY, order=50)

B = Byte = Magnitude.create_magnitude("Byte", base_magnitude=bit, base=BINARY, order=3)
KiB = KibiByte = Magnitude.create_magnitude("KibiByte", base_magnitude=Byte, base=BINARY, order=10)
MiB = MebiByte = Magnitude.create_magnitude("MebiByte", base_magnitude=Byte, base=BINARY, order=20)
GiB = GibiByte = Magnitude.create_magnitude("GibiByte", base_magnitude=Byte, base=BINARY, order=30)
TiB = TebiByte = Magnitude.create_magnitude("TebiByte", base_magnitude=Byte, base=BINARY, order=40)
PiB = PebiByte = Magnitude.create_magnitude("PebiByte", base_magnitude=Byte, base=BINARY, order=50)

Kb = Kilobit = Magnitude.create_magnitude("Kilobit", base_magnitude=bit, base=DECIMAL, order=3)
Mb = Megabit = Magnitude.create_magnitude("Megabit", base_magnitude=bit, base=DECIMAL, order=4)
Gb = Gigabit = Magnitude.create_magnitude("Gigabit", base_magnitude=bit, base=DECIMAL, order=5)
Tb = Terabit = Magnitude.create_magnitude("Terabit", base_magnitude=bit, base=DECIMAL, order=6)
Pb = Petabit = Magnitude.create_magnitude("Petabit", base_magnitude=bit, base=DECIMAL, order=7)

KB = KiloByte = Magnitude.create_magnitude("KiloByte", base_magnitude=Byte, base=DECIMAL, order=3)
MB = MegaByte = Magnitude.create_magnitude("MegaByte", base_magnitude=Byte, base=DECIMAL, order=4)
GB = GigaByte = Magnitude.create_magnitude("GigaByte", base_magnitude=Byte, base=DECIMAL, order=5)
TB = TeraByte = Magnitude.create_magnitude("TeraByte", base_magnitude=Byte, base=DECIMAL, order=6)
PB = PetaByte = Magnitude.create_magnitude("PetaByte", base_magnitude=Byte, base=DECIMAL, order=7)

if __name__ == "__main__":
    assert Byte.get_minor_unit_class() is bit
    assert KB.get_minor_unit_class() is bit

    assert Byte.from_minor_units(16) == Byte(2)
    assert bit(16).convert_to(Byte) == Byte(2)

    # Comparisons between different unit sizes
    assert bit(1024) > Byte(3)
    assert bit(1024) > bit(1)
    assert Byte(1024) > Byte(1)

    # Comparisons between magnitudes
    # bytes to bit
    assert B() == bit(8)
    assert KiB() == 8 * Kib()

    # bit to bit
    assert 1 * Kib() == 1024 * bit()
    assert 1 * Kib() == 1024 * bit()

    # byte to byte
    assert 1 * KiB() == 1024 * B()
    assert 1 * MiB() == 1024 * KiB()
    assert 1 * GiB() == 1024 * MiB()
    assert 1 * TiB() == 1024 * GiB()

    # kilo
    assert Kb() == 1000 * b()
    assert KB() == 8000 * b()

    # kibi vs kilo
    assert 1000 * Kib() == 1024 * Kb()

    assert GiB(1).convert_to(Byte).value == 2**30
    assert GiB(1).to_minor_units().value == 2**30 * 8
