import os
import textwrap
from conan import ConanFile
from conan.tools.apple import XcodeDeps, XcodeToolchain
from conan.tools.build import cppstd_flag
from conan.tools.files import save


class SwiftCppDemo(ConanFile):
    settings = "os", "arch", "compiler", "build_type"

    def layout(self):
        self.folders.generators = "generators"

    def requirements(self):
        self.requires("lunasvg/3.5.0")

    def generate(self):
        XcodeDeps(self).generate()

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

        cppstd = cppstd_flag(self)

        tc = XcodeToolchain(self)
        tc.build_settings["OTHER_SWIFT_FLAGS"] = (
            f'$(inherited) -cxx-interoperability-mode=default '
            f'-Xcc {cppstd} -Xcc -fmodule-map-file="{modulemap_path}"'
        )
        tc.generate()
