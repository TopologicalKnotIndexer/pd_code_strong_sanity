# pd-code-strong-sanity

Check whether a PD code is accepted and routed by the diagram-layout engine.

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

Strong sanity delegates to the layout engine and returns `True` only when it constructs a routed planar matrix without inconsistent sockets or crossings. It catches ordinary validation, build, and layout exceptions, but does not suppress process-control exceptions such as `KeyboardInterrupt` or `SystemExit`.

This is a conservative executable check, not a mathematical decision procedure for PD-code realizability. `False` can mean either invalid input or that the bounded heuristic router did not find a layout. Use `pd-code-sanity` when only weak structural validation is required, and call `pd-code-to-diagram` directly when failure details matter.

## Input conventions

A PD code is represented as a list of four-entry crossings. Arc labels normally occur exactly twice. Public functions validate inputs and return new values rather than mutating caller-owned data unless their API explicitly says otherwise.

## External software

- A C++17 compiler is required the first time the bundled layout engine is built.
- No display server or GUI is required.

## Development

Python 3.10 or newer is required. Run the unit tests with the declared
`pd-code-to-diagram` dependency available:

```bash
python -m unittest discover -s tests -v
```

No PyPI publication is performed as part of repository maintenance.

## License

MIT. See `LICENSE`.

## Citation

If you use this repository in academic work, please cite it as:

```bibtex
@software{topologicalknotindexer_pd_code_strong_sanity,
  author = {{TopologicalKnotIndexer contributors}},
  title = {{pd\_code\_strong\_sanity}},
  year = {2026},
  url = {https://github.com/TopologicalKnotIndexer/pd_code_strong_sanity}
}
```
