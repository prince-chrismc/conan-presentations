import os, shutil
from contextlib import contextmanager


def run(cmd, error=False):
    ret = os.system(cmd)
    if not error and ret != 0:
        raise Exception("Cmd failed", cmd)
    if error and ret == 0:
        raise Exception("Cmd not failed (but expected)", cmd)


def load(path):
    return open(path, "r").read()

@contextmanager
def chdir(d):
    cwd = os.getcwd()
    os.chdir(d)
    yield
    os.chdir(cwd)


# Preparation
run("conan remove math/1.0.1* -f")
run("conan remove game* -f")
run("conan create math --version=1.0 --build=missing")
run("conan create engine --build=missing")
run("conan create engine -o engine*:shared=True --build=missing")


###### GRAPH  #######################################################
run("conan install game -o engine*:shared=True")
# Show here that no math find is necessary
run("conan install game")
# Now show that math is there, but only the library, not the headers


###### PACKAGE-ID #######################################################
# do a change in math, bump patch
run("conan create math --version=1.0.1")
run("conan graph build-order --requires=game/1.0 -o engine*:shared=True --build=missing")
run("conan graph build-order --requires=game/1.0 --build=missing")
run("conan create game -o engine*:shared=True --build=missing")


###### DEPLOY #######################################################
with chdir("game"):
    run("conan install . --deploy=full_deploy")
    run("conan install . --deploy=full_deploy  -g CMakeDeps")

# Custom one:
run("conan install --requires=game/1.0 -o engine*:shared=True --deploy=runtime_zip_deploy")


raise

with chdir("lockfiles"):
    # partial lockfile to create a new lockfile
    run("conan install game")
    run("conan create math --version=1.1")
    run("conan install game")
    # oppss
    run("conan install game --lockfile-out=game.lock")
    print(load("game.lock"))

    run("conan create math --version=1.2")
    run("conan install game --lockfile=game.lock")  # All good, still 1.1

    # create a new version of engine, modifying lockfile
    run("conan create engine --version=1.1 --lockfile=game.lock --lockfile-out=new_engine.lock")
    print(load("new_engine.lock"))
    run("conan install game --lockfile=new_engine.lock")

with chdir("commands"):
    run("conan config install config")

    run("conan -h")
    run("conan jfrog:hello")
    run("conan jfrog:hello --format=json")
    run("conan jfrog:multi-export repo --format=json")