import platform

from test.examples_tools import run

print("Swift C++ interop: consuming a plain ConanCenter package from Swift")


if platform.system() != "Darwin":
    print("WARNING: Skipping Swift interop example, requires macOS with swiftc")
else:
    run("conan install . --build=missing -c tools.cmake.cmaketoolchain:generator=Ninja")
    run("cmake --preset conan-release")
    run("cmake --build --preset conan-release")
    run("./build/Release/demo")
