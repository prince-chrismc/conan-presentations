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


run("conan remove * -f")
run("conan create math --version=1.0 --build=missing")
run("conan create engine --build=missing")
run("conan create engine -o engine*:shared=True --build=missing")
run("conan create game -o engine*:shared=True --build=missing")
run("conan create game --build=missing")

# do a change in math, bump patch
run("conan create math --version=1.0.1 --build=missing")
run("conan graph build-order --requires=game/1.0 -o engine*:shared=True --build=missing")
run("conan graph build-order --requires=game/1.0 --build=missing")
