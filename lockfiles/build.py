import os, shutil
from contextlib import contextmanager


def run(cmd, error=False):
    ret = os.system(cmd)
    if not error and ret != 0:
        raise Exception("Cmd failed", cmd)
    if error and ret == 0:
        raise Exception("Cmd not failed (but expected)", cmd)


@contextmanager
def chdir(d):
    cwd = os.getcwd()
    os.chdir(d)
    yield
    os.chdir(cwd)


run("conan create math --version=1.0")
run("conan create engine")
