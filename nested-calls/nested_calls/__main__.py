from brewtils import Plugin, SystemClient, command

__version__ = "3.0.0.dev0"


class NestedCallClient:
    """A client that calls nested commands as System Clients"""

    def __init__(self):
        self.nestedCallsClient = SystemClient(system_name="nested-calls")

    @command(description="Start Commands at Level One")
    def level_1(self):
        """Starts Commands at Level One"""

        return self.nestedCallsClient.level_2().output

    @command(description="Start Commands at Level Two")
    def level_2(self):
        """Starts Commands at Level Two"""

        return self.nestedCallsClient.level_3().output

    @command(description="Start Commands at Level Three")
    def level_3(self):
        """Starts Commands at Level Three"""

        return self.nestedCallsClient.level_4().output

    @command(description="Start Commands at Level Four")
    def level_4(self):
        """Starts Commands at Level Four"""

        return self.nestedCallsClient.level_5().output

    @command(description="Start Commands at Level Five")
    def level_5(self):
        """Starts Commands at Level Five"""

        return "Success"

    @command(description="Start JSON Commands at Level One", output_type="JSON")
	def level_1_json(self):
        """Starts JSON Commands at Level One"""

		return self.nestedCallsClient.level_2_json().output
		
	@command(description="Start JSON Commands at Level Two", output_type="JSON")
	def level_2_json(self):
        """Starts JSON Commands at Level Two"""

		return self.nestedCallsClient.level_3_json().output
		
	@command(description="Start JSON Commands at Level Three", output_type="JSON")
	def level_3_json(self):
        """Starts JSON Commands at Level Three"""

		return self.nestedCallsClient.level_4_json().output
		
	@command(description="Start JSON Commands at Level Four", output_type="JSON")
	def level_4_json(self):
        """Starts JSON Commands at Level Four"""

		return self.nestedCallsClient.level_5_json().output
		
	@command(description="Start JSON Commands at Level Five", output_type="JSON")
	def level_5_json(self):
        """Starts JSON Commands at Level Five"""

		return [1,2,3,4,5]
		


def main():
    plugin = Plugin(
        name="nested-calls",
        version=__version__,
        description="A plugin that calls commands on itself",
    )
    plugin.client = NestedCallClient()
    plugin.run()


if __name__ == "__main__":
    main()
