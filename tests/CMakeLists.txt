enable_testing ()

add_executable (testcase testcase.cpp )
add_test (NAME python_tests
	COMMAND python run_tests.py)
