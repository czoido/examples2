import glob
import os
import shutil

from test.examples_tools import run

# ############# Example ################
print("Build a Python C++ extension (pybind11 + fmt) with conan-py-build")

run("pip wheel . -w dist/ -v")

wheels = glob.glob(os.path.join("dist", "myadder-*.whl"))
assert wheels, "No wheel was generated"

run(f"pip install --force-reinstall {wheels[0]}")

output = run('python -c "from myadder import add; add(2, 3)"')
assert "2 + 3 = 5" in output

run("pip uninstall myadder -y")

shutil.rmtree("dist", ignore_errors=True)
shutil.rmtree("build", ignore_errors=True)
