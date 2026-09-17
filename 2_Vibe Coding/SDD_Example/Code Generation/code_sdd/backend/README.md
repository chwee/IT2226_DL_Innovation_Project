# Backend — Web Translator

## Setup

`googletrans==4.0.0-rc1` pins `httpx==0.13.3`, which imports the stdlib `cgi`
module. `cgi` was removed in Python 3.13 (PEP 594), so this project requires
**Python 3.12 or earlier**.

```bash
py -3.12 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -c "import googletrans; print(googletrans.__version__)"
```

If `import googletrans` fails with a version-mismatch error (e.g. an
`httpx`/`h11`/`h2` conflict pulled in from an already-populated environment),
force a clean resolve of its pinned dependency tree:

```bash
pip uninstall googletrans httpx httpcore h11 h2 -y
pip install googletrans==4.0.0-rc1
```

For running tests, also install dev dependencies:

```bash
pip install -r requirements-dev.txt
```
