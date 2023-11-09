import logging

from brewtils import subscribe, Plugin

__version__ = "3.0.0.dev0"

class SubscribeClient:

    @subscribe(topics=["topic1","topic2"])
    def subscribe_multiple_topics(self, value:str) -> str:
        return value

    @subscribe(topics="topic1")
    def subscrib_one_topics(self, value:str) -> str:
        return value

    @subscribe(topics="topic.*")
    def subscribe_wildcard_topics(self, value:str) -> str:
        return value

def main():
    plugin = Plugin(
        name="subscribe",
        version=__version__,
        description="A plugin that subscribes to topics",
        max_concurrent=1,
    )
    plugin.client = SubscribeClient()
    plugin.run()


if __name__ == "__main__":
    main()
