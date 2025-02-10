cmake_minimum_required(VERSION 3.0.2)
project(pruebas)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
#find_package(catkin REQUIRED)

find_package(catkin REQUIRED COMPONENTS roscpp)
find_package(catkin REQUIRED COMPONENTS roscpp geometry_msgs)

#Declare our catkin package

catkin_package()

#Specify locations of header files
include_directories(include ${catkin_INCLUDE_DIRS})

# Declare the executable, along with its source files.If
# there are multiple executables, use multiple copies of
# this line .

add_executable(hello hello.cpp)
add_executable(pubvel pubvel.cpp)
add_executable(subpose subpose.cpp)

#Specify libraries against which to link. Again, this line should be copied for eachcdistinct executable in the package

target_link_libraries(hello ${catkin_LIBRARIES})
target_link_libraries(pubvel ${catkin_LIBRARIES})
target_link_libraries(subpose ${catkin_LIBRARIES})
