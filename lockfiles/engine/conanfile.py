from conan import ConanFile

class Engine(ConanFile):
    name = "engine"

    requires = "math/[>=1.0 <2.0]"
