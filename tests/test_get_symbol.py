from antlr_playground.symbol_finder import get_symbol_at_location
import pytest
from lsprotocol.types import Position

code = """
class TheQuickBrownFox {
    void TheQuickBrownFox() {}
}
fox := new TheQuickBrownFox()
void jumpOverTheLazyDog() {}
jumpOverTheLazyDog()
"""


@pytest.mark.parametrize(
    "line,character,expected_symbol",
    [
        (5, 14, "TheQuickBrownFox"),
        (7, 0, "jumpOverTheLazyDog"),
    ],
)
def test_get_symbol_at_location(line, character, expected_symbol):
    assert (
        get_symbol_at_location(code, Position(line=line, character=character))
        == expected_symbol
    )
