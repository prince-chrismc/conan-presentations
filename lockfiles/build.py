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


# basic usage of a lockfile
run("conan remove * -f")
run("conan create math --version=1.0")
run("conan create engine --version=1.0")

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
