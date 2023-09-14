from typing import Optional, List
from antlr4 import InputStream, Token
from antlr_playground.grammar.bdsLexer import bdsLexer
from lsprotocol.types import Position


def get_all_tokens(source_code: str) -> List[Token]:
    input_stream = InputStream(source_code)
    lexer = bdsLexer(input_stream)
    return lexer.getAllTokens()


def is_position_within_token(position: Position, token: Token) -> bool:
    return (
        token.line == position.line
        and token.column <= position.character < token.column + len(token.text)
    )


def get_symbol_from_tokens(
    source_code: str, position: Position
) -> Optional[str]:
    tokens = get_all_tokens(source_code)

    for token in tokens:
        if is_position_within_token(position, token):
            return token.text

    return None
