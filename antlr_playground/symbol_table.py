from typing import Optional
from antlr4 import (
    CommonTokenStream,
    ParseTreeWalker,
    InputStream,
)
from antlr4.tree.Tree import TerminalNodeImpl

from antlr_playground.grammar import Lexer, Parser, Listener
from lsprotocol.types import Range, Position


class SymbolDefinitionListener(Listener):
    def __init__(self) -> None:
        self.symbol_map: dict[str, Range] = {}

    def enterFunctionDeclaration(
        self, ctx: Parser.FunctionDeclarationContext
    ) -> None:
        self._add_symbol(ctx.ID())

    def enterVariableInitImplicit(
        self, ctx: Parser.VariableInitImplicitContext
    ) -> None:
        self._add_symbol(ctx.ID())

    def _add_symbol(self, token: TerminalNodeImpl) -> None:
        symbol_name = token.getText()
        symbol = token.getSymbol()
        start = Position(symbol.line, symbol.column)
        end = Position(symbol.line, symbol.column + len(symbol_name))
        self.symbol_map[symbol_name] = Range(start, end)


class SymbolTable:
    def __init__(self, source_code: str) -> None:
        self.source_code = source_code
        self.symbol_map = self._initialize_symbol_map()

    def _initialize_symbol_map(self) -> dict[str, Range]:
        input_stream = InputStream(self.source_code)
        lexer = Lexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = Parser(tokens)
        listener = SymbolDefinitionListener()
        walker = ParseTreeWalker()
        walker.walk(listener, parser.programUnit())
        return listener.symbol_map

    def get(self, symbol: str) -> Optional[Range]:
        return self.symbol_map.get(symbol)
