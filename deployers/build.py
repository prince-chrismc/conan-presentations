import os
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
    run("conan remote remove conancenter")
    run("conan remote add conanv2 https://conanv2beta.jfrog.io/artifactory/api/conan/conan --index 0")
except:
    pass

try:
    run("conan profile detect")
except:
    pass

run("conan search * -r=conanv2")
run("conan install --requires=zlib/1.2.12 --tool-requires=cmake/3.19.8 --build=missing --deploy=full_deploy -of=full_deploy")
run("conanbuild.bat && cmake --version")