enable_testing ()

find_package (PythonInterp REQUIRED)

add_executable (testcase testcase.cpp)
target_link_libraries (testcase docopt_cpp)
file (COPY ${CMAKE_CURRENT_SOURCE_DIR}/testcases.docopt DESTINATION ${CMAKE_CURRENT_BINARY_DIR})
file (COPY ${CMAKE_CURRENT_SOURCE_DIR}/run_tests.py DESTINATION ${CMAKE_CURRENT_BINARY_DIR})
add_test (python_tests ${PYTHON_EXECUTABLE} "${CMAKE_CURRENT_SOURCE_DIR}/run_tests.py")
