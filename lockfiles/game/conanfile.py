from conan import ConanFile

class Game(ConanFile):
    name = "game"
    version = "1.0"

    requires = "engine/[>=1.0 <2.0]"
