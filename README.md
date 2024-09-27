# SLURM node list parser

EBNF grammar for parsing SLURM node list definitions using TatSu

## prior art
 * the [magic slurm node list parser](https://gist.github.com/ebirn/cf52876120648d7d85501fcbf185ff07)
 * [python-hostlist](https://pypi.org/project/python-hostlist) found when thinking about renaming to "hostlist"

### example
```
node-[1,3][1,2,3-5]
```
gets expanded to
```python
from slurm_node_list_parser import parse
print([i for i in parse("node-[1,3][1,2,3-5]")])
```

```json5
[
   'node-11', 'node-12', 'node-13', 'node-14', 'node-15',
   'node-31', 'node-32', 'node-33', 'node-34', 'node-35'
]
```

## Regenerate parser
```
tatsu --generate-parser --name slurm_node_list --outfile src/slurm_node_list_parser/parser.py src/slurm_node_list_parser/parser.ebnf
```
