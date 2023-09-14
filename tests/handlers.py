from pygls.server import LanguageServer
from lsprotocol.types import DefinitionParams, Location
from antlr_playground.symbol_finder import get_symbol_from_tokens
from antlr_playground.symbol_definitions import SymbolDefinitionsIndex


def handle_get_document_definition(
    server: LanguageServer, params: DefinitionParams
) -> Location:
    uri = params.text_document.uri
    position = params.position

    source_code = server.workspace.get_document(uri).source
    symbol = get_symbol_from_tokens(source_code, position)
    index = SymbolDefinitionsIndex(source_code)
    return index.get(symbol)
