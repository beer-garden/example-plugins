import logging

from brewtils import PublishClient, Plugin, command

__version__ = "3.0.0.dev0"

class Publisher:

    def __init__(self):
        self.publishClient = publishClient()

    @command()
    def publish_topics(self, payload:dict, topic:str = "topic1") -> dict:
        self.publishClient.publish(_topic=topic, payload = payload)
        return dict

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
