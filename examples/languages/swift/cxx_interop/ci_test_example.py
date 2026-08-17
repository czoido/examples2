import platform

from conan.tools.scm import Version

from test.examples_tools import run

print("Swift C++ interop: consuming a plain ConanCenter package from Swift")

conan_version = run("conan --version").split()[-1]

if platform.system() != "Darwin" or Version(conan_version).main < Version("2.32").main:
    print("WARNING: Skipping Swift interop example, requires macOS with swiftc and Conan >= 2.32")
else:
    run("conan install . -s build_type=Release --build=missing")
    run("xcodebuild -project demo.xcodeproj -scheme demo -configuration Release "
        "-derivedDataPath build build")
    run("./build/Build/Products/Release/demo")
