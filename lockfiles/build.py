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
run("conan install engine")
run("conan create math --version=1.1")
run("conan install engine")
run("conan install engine --lockfile-out=conan.lock")
print(load("conan.lock"))
run("conan create math --version=1.2")
run("conan install engine --lockfile=conan.lock")

# incremental, partial lockfile?
# multi-configuration lockfile?
