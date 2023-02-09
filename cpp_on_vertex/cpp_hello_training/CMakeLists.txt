cmake_minimum_required(VERSION 3.20)

# Define the project name and where to report bugs.
set(PACKAGE_BUGREPORT
    "https://github.com/GoogleCloudPlatform/cpp-samples/issues")
project(<enter your project id here>)

add_executable(hello hello.cc)
target_compile_features(hello PRIVATE cxx_std_17)
target_link_libraries(hello functions-framework-cpp::framework)

include(GNUInstallDirs)
install(TARGETS hello RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR})