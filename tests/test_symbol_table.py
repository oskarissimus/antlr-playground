code = """class TheQuickBrownFox {
    void TheQuickBrownFox() {}
}
fox := new TheQuickBrownFox()
int returnTwo() {
    return 2
}
int returnThree() {
    return 3
}
two := returnTwo()
three := returnThree()
println two + three
"""
import pytest
from antlr_playground.symbol_table import SymbolTable
from lsprotocol.types import Range, Position


@pytest.mark.parametrize(
    "symbol,expected_range",
    [
        ("TheQuickBrownFox", Range(Position(2, 9), Position(2, 25))),
        ("returnTwo", Range(Position(5, 4), Position(5, 13))),
        ("returnThree", Range(Position(8, 4), Position(8, 15))),
        ("two", Range(Position(11, 0), Position(11, 3))),
        ("three", Range(Position(12, 0), Position(12, 5))),
    ],
)
def test_symbol_table(symbol, expected_range):
    st = SymbolTable(code)
    assert st.get(symbol) == expected_range
