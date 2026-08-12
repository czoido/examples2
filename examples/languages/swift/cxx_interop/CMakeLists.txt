cmake_minimum_required(VERSION 3.23)
project(swift_cpp_demo LANGUAGES CXX Swift)

find_package(lunasvg REQUIRED)

add_executable(demo main.swift)

target_link_libraries(demo PRIVATE
  lunasvg::lunasvg
)

target_compile_options(demo PRIVATE
  "$<$<COMPILE_LANGUAGE:Swift>:-cxx-interoperability-mode=default>"
  "$<$<COMPILE_LANGUAGE:Swift>:SHELL:-Xcc -std=c++${CMAKE_CXX_STANDARD}>"
  "$<$<COMPILE_LANGUAGE:Swift>:SHELL:-Xcc -fmodule-map-file=${LUNASVG_MODULEMAP}>"
)
