import os
import json

from conan.api.conan_api import ConanAPIV2
from conan.api.output import ConanOutput
from conan.cli.command import conan_command

def output_json(exported):
    return json.dumps({"exported": [repr(r) for r in exported]})


@conan_command(group="My own commands", formatters={"json": output_json})
def multi_export(conan_api: ConanAPIV2, parser, *args):
    """
    Exporting several recipes
    """
    parser.add_argument('path')
    args = parser.parse_args(*args)
    result = []
    for f in os.listdir(args.path):
        f = os.path.join(args.path, f)
        print("Checking", f)
        if os.path.isdir(f):
            conanfile = os.path.join(f, "conanfile.py")
            if os.path.isfile(conanfile):
                print("Exporting", f)
                ref = conan_api.export.export(os.path.abspath(conanfile), None, None, None, None)
                result.append(ref)
    return result