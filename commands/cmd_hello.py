import json

from conan.api.conan_api import ConanAPIV2
from conan.api.output import ConanOutput
from conan.cli.command import conan_command

def output_json(msg):
    return json.dumps({"greet": msg})


@conan_command(group="My own commands", formatters={"json": output_json})
def hello(conan_api: ConanAPIV2, parser, *args):
    """
    Simple command to print "Hello World!" line
    """
    msg = "Hello World!"
    ConanOutput().info(msg)
    return msg