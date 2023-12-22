from brewtils import command, system, Plugin, SystemClient

__version__ = "3.0.0.dev0"


class MaxConccurentClient(object):
    """Client that will break if max concurrency is not fixed"""

    def __init__(self):
        self.system_client  = SystemClient(system_name="max_conccurent")

    @command()
    def one_concurrent(self) -> bool:
        """One concurrent request"""
        return True
    
    @command()
    def two_concurrent(self) -> bool:
        """Two concurrent request"""
        return self.system_client.one_concurrent()
    
    @command()
    def three_concurrent(self) -> bool:
        """Three concurrent request"""
        return self.system_client.two_concurrent()
    
    @command()
    def four_concurrent(self) -> bool:
        """Four concurrent request"""
        return self.system_client.three_concurrent()
    
    @command()
    def five_concurrent(self) -> bool:
        """Five concurrent request"""
        return self.system_client.four_concurrent()
    
    @command()
    def six_concurrent(self) -> bool:
        """Six concurrent request"""
        return self.system_client.five_concurrent()
    
    @command()
    def custom_concurrent(self, concurrent_amount: int ) -> int:
        """Custom concurrent request"""
        if concurrent_amount > 0:
            return self.system_client.custom_concurrent(concurrent_amount = (concurrent_amount - 1))
        return concurrent_amount
    
    @command()
    def custom_local_calls(self, concurrent_amount: int) -> int:
        """Local function calls"""
        if concurrent_amount > 0:
            return self.custom_local_calls(concurrent_amount = (concurrent_amount - 1))
        return concurrent_amount



def main():
    plugin = Plugin(
        name="max_conccurent",
        version=__version__,
        description="Client that will break if max concurrency is not fixed",
    )
    plugin.client = MaxConccurentClient()
    plugin.run()


if __name__ == "__main__":
    main()
