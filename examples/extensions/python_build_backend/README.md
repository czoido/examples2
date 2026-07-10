# Python extension built with conan-py-build

A minimal example of a Python package with a C++ extension (built with
**pybind11** and **fmt**) where all the C++ dependencies are managed by
Conan through [`conan-py-build`](https://github.com/conan-io/conan-py-build),
a PEP 517 build backend.

- Conan blog post: https://blog.conan.io/cpp/conan/python/2026/05/05/Introducing-conan-py-build.html
- `conan-py-build` documentation: https://conan-py-build.conan.io

## How it works

- `pyproject.toml` declares `conan-py-build` as the build backend.
- `conanfile.py` is a regular Conan recipe declaring `pybind11` and `fmt`
  as requirements, and building the extension with CMake using the same
  Python interpreter as `pip`.
- `CMakeLists.txt` builds the `_core` extension module and installs it
  into a `myadder` directory, matching the Python package name so the
  compiled module ends up next to `__init__.py` in the resulting wheel.
- `python/myadder/__init__.py` re-exports the `add()` function from the
  compiled `_core` module.

## Build and test

```bash
git clone https://github.com/conan-io/examples2.git
cd examples2/examples/extensions/python_build_backend

pip wheel . -w dist/

pip install dist/myadder-*.whl
python -c "from myadder import add; add(2, 3)"
```

This prints `2 + 3 = 5` in bold green (via `fmt`'s color support) and returns `5.0`.
