enable_testing ()

add_executable (testcase testcase.cpp)
target_link_libraries (testcase docopt_cpp)
add_test (python_tests
	testcase
	)
