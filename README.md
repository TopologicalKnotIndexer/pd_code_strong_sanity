# pd-code-strong-sanity

Check whether a structurally valid PD code can be realized by the diagram-layout engine.

## Installation

```bash
pip install pd-code-strong-sanity
```

## Usage example

```python
from pd_code_strong_sanity import sanity

pd = [[1, 5, 2, 4], [3, 1, 4, 6], [5, 3, 6, 2]]
print(sanity(pd))
```

## Algorithm

Strong sanity delegates to the layout engine and returns `True` only when it can construct a routed planar matrix without inconsistent sockets or crossings. It catches layout failures and exposes a simple boolean API. This is intentionally more expensive than structural sanity and should be used when geometric realizability is required.

## Input conventions

A PD code is represented as a list of four-entry crossings. Arc labels normally occur exactly twice. Public functions validate inputs and return new values rather than mutating caller-owned data unless their API explicitly says otherwise.

## External software

- A C++17 compiler is required the first time the bundled layout engine is built.
- No display server or GUI is required.

## Development

Run examples and package checks before release. Python packages require Python 3.10 or newer. Build PyPI artifacts with:

```bash
poetry check
poetry build
```

## License

MIT. See `LICENSE`.
