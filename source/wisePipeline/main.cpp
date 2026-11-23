#include <libs/pybind11/include/pybind11/pybind11.h>

namespace py = pybind11;

int main() {
    py::scoped_interpreter gaurd{}; // start the Interpreter and keep it alive

    py::print("Hello, PyBind!"); // use the Python API
}
