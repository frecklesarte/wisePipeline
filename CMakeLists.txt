cmake_minimum_required(VERSION 3.10)
project(wisePipeline LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(APP_SOURCE "${PROJECT_SOURCE_DIR}/source/app")
set(MODULE_SOURCE "${PROJECT_SOURCE_DIR}/source/module")
set(LIBRARIES_SOURCE "${PROJECT_SOURCE_DIR}/libs")
set(SITE_PACKAGES_SOURCE "${PROJECT_SOURCE_DIR}/wise-venv/lib/python3.13/site-packages")

set(Python_FIND_VIRTUALENV ONLY)
find_package(Python 3.13 REQUIRED COMPONENTS Interpreter Development.Embed)

set(PYBIND11_FINDPYTHON ON)
add_subdirectory("${PROJECT_SOURCE_DIR}/libs/pybind11")

add_executable(main "${PROJECT_SOURCE_DIR}/source/wisePipeline/main.cpp")
target_link_libraries(main PRIVATE pybind11::embed)
install(TARGETS main DESTINATION .)
