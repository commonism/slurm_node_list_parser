from .models import NodeList

from .parser import slurm_node_listParser as Parser


def parse(data: str):
    parser = Parser(semantics=Semantic())
    v = parser.parse(data, semantics=Semantic())
    return v


class Semantic:
    def nodes(self, ast):
        return NodeList(ast)

    def bracketed(self, ast):
        return NodeList.RangeList(ast[1])

    def node(self, ast):
        return NodeList.Node(ast.segments)

    def range_list(self, ast):
        match ast.type:
            case "range":
                return NodeList.Segment.Range(ast.begin, ast.end)
            case "item":
                return NodeList.Segment.Item(ast.value)
        raise ValueError(ast.type)
