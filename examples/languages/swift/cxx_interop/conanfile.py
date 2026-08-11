import os
from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.files import save


class SwiftCppDemo(ConanFile):
    settings = "os", "arch", "compiler", "build_type"

    def layout(self):
        cmake_layout(self)

    def requirements(self):
        self.requires("lunasvg/3.5.0")

    def _write_modulemap(self, filename, module_name, header_path):
        content = f'module {module_name} {{\n    header "{header_path}"\n    export *\n}}\n'
        save(self, os.path.join(self.generators_folder, "shim", filename), content)

    def generate(self):
        CMakeDeps(self).generate()
        CMakeToolchain(self).generate()

        # lunasvg has no Swift module map; write a shim one from its cpp_info.
        lunasvg_include = self.dependencies["lunasvg"].cpp_info.includedirs[0]
        self._write_modulemap("lunasvg.modulemap", "LunaSVGMod", f"{lunasvg_include}/lunasvg/lunasvg.h")
