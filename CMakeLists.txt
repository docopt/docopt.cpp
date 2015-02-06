cmake_minimum_required (VERSION 2.8 FATAL_ERROR)

project (docoptcpp)

option (GRIZZLY_TEST "Testing for grizzly and all of its subpojects." OFF)

set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall")

include_directories (include)
add_library (docoptcpp src/main.cpp src/docopt.cpp)
