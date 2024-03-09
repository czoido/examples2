from conan import ConanFile
from conan.tools.cmake import cmake_layout

class CompressorRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def requirements(self):
        self.requires("zlib/1.2.11")
    
    def build_requirements(self):
        self.tool_requires("arm-toolchain/13")

    def layout(self):
        cmake_layout(self)
