# pd-code-strong-sanity

Validate that a PD code can be realized by the diagram-layout backend.

## Installation

```bash
pip install pd-code-strong-sanity
```

## Quick start

`from pd_code_strong_sanity import sanity`; the function returns a boolean.

PD codes are lists of four-entry crossings. Each arc label must occur exactly twice. Functions validate their inputs and do not mutate caller-owned PD-code lists unless explicitly documented.

## Development

Use Python 3.10 or newer for Python packages. Build distributions with `poetry build`. Run the package's tests or examples before publishing. C++ projects require a modern standards-compliant compiler.

## License

MIT. See `LICENSE`.
