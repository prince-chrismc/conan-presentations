import os, shutil
import zipfile

# USE **KWARGS to be robust against changes
def deploy(conanfile, output_folder, **kwargs):
    files = []
    for r, d in conanfile.dependencies.items():
        # look for .dlls and .exes in the bin folder
        bindir = os.path.join(d.package_folder, "bin")
        for f in os.listdir(bindir):
            if f.endswith(".dll") or f.endswith(".exe"):
                dst = os.path.join(output_folder, f)
                shutil.copy2(os.path.join(bindir, f), dst)
                files.append(dst)

    with zipfile.ZipFile(os.path.join(output_folder, 'runtime.zip'), 'w') as myzip:
        for f in files:
            myzip.write(f, os.path.basename(f), compress_type=zipfile.ZIP_DEFLATED)
            os.remove(f)
