cmake_minimum_required(VERSION 3.8)
project(octomap)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(moveit_task_constructor_core REQUIRED)
find_package(PythonInterp REQUIRED)

# Python Executables
ament_python_install_package(${PROJECT_NAME})

install(PROGRAMS
    src/octoload.py
    DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY launch config map DESTINATION share/${PROJECT_NAME})

ament_package()

