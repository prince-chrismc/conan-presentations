from conan import ConanFile

class Engine(ConanFile):
    name = "engine"
    version = "0.1"

    requires = "math/[>=1.0 <2.0]"
