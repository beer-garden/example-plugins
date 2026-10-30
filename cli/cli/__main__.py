import logging
import subprocess

from brewtils import Plugin, command, parameter, shutdown

__version__ = "3.0.0.dev0"
logger = logging.getLogger(__name__)


class CLIClient(object):
    """A plugin that executes OS commands against a sub process terminal"""

    subprocess_list = {}

    @parameter(
        key="subprocess_label",
        type="String",
        description="Session Label for running subprocess to be created",
    )
    def start_subprocess(self, subprocess_label: str):
        if subprocess_label in self.subprocess_list:
            raise Exception(f"Sub process already exists by label: {subprocess_label}")

        self.subprocess_list[subprocess_label] = subprocess.Popen(
            ["/bin/bash"],  # Use 'cmd.exe' on Windows
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        return f"{subprocess_label} subprocess created"

    @parameter(
        key="subprocess_label",
        type="String",
        description="Session Label for running subprocess to be shutdown",
        optional=False,
        choices={"type": "command", "value": "get_subprocess_list"},
    )
    def stop_subprocess(self, subprocess_label: str):
        if subprocess_label in self.subprocess_list:
            self.subprocess_list[subprocess_label].stdin.close()
            self.subprocess_list[subprocess_label].terminate()
            del self.subprocess_list[subprocess_label]
            return f"{subprocess_label} subprocess deleted"
        else:
            raise Exception(
                f"Unable to find targeted sub process by label {subprocess_label}"
            )

    @shutdown
    @command
    def shutdown_all_subprocesses(self):
        for label in self.get_subprocess_list():
            self.stop_subprocess(label)

        return "All Subprocesses Deleted"

    @command
    def get_subprocess_list(self):
        return list(self.subprocess_list.keys())

    @parameter(
        key="subprocess_label",
        type="String",
        description="Session Label for running subprocess command",
        optional=False,
        choices={"type": "command", "value": "get_subprocess_list"},
    )
    @parameter(
        key="cmd",
        type="String",
        description="The targeted command to execute within the subprocess",
    )
    def run_command(self, subprocess_label: str, cmd: str):

        # Send the command followed by a newline character

        if subprocess_label in self.subprocess_list:
            proc = self.subprocess_list[subprocess_label]
        else:
            raise Exception(
                f"Unable to find targeted sub process by label {subprocess_label}"
            )

        proc.stdin.write(cmd + "\n")
        proc.stdin.flush()

        # Simple delimiter trick to know when command output ends
        delimiter = "---CMD_DONE---"
        proc.stdin.write(f"echo {delimiter}\n")
        proc.stdin.flush()

        # Read the stream lines until the delimiter is encountered
        output = []
        while True:
            line = proc.stdout.readline()
            if delimiter in line or not line:
                break
            output.append(line)

        return "".join(output).strip()


def main():

    plugin = Plugin(
        name="CLI",
        version=__version__,
        description="A plugin that executes OS commands against a sub process terminal",
    )
    plugin.client = CLIClient()
    plugin.run()


if __name__ == "__main__":
    main()
