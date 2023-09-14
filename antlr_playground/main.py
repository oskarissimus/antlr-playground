from pygls.server import LanguageServer
from antlr_playground.handlers import (
    handle_get_document_definition,
)
from lsprotocol.types import (
    TEXT_DOCUMENT_DEFINITION,
)

server = LanguageServer("BDS Language Server", "0.0.1")
server.feature(TEXT_DOCUMENT_DEFINITION)(handle_get_document_definition)
server.start_io()
