from typing import Optional
from antlr4 import (
    CommonTokenStream,
    ParseTreeWalker,
    InputStream,
)
from antlr4.tree.Tree import TerminalNodeImpl

from antlr_playground.grammar.bdsLexer import bdsLexer
from antlr_playground.grammar.bdsParser import bdsParser
from antlr_playground.grammar.bdsListener import bdsListener
from lsprotocol.types import Range, Position


class SymbolDefinitionListener(bdsListener):
    def __init__(self) -> None:
        self.symbol_map: dict[str, Range] = {}

    def enterClassDef(self, ctx: bdsParser.ClassDefContext) -> None:
        token: TerminalNodeImpl = ctx.ID(0)
        class_name = token.getText()
        symbol = token.getSymbol()
        start_position = Position(symbol.column, symbol.line)
        end_position = Position(symbol.column, symbol.line + len(class_name))
        range = Range(start_position, end_position)
        self.symbol_map[class_name] = range


class SymbolTable:
    def __init__(self, source_code: str) -> None:
        self.source_code = source_code
        self.symbol_map = self._initialize_symbol_map()

    def _initialize_symbol_map(self) -> dict[str, Range]:
        input_stream = InputStream(self.source_code)
        lexer = bdsLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = bdsParser(tokens)
        tree = parser.programUnit()
        listener = SymbolDefinitionListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        return listener.symbol_map

    def get(self, symbol: str) -> Optional[Range]:
        return self.symbol_map.get(symbol)
