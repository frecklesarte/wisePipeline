cmake_minimum_required(VERSION 3.10)
project('CGI-ProductionStructure')
set(STANDARD 17)

set(APP_SOURCE "${PROJECT_SOURCE_DIR}/source/app")
set(MODULE_SOURCE "${PROJECT_SOURCE_DIR}/source/module")
set(LIBRARIES_SOURCE "${PROJECT_SOURCE_DIR}/libs")
set(SITE_PACKAGES_SOURCE "${PROJECT_SOURCE_DIR}/wise-venv/lib/python3.13/site-packages")

set(PYBIND11_FINDPYTHON ON)
add_subdirectory("${PROJECT_SOURCE_DIR}/libs/pybind11")

add_executable(main "${PROJECT_SOURCE_DIR}/source/wisePipeline/main.cpp")
target_link_libraries(main PRIVATE pybind11::pybind11 pybind11::embed)
install(TARGETS main DESTINATION .)
