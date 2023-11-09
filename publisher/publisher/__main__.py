import logging

from brewtils import PublishClient, Plugin, command

__version__ = "3.0.0.dev0"

class Publisher:

    def __init__(self):
        self.publishClient = PublishClient()

    @command()
    def publish_topics(self, value:str = "value", topic:str = "topic1") -> str:
        self.publishClient.publish(_topic=topic, value = value)
        return value

def main():
    plugin = Plugin(
        name="publisher",
        version=__version__,
        description="A plugin that publishes to topics",
        max_concurrent=1,
    )
    plugin.client = Publisher()
    plugin.run()


if __name__ == "__main__":
    main()
