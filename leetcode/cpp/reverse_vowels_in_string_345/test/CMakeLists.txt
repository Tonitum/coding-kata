enable_testing()
add_executable(
  solution_test_345
  ${CMAKE_CURRENT_LIST_DIR}/test_solution_345.cpp
)

target_link_libraries(
  solution_test_345
  GTest::gtest_main
)

include(GoogleTest)
gtest_discover_tests(solution_test_345)

