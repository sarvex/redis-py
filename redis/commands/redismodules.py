from json import JSONDecoder, JSONEncoder


class RedisModuleCommands:
    """This class contains the wrapper functions to bring supported redis
    modules into the command namespace.
    """

    def json(self, encoder=JSONEncoder(), decoder=JSONDecoder()):
        """Access the json namespace, providing support for redis json."""

        from .json import JSON

        return JSON(client=self, encoder=encoder, decoder=decoder)

    def ft(self, index_name="idx"):
        """Access the search namespace, providing support for redis search."""

        from .search import Search

        return Search(client=self, index_name=index_name)

    def ts(self):
        """Access the timeseries namespace, providing support for
        redis timeseries data.
        """

        from .timeseries import TimeSeries

        return TimeSeries(client=self)

    def bf(self):
        """Access the bloom namespace."""

        from .bf import BFBloom

        return BFBloom(client=self)

    def cf(self):
        """Access the bloom namespace."""

        from .bf import CFBloom

        return CFBloom(client=self)

    def cms(self):
        """Access the bloom namespace."""

        from .bf import CMSBloom

        return CMSBloom(client=self)

    def topk(self):
        """Access the bloom namespace."""

        from .bf import TOPKBloom

        return TOPKBloom(client=self)

    def tdigest(self):
        """Access the bloom namespace."""

        from .bf import TDigestBloom

        return TDigestBloom(client=self)

    def graph(self, index_name="idx"):
        """Access the graph namespace, providing support for
        redis graph data.
        """

        from .graph import Graph

        return Graph(client=self, name=index_name)


class AsyncRedisModuleCommands(RedisModuleCommands):
    def ft(self, index_name="idx"):
        """Access the search namespace, providing support for redis search."""

        from .search import AsyncSearch

        return AsyncSearch(client=self, index_name=index_name)

    def graph(self, index_name="idx"):
        """Access the graph namespace, providing support for
        redis graph data.
        """

        from .graph import AsyncGraph

        return AsyncGraph(client=self, name=index_name)
