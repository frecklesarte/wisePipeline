#include <pybind11/embed.h>

namespace py = pybind11;

int
main() {
    py::scoped_interpreter gaurd{};  // start the Interpreter and keep it alive

    // add main_window.py to python import path
    py::module_::import("sys").attr("path").attr("insert(0, "ui/main_window.py")")

    return py::module_::import("main_window").attr("run")().cast<int>();
    py::print("Hello, PyBind!");  // use the Python API
}
