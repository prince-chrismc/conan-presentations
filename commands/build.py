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


try:
    shutil.rmtree("..\..\..\.conan2\extensions\commands\jfrog")
except:
    pass
os.makedirs("..\..\..\.conan2\extensions\commands\jfrog")
run("cp cmd_hello.py ..\..\..\.conan2\extensions\commands\jfrog")
run("conan -h")
run("conan jfrog:hello")
run("conan jfrog:hello --format=json")

run("cp cmd_multi_export.py ..\..\..\.conan2\extensions\commands\jfrog")
run("conan -h")
run("conan jfrog:multi-export repo --format=json")

