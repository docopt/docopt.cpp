cmake_minimum_required (VERSION 2.8 FATAL_ERROR)

project (docopt_cpp)
set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall")

option (DOCOPT_CPP_ENABLE_TEST "Run tests for docopt.cpp." OFF)

set (DOCOPT_CPP_INCLUDES
	include/docopt.h
	include/docopt_private.h
	include/docopt_util.h
	include/docopt_value.h)
add_library (docopt_cpp src/docopt.cpp ${DOCOPT_CPP_INCLUDES})

if (DOCOPT_CPP_ENABLE_TEST)
	add_subdirectory (tests)
endif (DOCOPT_CPP_ENABLE_TEST)
