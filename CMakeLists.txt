cmake_minimum_required(VERSION 3.1)

option(WITH_TESTS           "Build tests."       OFF)
option(WITH_EXAMPLE         "Build example."     OFF)
option(WITH_STATIC          "Build static libs." ON)

project(docopt.cpp)
include_directories("${PROJECT_SOURCE_DIR}")

########################################################################
# Compiler properties

# C++ standard
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
if(NOT CMAKE_CXX_STANDARD)
	set(CMAKE_CXX_STANDARD 11)
endif()

# Suppression of "unknown pragma" warning on GCC
if(CMAKE_COMPILER_IS_GNUCXX)
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wno-unknown-pragmas")	# Code uses #pragma mark
endif()

########################################################################
# docopt

set(DOCOPT_SRC
		docopt.cpp
		docopt.h
		docopt_private.h
		docopt_util.h
		docopt_value.h
		)
if(WITH_STATIC)
	add_library(docopt_s STATIC ${DOCOPT_SRC})
	target_include_directories(docopt_s PUBLIC "${PROJECT_SOURCE_DIR}")
endif()
add_library(docopt SHARED ${DOCOPT_SRC})
target_include_directories(docopt PUBLIC "${PROJECT_SOURCE_DIR}")

########################################################################
# tests

if (WITH_EXAMPLE)
	add_executable(docopt_example examples/naval_fate.cpp)
	target_link_libraries(docopt_example docopt)
endif()

########################################################################
# example

if (WITH_TESTS)
	set(TESTPROG "${CMAKE_CURRENT_BINARY_DIR}/run_testcase")
	set(TESTCASES "${PROJECT_SOURCE_DIR}/testcases.docopt")
	add_executable(run_testcase run_testcase.cpp)
	target_link_libraries(run_testcase docopt)
	configure_file(
			"${PROJECT_SOURCE_DIR}/run_tests.py"
			"${CMAKE_CURRENT_BINARY_DIR}/run_tests"
			ESCAPE_QUOTES
	)
	add_test("Testcases docopt" ${TESTPROG})
endif()

########################################################################
# installation

INSTALL(TARGETS
		docopt
		DESTINATION lib)
if(WITH_STATIC)
	INSTALL(TARGETS
			docopt_s
			DESTINATION lib)
endif()
INSTALL(FILES
		docopt.h
		docopt_private.h
		docopt_util.h
		docopt_value.h
		DESTINATION include/docopt)
SET(CPACK_PACKAGE_NAME "docopt")
SET(CPACK_DEBIAN_PACKAGE_DEPENDS "")
SET(CPACK_RPM_PACKAGE_REQUIRES "")
SET(CPACK_PACKAGE_DESCRIPTION_SUMMARY "Beautiful command line interfaces")
SET(CPACK_PACKAGE_VENDOR "Jared Grubb")
SET(CPACK_PACKAGE_CONTACT ${CPACK_PACKAGE_VENDOR})
SET(CPACK_PACKAGE_DESCRIPTION_FILE "${PROJECT_SOURCE_DIR}/README.rst")
SET(CPACK_RESOURCE_FILE_LICENSE "${PROJECT_SOURCE_DIR}/LICENSE-MIT")
SET(CPACK_PACKAGE_VERSION_MAJOR 0)
SET(CPACK_PACKAGE_VERSION_MINOR 6)
SET(CPACK_PACKAGE_VERSION_PATCH 1)
SET(CPACK_DEBIAN_PACKAGE_SECTION "Development")
SET(CPACK_RPM_PACKAGE_GROUP "Development/Libraries")
SET(CPACK_RPM_PACKAGE_LICENSE "MIT")
SET(CPACK_STRIP_FILES TRUE)
INCLUDE(CPack)
