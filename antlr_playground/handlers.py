from typing import Optional
from pygls.server import LanguageServer
from lsprotocol.types import DefinitionParams, Location
from antlr_playground.symbol_finder import get_symbol_from_tokens
from antlr_playground.symbol_table import SymbolTable


def handle_get_document_definition(
    server: LanguageServer, params: DefinitionParams
) -> Optional[Location]:
    uri = params.text_document.uri
    position = params.position

    source_code = server.workspace.get_document(uri).source
    symbol = get_symbol_from_tokens(source_code, position)
    if symbol is None:
        return None
    symbol_table = SymbolTable(source_code)
    symbol_range = symbol_table.get(symbol)
    if symbol_range is None:
        return None
    return Location(uri, symbol_range)
