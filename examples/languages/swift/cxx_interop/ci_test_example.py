import platform
import re
import subprocess

from test.examples_tools import run

# ############# Example ################
print("Swift <-> C++ interop: consuming a plain ConanCenter package from Swift")


def _cmake_supports_swift(minimum=(3, 28)):
    try:
        output = subprocess.run(["cmake", "--version"], capture_output=True, text=True, check=True).stdout
    except FileNotFoundError:
        return False
    match = re.search(r"(\d+)\.(\d+)\.(\d+)", output)
    return bool(match) and tuple(int(x) for x in match.groups()[:2]) >= minimum


if platform.system() != "Darwin" or not _cmake_supports_swift():
    print("WARNING: Skipping Swift interop example, requires macOS with swiftc and CMake >= 3.28")
else:
    run("conan install . --build=missing -c tools.cmake.cmaketoolchain:generator=Ninja")
    run("cmake --preset conan-release")
    run("cmake --build --preset conan-release")
    # No window/event loop involved, so the binary can run headlessly in CI.
    run("./build/Release/demo")
