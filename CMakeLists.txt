cmake_minimum_required (VERSION 2.8 FATAL_ERROR)
set(CMAKE_MACOSX_RPATH ON) # see CMP0042

project (docopt_cpp)
set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall")

option (DOCOPT_CPP_ENABLE_TEST "Run tests for docopt.cpp." OFF)

set (DOCOPT_CPP_INCLUDES
	include/docopt.h
	include/docopt_private.h
	include/docopt_util.h
	include/docopt_value.h)
set (DOCOPT_CPP_SOURCES
	src/docopt.cpp)

add_library (docopt_cpp_lib SHARED ${DOCOPT_CPP_INCLUDES} ${DOCOPT_CPP_SOURCES})

install (FILES ${DOCOPT_CPP_INCLUDES}
	DESTINATION include/docopt_cpp)
install (TARGETS docopt_cpp_lib
	LIBRARY DESTINATION lib/docopt_cpp
	ARCHIVE DESTINATION lib/docopt_cpp
	RUNTIME DESTINATION bin/docopt_cpp)

if (DOCOPT_CPP_ENABLE_TEST)
	add_subdirectory (tests)
endif (DOCOPT_CPP_ENABLE_TEST)
