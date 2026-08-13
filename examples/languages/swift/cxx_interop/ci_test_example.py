import platform

from test.examples_tools import run

print("Swift C++ interop: consuming a plain ConanCenter package from Swift")


if platform.system() != "Darwin":
    print("WARNING: Skipping Swift interop example, requires macOS with swiftc")
else:
    run("conan install . -s build_type=Release --build=missing")
    run("xcodebuild -project demo.xcodeproj -scheme demo -configuration Release "
        "-derivedDataPath build build")
    run("./build/Build/Products/Release/demo")
