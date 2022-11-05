import os


def sign(ref, artifacts_folder, signature_folder):
    print("Signing ref: ", ref)
    print("Signing folder: ", artifacts_folder)
    files = []
    for f in sorted(os.listdir(artifacts_folder)):
        if os.path.isfile(os.path.join(artifacts_folder, f)):
            files.append(f)
    signature = os.path.join(signature_folder, "signature.asc")
    open(signature, "w").write("\n".join(files))


def verify(ref, artifacts_folder, signature_folder):
    print("Verifying ref: ", ref)
    print("Verifying folder: ", artifacts_folder)
    signature = os.path.join(signature_folder, "signature.asc")
    contents = open(signature).read()
    print("verifying contents", contents)
    for f in sorted(os.listdir(artifacts_folder)):
        print("VERIFYING ", f)
        if os.path.isfile(os.path.join(artifacts_folder, f)):
            assert f in contents
