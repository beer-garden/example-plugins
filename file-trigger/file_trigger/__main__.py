from brewtils import parameter, Plugin, get_current_request_read_only, SystemClient
import os

__version__ = "3.0.0.dev0"

class FileTriggerClient(object):
    """Client that runs off File Trigger Scheduler Logic"""

    def __init__(self):
        self.system_client  = SystemClient()

    @parameter(
        key="upload_file",
        type="Boolean",
        description="Should File be uploaded to Beer Garden prior to processing?",
        default=False,
    )
    @parameter(
        key="delete_file",
        type="Boolean",
        description="Should File be deleted after processing?",
        default=False,
    )
    def file_create_trigger(self, upload_file: bool=False, delete_file: bool = True):
        """Used for File Trigger Jobs"""

        # Grab the file path from the metadata. Currently there isn't a clean way to 
        # inject the path into the input parameters
        current_request = get_current_request_read_only()

        if "src_path" not in current_request.metadata:
            raise Exception("Missing 'src_path' metadata from file trigger")
        
        file_path = current_request.metadata["src_path"]

        if not os.path.exists(file_path):
            raise Exception(f"File path does not exist: {file_path}")
        
        if upload_file:
            # Uploading the file is good for scenarios where the command that processes the file does
            # not have access to the file path

            # Uploading to Base64 Parameters
            self.system_client.process_file_upload(uploaded_file=file_path)
            # The Base64 file can also be passed in via `open()`, if file path is provided
            # as a String, then Brewtils will invoke `open(path, 'rb')`
            # self.system_client.process_file_upload(uploaded_file=open(file_path, "r"))

            # Uploading to Bytes Parameters
            self.system_client.process_file_upload_bytes(uploaded_file=open(file_path, "rb").read())
        else:
            self.system_client.process_file(file_path=file_path)
        
        if delete_file:
            os.remove(file_path)


    @parameter(
        key="file_path",
        type="String",
        description="Path to file to be processed",
    )
    def process_file(self, file_path:str):
        """Returns contents of file path provided"""

        with open(file_path, 'r') as file:
            file_content = file.read()
        return file_content

    
    @parameter(
        key="uploaded_file",
        type="Base64",
        description="Path to file to be processed",
    )
    def process_file_upload(self, uploaded_file):
        """Returns contents of file uploaded"""
        return uploaded_file.read()


    @parameter(
        key="uploaded_file",
        type="Bytes",
        description="Path to file to be processed",
    )
    def process_file_upload_bytes(self, uploaded_file):
        """Returns contents of file uploaded"""
        return uploaded_file


def main():
    plugin = Plugin(
        name="file_trigger",
        version=__version__,
        description="Example for how to handle file triggers",
    )
    plugin.client = FileTriggerClient()
    plugin.run()


if __name__ == "__main__":
    main()
