import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from brewtils import Plugin, SystemClient, command, schema_parser, system

__version__ = "3.0.0.dev0"


class HTTPRequestHandler(BaseHTTPRequestHandler):
    """HTTP request handler with additional properties and functions."""

    def __init__(self, *args, **kwargs):
        self.system_client = SystemClient(system_name="echo")
        self.serializer = schema_parser.SchemaParser()
        super().__init__(*args, **kwargs)

    def do_GET(self):
        """handle GET requests."""

        request = self.system_client.say(message="GET_API", loud=False)

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        self.wfile.write(
            self.serializer.serialize_request(request, to_string=True).encode(
                encoding="utf_8"
            )
        )


@system
class EchoHttpClient(object):
    """
    Client that hosts an HTTP server to echos things.

    This is an example of how to handle external systems connecting that have
    limited support for development allowing for the plugin to do the heavy
    lifting in transforming input/output data to match the external system
    expectations
    """

    def __init__(self, port: int = 8888):
        self._thread = None
        self.port = port
        self._start_thread()

    def _start_thread(self):

        if self._thread is None or not self._thread.is_alive():
            self._thread = threading.Thread(target=self._start_http_server)
            self._thread.start()

    def _start_http_server(
        self, server_class=ThreadingHTTPServer, handler_class=HTTPRequestHandler
    ):
        server_address = ("", self.port)
        httpd = server_class(server_address, handler_class)
        httpd.serve_forever()

    @command()
    def check_status(self) -> bool:
        """Local function calls"""
        return not (self._thread is None or not self._thread.is_alive())


def main():
    plugin = Plugin(
        name="echo_http_server",
        version=__version__,
        description="A plugin that starts an HTTP server to invoke Echo commands",
    )
    plugin.client = EchoHttpClient()
    plugin.run()


if __name__ == "__main__":
    main()
