# Swift / C++ interop with Conan-managed dependencies

A Swift app that consumes a plain, Swift-unaware ConanCenter package --
[lunasvg](https://conan.io/center/recipes/lunasvg) -- directly, via
[Swift's C++ interoperability mode](https://www.swift.org/documentation/cxx-interop/).
Swift builds an SVG scene as a string, hands it to lunasvg's C++ `Document`
and `Bitmap` classes to parse and rasterize, and writes the result to a PNG
file -- no C wrapper library needed.

Since lunasvg ships no Swift module map, `conanfile.py`'s `generate()` writes
a small [Clang module map](https://clang.llvm.org/docs/Modules.html) pointing
at its real installed header (read from `cpp_info`), and `CMakeLists.txt`
passes that to `swiftc` via `-Xcc -fmodule-map-file=...` together with
`-cxx-interoperability-mode=default`.

## Requirements

- macOS with Xcode command line tools (`swiftc`), Swift 5.9+.
- CMake >= 3.23, with the Ninja generator.

## Build and run

```bash
git clone https://github.com/conan-io/examples2.git
cd examples2/examples/languages/swift/cxx_interop

conan install . --build=missing -c tools.cmake.cmaketoolchain:generator=Ninja
cmake --preset conan-release
cmake --build --preset conan-release
./build/Release/demo
```

The program renders the SVG and writes `summer.png` to the working directory.
