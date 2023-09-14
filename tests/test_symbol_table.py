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
        ("TheQuickBrownFox", Range(Position(1, 6), Position(1, 22))),
    ],
)
def test_symbol_table(symbol, expected_range):
    st = SymbolTable(code)
    assert st.get(symbol) == expected_range
