# octet

Object-oriented way to represent digital sizes (bits and bytes)

## Examples

```python
>>> from octet import *
>>> GiB(1024).convert_to(TiB)
TebiByte(1)
>>> size = 1024 * KiB()
>>> size.to_minor_units()
bit(8388608)
>>> KiB(1) > 1000 * B()
True
>>> KiB(1) > 1025 * B()
False
```
