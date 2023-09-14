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
from antlr_playground.symbol_finder import get_symbol_from_tokens
import pytest
from lsprotocol.types import Position


@pytest.mark.parametrize(
    "line,character,expected_symbol",
    [
        (4, 14, "TheQuickBrownFox"),
        (11, 8, "returnTwo"),
        (12, 10, "returnThree"),
        (13, 8, "two"),
        (13, 14, "three"),
    ],
)
def test_get_symbol_at_location(line, character, expected_symbol):
    assert (
        get_symbol_from_tokens(code, Position(line=line, character=character))
        == expected_symbol
    )
