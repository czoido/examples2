import platform

from test.examples_tools import run

# ############# Example ################
print("Swift <-> C++ interop: consuming a plain ConanCenter package from Swift")


if platform.system() != "Darwin":
    print("WARNING: Skipping Swift interop example, requires macOS with swiftc")
else:
    run("conan install . --build=missing -c tools.cmake.cmaketoolchain:generator=Ninja")
    run("cmake --preset conan-release")
    run("cmake --build --preset conan-release")
    # No window/event loop involved, so the binary can run headlessly in CI.
    run("./build/Release/demo")
