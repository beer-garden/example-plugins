from brewtils import Plugin, SystemClient, command, parameter, system

__version__ = "1.0.0.dev0"


@system
class DeployClient(object):
    """Plugin that deploys other plugins"""

    @command
    def bytes_from_file(self):
        with open("./binary", "rb") as f:
            data = f.read()

        return SystemClient().bytes_command(the_bytes=data).output

    @command
    def bytes_literal(self):
        return SystemClient().bytes_command(the_bytes=b'im a byte').output

    @parameter(key="the_bytes", type="Bytes")
    def bytes_command(self, the_bytes):
        return the_bytes

    @command
    def echo_invoker(self):
        return SystemClient().echo(my_file="./text").output

    @parameter(
        key="my_file",
        type="Base64",
        description="Any file",
        optional=False,
    )
    def echo(self, my_file):
        """Echoes the contents of the given file."""
        try:
            return my_file.read().decode('utf-8')
        except UnicodeError:
            my_file.seek(0)
            return my_file.read()


def main():
    p = Plugin(name="deploy", version=__version__)
    p.client = DeployClient()
    p.run()


if __name__ == "__main__":
    main()
