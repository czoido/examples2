import os
import textwrap
from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.files import save


class SwiftCppDemo(ConanFile):
    settings = "os", "arch", "compiler", "build_type"

    def layout(self):
        cmake_layout(self)

    def requirements(self):
        self.requires("lunasvg/3.5.0")

    def generate(self):
        CMakeDeps(self).generate()

        # lunasvg has no Swift module map; write a shim one from its cpp_info.
        include_dir = self.dependencies["lunasvg"].cpp_info.includedir
        header = f"{include_dir}/lunasvg/lunasvg.h"

        modulemap_path = os.path.join(self.generators_folder, "lunasvg.modulemap")
        modulemap = textwrap.dedent(f'''\
            module LunaSVGMod {{
                header "{header}"
                export *
            }}
            ''')
        save(self, modulemap_path, modulemap)

        tc = CMakeToolchain(self)
        tc.variables["LUNASVG_MODULEMAP"] = modulemap_path
        tc.generate()
