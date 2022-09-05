cmake_minimum_required(VERSION 3.15)
project(engine CXX)

find_package(math CONFIG REQUIRED)

add_library(engine src/engine.cpp)
target_include_directories(engine PUBLIC include)

target_link_libraries(engine PUBLIC math::math)

set_target_properties(engine PROPERTIES PUBLIC_HEADER "include/engine.h")
install(TARGETS engine)
