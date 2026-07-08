#include <pybind11/pybind11.h>
#include <fmt/core.h>
#include <fmt/color.h>

namespace py = pybind11;

double add(double a, double b) {
    double result = a + b;
    fmt::print(fg(fmt::color::green) | fmt::emphasis::bold,
               "{} + {} = {}\n", a, b, result);
    return result;
}

PYBIND11_MODULE(_core, m) {
    m.doc() = "Simple Python extension using fmt via Conan.";
    m.def("add", &add, "Add two numbers and print the result formatted with fmt.",
          py::arg("a"), py::arg("b"));
}
