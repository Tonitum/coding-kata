add_library(
  solution
  ${CMAKE_CURRENT_LIST_DIR}/solution345.cpp
)

include("${CMAKE_CURRENT_LIST_DIR}/test/CMakeLists.txt")
