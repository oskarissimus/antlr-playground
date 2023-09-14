from typing import Optional
from antlr4 import CommonTokenStream, InputStream
from antlr_playground.grammar.bdsLexer import bdsLexer
from antlr_playground.grammar.bdsParser import bdsParser
from antlr_playground.grammar.bdsListener import bdsListener
from antlr4 import ParseTreeWalker, ParserRuleContext
from lsprotocol.types import Position

from antlr4 import CommonTokenStream, InputStream
from antlr_playground.grammar.bdsLexer import bdsLexer
from antlr_playground.grammar.bdsParser import bdsParser
from antlr_playground.grammar.bdsListener import bdsListener
from antlr4 import ParseTreeWalker, ParserRuleContext
from lsprotocol.types import Position


class SymbolCaptureListener(bdsListener):
    def __init__(self, position: Position):
        super().__init__()
        self.position = position
        self.symbol: Optional[str] = None

    def enterExpression(self, ctx: ParserRuleContext):
        if is_relevant_position(ctx, self.position):
            if is_class_instantiation(ctx):
                self.symbol = get_class_name(ctx)
            elif is_function_call(ctx):
                self.symbol = get_function_name(ctx)


def is_function_call(ctx: ParserRuleContext) -> bool:
    return ctx.getText().endswith("()")


def get_function_name(ctx: ParserRuleContext) -> str:
    return ctx.getChild(0).getText()


def is_relevant_position(ctx: ParserRuleContext, position: Position) -> bool:
    result = (
        ctx.start.line == position.line
        and ctx.start.column <= position.character
    )
    if result:
        print(f"Relevant Context: {ctx.getText()}")
    return result


def is_class_instantiation(ctx: ParserRuleContext) -> bool:
    return ctx.getChildCount() > 0 and ctx.getChild(0).getText() == "new"


def get_class_name(ctx: ParserRuleContext) -> str:
    return ctx.getChild(1).getText()


def get_symbol_at_location(
    source_code: str, position: Position
) -> Optional[str]:
    input_stream = InputStream(source_code)
    lexer = bdsLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = bdsParser(token_stream)
    tree = parser.programUnit()
    listener = SymbolCaptureListener(position)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return listener.symbol
