import os, shutil

# USE **KWARGS to be robust against changes
def deploy(conanfile, output_folder, **kwargs):
    for r, d in conanfile.dependencies.host.items():
        # look for the bin folder
        bindir = os.path.join(d.package_folder, "bin")
        for f in os.listdir(bindir):
            if f.endswith(".dll") or f.endswith(".exe"):
                shutil.copy2(os.path.join(bindir, f), output_folder)
