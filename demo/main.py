import sys
from antlr4 import *
from .DemoLexer import DemoLexer
from .DemoParser import DemoParser
from .visitor import Visitor


def main(argv):
    s = FileStream(sys.argv[1])
    lexer = DemoLexer(s)
    stream = CommonTokenStream(lexer)
    parser = DemoParser(stream)
    tree = parser.program()
    visitor = Visitor()
    visitor.visit(tree)
    visitor.visit(visitor.subroutines["main"])
