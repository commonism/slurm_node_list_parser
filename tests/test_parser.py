import itertools

import tatsu
from pathlib import Path

import pytest

import sys

v = sys.path

TESTS = [
    pytest.param("a-a,a-b", {"a-a", "a-b"}, id="list"),
    pytest.param("a[1-2]", {"a1", "a2"}, id="range"),
    pytest.param("a[3,4]", {"a3", "a4"}, id="items"),
    pytest.param("a[1-2,3,4]", {"a1", "a2", "a3", "a4"}, id="range-items"),
    pytest.param("a[01-02]", {"a01", "a02"}, id="zfill"),
    pytest.param("a[1-2][1-2]", {"a11", "a12", "a21", "a22"}, id="multi"),
    pytest.param(
        "a[01-02,11-12,17,18],b[03-04,13-14,19,20],c[1-2][3,4]",
        {"a01", "a02", "a11", "a12", "a17", "a18"}
        | {"b03", "b04", "b13", "b14", "b19", "b20"}
        | {"c13", "c14", "c23", "c24"},
        id="all",
    ),
]


@pytest.mark.parametrize("pattern,expanded", TESTS)
def test_node_list_patterns(pattern, expanded):
    from slurm_node_list_parser import Semantic

    parser = tatsu.compile(
        (Path(__file__).parent.parent / "src" / "slurm_node_list_parser" / "parser.ebnf").read_text()
    )
    v = parser.parse(pattern, semantics=Semantic())

    assert {i for i in v} == expanded


@pytest.mark.parametrize("pattern,expanded", TESTS)
def test_node_list_parser(pattern, expanded):
    from slurm_node_list_parser import parse

    v = parse(pattern)
    assert {i for i in v} == expanded
