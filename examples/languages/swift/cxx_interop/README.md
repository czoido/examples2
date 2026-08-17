# Swift / C++ interop with Conan-managed dependencies

A Swift app that consumes a plain, Swift-unaware ConanCenter package --
[lunasvg](https://conan.io/center/recipes/lunasvg) -- directly, via
[Swift's C++ interoperability mode](https://www.swift.org/documentation/cxx-interop/).
Swift builds an SVG scene as a string, hands it to lunasvg's C++ `Document`
and `Bitmap` classes to parse and rasterize, and writes the result to a PNG
file -- no C wrapper library needed.

Since lunasvg ships no Swift module map, `conanfile.py`'s `generate()` writes
a small [Clang module map](https://clang.llvm.org/docs/Modules.html) pointing
at its real installed header (read from `cpp_info`), and sets `OTHER_SWIFT_FLAGS`
through `XcodeToolchain.build_settings` to pass that to `swiftc` via
`-Xcc -fmodule-map-file=...` together with `-cxx-interoperability-mode=default`.
`demo.xcodeproj` is a plain Xcode project whose Release configuration is based
on the `.xcconfig` files that Conan's `XcodeDeps`/`XcodeToolchain` generators
write.

## Requirements

- macOS with Xcode (`swiftc`, `xcodebuild`), Swift 5.9+.
- Conan 2.32 or newer (`XcodeToolchain.build_settings`).

## Build and run

```bash
git clone https://github.com/conan-io/examples2.git
cd examples2/examples/languages/swift/cxx_interop

conan install . -s build_type=Release --build=missing
open demo.xcodeproj
```

From there it is a normal Xcode project: press Run, and Swift calls into
lunasvg. The same build also works from the command line:

```bash
xcodebuild -project demo.xcodeproj -scheme demo -configuration Release \
    -derivedDataPath build build
./build/Build/Products/Release/demo
```

The program renders the SVG and writes `summer.png` to the working directory.
