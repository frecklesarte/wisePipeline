cmake_minimum_required(VERSION 3.10)
project('CGI-ProductionStructure')
set(STANDARD 17)

set(APP_SOURCE "${PROJECT_SOURCE_DIR}/source/app")
set(MODULE_SOURCE "${PROJECT_SOURCE_DIR}/source/module")
set(LIBRARIES_SOURCE "${PROJECT_SOURCE_DIR}/libs")
set(SITE_PACKAGES_SOURCE "${PROJECT_SOURCE_DIR}/cgi-venv/lib/python3.13/site-packages")

set(PYBIND11_FINDPYTHON OFF)
find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(main "${PROJECT_SOURCE_DIR}/source/cgi_production_tool/main.cpp")
install(TARGETS main DESTINATION .)
