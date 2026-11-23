#include <pybind11/embed.h>

namespace py = pybind11;

int
main() {
    py::scoped_interpreter gaurd{};  // start the Interpreter and keep it alive

    py::print("Hello, PyBind!");  // use the Python API
}
