#include <filesystem>
#include <pybind11/embed.h>

namespace py = pybind11;
namespace fs = std::filesystem;

int main() {

    py::scoped_interpreter interpreter{};  // start the Interpreter and keep it alive

    const fs::path ui_dir = fs::path(__FILE__).parent_path() / "ui";

    // add main_window.py to python import path
    py::module_::import("sys").attr("path").attr("insert")(0, ui_dir.string());

    py::print("Hello, PyBind!");  // use the Python API

    return py::module_::import("main_window").attr("run")().cast<int>();
}
