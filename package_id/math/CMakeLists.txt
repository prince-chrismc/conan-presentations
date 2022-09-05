cmake_minimum_required(VERSION 3.15)
project(math CXX)

add_library(mymath src/mymath.cpp)
target_include_directories(mymath PUBLIC include)

set_target_properties(mymath PROPERTIES PUBLIC_HEADER "include/mymath.h")
install(TARGETS mymath)
