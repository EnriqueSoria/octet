from octet import *

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
