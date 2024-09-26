import collections
import itertools


class NodeList:
    class Segment:
        class Range(collections.namedtuple("Range", ["begin", "end"])):
            def __iter__(self):
                if self.begin[0] == "0" and self.begin != "0":
                    assert len(self.begin) == len(self.end), (
                        "Boundaries of a ranged string with padding " "must have the same length."
                    )
                    mod = lambda x: x.zfill(len(self.begin))
                else:
                    mod = lambda x: x
                yield from (mod(str(x)) for x in range(int(self.begin), int(self.end) + 1))

        Item = collections.namedtuple("Item", ["value"])

    class RangeList(collections.namedtuple("RangeList", ["values"])):
        def __iter__(self):
            for i in self.values:
                if isinstance(i, NodeList.Segment.Item):
                    yield i.value
                elif isinstance(i, NodeList.Segment.Range):
                    yield from i

    class Node(collections.namedtuple("Node", ["segments"])):
        def __iter__(self):
            r = ""
            segments = []
            for p in self.segments:
                if isinstance(p, str):
                    segments.append([p])
                elif isinstance(p, NodeList.RangeList):
                    segments.append(p)
            items = itertools.product(*segments)
            r = map(lambda x: "".join(x), items)
            yield from r

    def __init__(self, v):
        self.value = v

    def __iter__(self):
        for i in self.value:
            yield from i

    def __repr__(self):
        return repr(self.value)
