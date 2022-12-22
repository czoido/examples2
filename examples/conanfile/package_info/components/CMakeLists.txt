cmake_minimum_required(VERSION 3.15)
project(game-engine CXX)

add_library(game-engine src/game-engine.cpp)
target_include_directories(game-engine PUBLIC include)

set_target_properties(game-engine PROPERTIES PUBLIC_HEADER "include/game-engine.h")
install(TARGETS game-engine)
