# octet

Object-oriented way to represent digital sizes (bits and bytes)

## Installation
```bash
pip install octet
```

## Examples

```python
>>> from octet import *
>>> GiB(1024).convert_to(TiB)
TiB(1)
>>> size = 1024 * KiB()
>>> size.to_minor_units()
b(8388608)
>>> KiB(1) > 1000 * B()
True
>>> KiB(1) > 1025 * B()
False
```
