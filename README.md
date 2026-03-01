# pd_code_strong_sanity
Check if a pd_code represents a valid knot/link (with mandatory guarantee of an existing planar layout scheme)

## Install

```bash
pip install pd-code-strong-sanity
```

## Usage

```python
import pd_code_strong_sanity

pd_code = [
    [1, 2, 1, 2]
]
print(pd_code_strong_sanity.sanity(pd_code)) # False
```
