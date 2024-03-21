import logging

from brewtils import Plugin, command, get_easy_client, parameter
from brewtils.models import Topic as BrewtilsTopic
from brewtils.schema_parser import SchemaParser
import json

__version__ = "0.0.1.dev0"


class Topic:
    def __init__(self):
        self._logger = logging.getLogger("topic")
        self.client = get_easy_client()

    @command
    def create_topic(self, name: str):
        topic = BrewtilsTopic(name=name)
        return self.client.create_topic(topic)

    @command(output_type="JSON")
    def get_topics(self):
        topics = []
        for topic in self.client.get_topics():
            topic_dict = topic.__dict__
            topic_dict["subscribers"] = [s.__dict__ for s in topic.subscribers]
            topics.append(topic_dict)
        return topics

    @command(output_type="JSON", hidden=True)
    def get_topic_choices(self):
        return [{"text": t["name"], "value": t["id"]} for t in self.get_topics()]

    @command(output_type="JSON", hidden=True)
    def get_subscriber_choices(self, topic_id):
        return [
            {
                "text": f"{s.garden if s.garden else '*'}-{s.namespace if s.namespace else '*'}-{s.system if s.system else '*'}-{s.version if s.version else '*'}-{s.instance if s.instance else '*'}-{s.command if s.command else '*'}",
                "value": SchemaParser.serialize_subscriber(s, to_string=True),
            }
            for s in self.get_topic(topic_id).subscribers
        ]

    @command
    @parameter(
        key="topic_id",
        type="String",
        description="Select a topic",
        choices={
            "type": "command",
            "display": "select",
            "value": "get_topic_choices()",
        },
    )
    def get_topic(self, topic_id) -> BrewtilsTopic:
        return self.client.get_topic(topic_id)

    @command
    @parameter(
        key="topic_id",
        type="String",
        description="Select a topic",
        choices={
            "type": "command",
            "display": "select",
            "value": "get_topic_choices()",
        },
    )
    def remove_topic(self, topic_id: str):
        return self.client.remove_topic(topic_id)

    @command
    @parameter(
        key="topic_id",
        type="String",
        description="Select a topic",
        choices={
            "type": "command",
            "display": "select",
            "value": "get_topic_choices()",
        },
    )
    @parameter(key="garden", optional=True, nullable=True)
    @parameter(key="namespace", optional=True, nullable=True)
    @parameter(key="system", optional=True, nullable=True)
    @parameter(key="version", optional=True, nullable=True)
    @parameter(key="instance", optional=True, nullable=True)
    @parameter(key="command", optional=True, nullable=True)
    def add_subscriber(
        self,
        topic_id: str,
        garden: str = None,
        namespace: str = None,
        system: str = None,
        version: str = None,
        instance: str = None,
        command: str = None,
    ):
        subscriber_dict = {
            "garden": garden,
            "namespace": namespace,
            "system": system,
            "version": version,
            "instance": instance,
            "command": command,
        }
        return self.client.update_topic(topic_id, add=subscriber_dict)

    @command
    @parameter(
        key="topic_id",
        type="String",
        description="Select a topic",
        choices={
            "type": "command",
            "display": "select",
            "value": "get_topic_choices()",
        },
    )
    @parameter(
        key="subscriber_dict",
        type="String",
        choices={
            "type": "command",
            "display": "select",
            "strict": True,
            "value": "get_subscriber_choices(topic_id=${topic_id})",
        },
    )
    def remove_subscriber(
        self,
        topic_id: str,
        subscriber_dict: str,
    ):
        subscriber = json.loads(subscriber_dict)
        return self.client.update_topic(topic_id, remove=subscriber)


def main():
    plugin = Plugin(
        name="topic",
        version=__version__,
        description="A plugin that manages topics",
        max_concurrent=1,
    )
    plugin.client = Topic()
    plugin.run()


if __name__ == "__main__":
    main()
