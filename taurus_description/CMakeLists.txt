cmake_minimum_required(VERSION 3.8)
project(taurus_description)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(urdf REQUIRED)


# Install
################################################################################
install(DIRECTORY meshes urdf launch worlds
  DESTINATION share/${PROJECT_NAME}
)

################################################################################
# Macro for ament package
#if(BUILD_TESTING)
#  find_package(ament_lint_auto REQUIRED)
#  set(ament_cmake_copyright_FOUND TRUE)
#  set(ament_cmake_cpplint_FOUND TRUE)
#  ament_lint_auto_find_test_dependencies()
#endif()
################################################################################
ament_package()
