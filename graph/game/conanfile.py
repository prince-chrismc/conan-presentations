from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout


class gameRecipe(ConanFile):
    name = "game"
    version = "1.0"
    package_type = "application"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    requires = "engine/1.0"
    generators = "CMakeDeps", "CMakeToolchain"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*"

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
