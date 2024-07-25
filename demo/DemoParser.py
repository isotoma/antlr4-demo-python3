# Generated from Demo.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,25,102,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,26,8,0,11,
        0,12,0,27,1,1,1,1,1,1,1,1,1,1,1,1,1,2,4,2,37,8,2,11,2,12,2,38,1,
        3,1,3,1,3,1,3,1,3,1,3,3,3,47,8,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,
        1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,3,9,79,8,9,1,10,1,10,1,10,1,10,1,11,1,11,
        1,11,1,11,3,11,89,8,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,97,8,11,
        10,11,12,11,100,9,11,1,11,0,1,22,12,0,2,4,6,8,10,12,14,16,18,20,
        22,0,3,1,0,20,25,1,0,15,16,1,0,17,18,101,0,25,1,0,0,0,2,29,1,0,0,
        0,4,36,1,0,0,0,6,46,1,0,0,0,8,48,1,0,0,0,10,52,1,0,0,0,12,56,1,0,
        0,0,14,60,1,0,0,0,16,65,1,0,0,0,18,68,1,0,0,0,20,80,1,0,0,0,22,88,
        1,0,0,0,24,26,3,2,1,0,25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,
        27,28,1,0,0,0,28,1,1,0,0,0,29,30,5,1,0,0,30,31,5,13,0,0,31,32,5,
        2,0,0,32,33,3,4,2,0,33,34,5,3,0,0,34,3,1,0,0,0,35,37,3,6,3,0,36,
        35,1,0,0,0,37,38,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,5,1,0,0,
        0,40,47,3,8,4,0,41,47,3,10,5,0,42,47,3,12,6,0,43,47,3,14,7,0,44,
        47,3,16,8,0,45,47,3,18,9,0,46,40,1,0,0,0,46,41,1,0,0,0,46,42,1,0,
        0,0,46,43,1,0,0,0,46,44,1,0,0,0,46,45,1,0,0,0,47,7,1,0,0,0,48,49,
        5,4,0,0,49,50,3,22,11,0,50,51,5,5,0,0,51,9,1,0,0,0,52,53,5,6,0,0,
        53,54,5,13,0,0,54,55,5,5,0,0,55,11,1,0,0,0,56,57,5,7,0,0,57,58,5,
        13,0,0,58,59,5,5,0,0,59,13,1,0,0,0,60,61,5,13,0,0,61,62,5,8,0,0,
        62,63,3,22,11,0,63,64,5,5,0,0,64,15,1,0,0,0,65,66,5,9,0,0,66,67,
        5,5,0,0,67,17,1,0,0,0,68,69,5,10,0,0,69,70,3,20,10,0,70,71,5,2,0,
        0,71,72,3,4,2,0,72,78,5,3,0,0,73,74,5,11,0,0,74,75,5,2,0,0,75,76,
        3,4,2,0,76,77,5,3,0,0,77,79,1,0,0,0,78,73,1,0,0,0,78,79,1,0,0,0,
        79,19,1,0,0,0,80,81,3,22,11,0,81,82,7,0,0,0,82,83,3,22,11,0,83,21,
        1,0,0,0,84,85,6,11,-1,0,85,89,5,13,0,0,86,89,5,12,0,0,87,89,5,14,
        0,0,88,84,1,0,0,0,88,86,1,0,0,0,88,87,1,0,0,0,89,98,1,0,0,0,90,91,
        10,5,0,0,91,92,7,1,0,0,92,97,3,22,11,6,93,94,10,4,0,0,94,95,7,2,
        0,0,95,97,3,22,11,5,96,90,1,0,0,0,96,93,1,0,0,0,97,100,1,0,0,0,98,
        96,1,0,0,0,98,99,1,0,0,0,99,23,1,0,0,0,100,98,1,0,0,0,7,27,38,46,
        78,88,96,98
    ]

class DemoParser ( Parser ):

    grammarFileName = "Demo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'sub'", "'{'", "'}'", "'print'", "';'", 
                     "'read'", "'gosub'", "'='", "'halt'", "'if'", "'else'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'-'", 
                     "'*'", "'/'", "<INVALID>", "'=='", "'!='", "'<'", "'<='", 
                     "'>'", "'>='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUMBER", "ID", "STRING", "ADD", "SUB", "MUL", "DIV", 
                      "WS", "EQ", "NE", "LT", "LE", "GT", "GE" ]

    RULE_program = 0
    RULE_subroutine = 1
    RULE_body = 2
    RULE_statement = 3
    RULE_print = 4
    RULE_read = 5
    RULE_gosub = 6
    RULE_assign = 7
    RULE_halt = 8
    RULE_if = 9
    RULE_compare = 10
    RULE_expr = 11

    ruleNames =  [ "program", "subroutine", "body", "statement", "print", 
                   "read", "gosub", "assign", "halt", "if", "compare", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    NUMBER=12
    ID=13
    STRING=14
    ADD=15
    SUB=16
    MUL=17
    DIV=18
    WS=19
    EQ=20
    NE=21
    LT=22
    LE=23
    GT=24
    GE=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subroutine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DemoParser.SubroutineContext)
            else:
                return self.getTypedRuleContext(DemoParser.SubroutineContext,i)


        def getRuleIndex(self):
            return DemoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = DemoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.subroutine()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubroutineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DemoParser.ID, 0)

        def body(self):
            return self.getTypedRuleContext(DemoParser.BodyContext,0)


        def getRuleIndex(self):
            return DemoParser.RULE_subroutine

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubroutine" ):
                return visitor.visitSubroutine(self)
            else:
                return visitor.visitChildren(self)




    def subroutine(self):

        localctx = DemoParser.SubroutineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_subroutine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(DemoParser.T__0)
            self.state = 30
            self.match(DemoParser.ID)
            self.state = 31
            self.match(DemoParser.T__1)
            self.state = 32
            self.body()
            self.state = 33
            self.match(DemoParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DemoParser.StatementContext)
            else:
                return self.getTypedRuleContext(DemoParser.StatementContext,i)


        def getRuleIndex(self):
            return DemoParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = DemoParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 35
                self.statement()
                self.state = 38 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 9936) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def print_(self):
            return self.getTypedRuleContext(DemoParser.PrintContext,0)


        def read(self):
            return self.getTypedRuleContext(DemoParser.ReadContext,0)


        def gosub(self):
            return self.getTypedRuleContext(DemoParser.GosubContext,0)


        def assign(self):
            return self.getTypedRuleContext(DemoParser.AssignContext,0)


        def halt(self):
            return self.getTypedRuleContext(DemoParser.HaltContext,0)


        def if_(self):
            return self.getTypedRuleContext(DemoParser.IfContext,0)


        def getRuleIndex(self):
            return DemoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = DemoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.print_()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.read()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.gosub()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 43
                self.assign()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 5)
                self.state = 44
                self.halt()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 6)
                self.state = 45
                self.if_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(DemoParser.ExprContext,0)


        def getRuleIndex(self):
            return DemoParser.RULE_print

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = DemoParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(DemoParser.T__3)
            self.state = 49
            self.expr(0)
            self.state = 50
            self.match(DemoParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DemoParser.ID, 0)

        def getRuleIndex(self):
            return DemoParser.RULE_read

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead" ):
                return visitor.visitRead(self)
            else:
                return visitor.visitChildren(self)




    def read(self):

        localctx = DemoParser.ReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_read)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(DemoParser.T__5)
            self.state = 53
            self.match(DemoParser.ID)
            self.state = 54
            self.match(DemoParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GosubContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DemoParser.ID, 0)

        def getRuleIndex(self):
            return DemoParser.RULE_gosub

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGosub" ):
                return visitor.visitGosub(self)
            else:
                return visitor.visitChildren(self)




    def gosub(self):

        localctx = DemoParser.GosubContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_gosub)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(DemoParser.T__6)
            self.state = 57
            self.match(DemoParser.ID)
            self.state = 58
            self.match(DemoParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DemoParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(DemoParser.ExprContext,0)


        def getRuleIndex(self):
            return DemoParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = DemoParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(DemoParser.ID)
            self.state = 61
            self.match(DemoParser.T__7)
            self.state = 62
            self.expr(0)
            self.state = 63
            self.match(DemoParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HaltContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DemoParser.RULE_halt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHalt" ):
                return visitor.visitHalt(self)
            else:
                return visitor.visitChildren(self)




    def halt(self):

        localctx = DemoParser.HaltContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_halt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(DemoParser.T__8)
            self.state = 66
            self.match(DemoParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compare(self):
            return self.getTypedRuleContext(DemoParser.CompareContext,0)


        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DemoParser.BodyContext)
            else:
                return self.getTypedRuleContext(DemoParser.BodyContext,i)


        def getRuleIndex(self):
            return DemoParser.RULE_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)




    def if_(self):

        localctx = DemoParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(DemoParser.T__9)
            self.state = 69
            self.compare()
            self.state = 70
            self.match(DemoParser.T__1)
            self.state = 71
            self.body()
            self.state = 72
            self.match(DemoParser.T__2)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 73
                self.match(DemoParser.T__10)
                self.state = 74
                self.match(DemoParser.T__1)
                self.state = 75
                self.body()
                self.state = 76
                self.match(DemoParser.T__2)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DemoParser.ExprContext)
            else:
                return self.getTypedRuleContext(DemoParser.ExprContext,i)


        def EQ(self):
            return self.getToken(DemoParser.EQ, 0)

        def NE(self):
            return self.getToken(DemoParser.NE, 0)

        def LT(self):
            return self.getToken(DemoParser.LT, 0)

        def LE(self):
            return self.getToken(DemoParser.LE, 0)

        def GT(self):
            return self.getToken(DemoParser.GT, 0)

        def GE(self):
            return self.getToken(DemoParser.GE, 0)

        def getRuleIndex(self):
            return DemoParser.RULE_compare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompare" ):
                return visitor.visitCompare(self)
            else:
                return visitor.visitChildren(self)




    def compare(self):

        localctx = DemoParser.CompareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_compare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.expr(0)
            self.state = 81
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66060288) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 82
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DemoParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NumberContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DemoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(DemoParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DemoParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DemoParser.ExprContext)
            else:
                return self.getTypedRuleContext(DemoParser.ExprContext,i)

        def ADD(self):
            return self.getToken(DemoParser.ADD, 0)
        def SUB(self):
            return self.getToken(DemoParser.SUB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DemoParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DemoParser.ExprContext)
            else:
                return self.getTypedRuleContext(DemoParser.ExprContext,i)

        def MUL(self):
            return self.getToken(DemoParser.MUL, 0)
        def DIV(self):
            return self.getToken(DemoParser.DIV, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DemoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(DemoParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DemoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(DemoParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = DemoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                localctx = DemoParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 85
                self.match(DemoParser.ID)
                pass
            elif token in [12]:
                localctx = DemoParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 86
                self.match(DemoParser.NUMBER)
                pass
            elif token in [14]:
                localctx = DemoParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 87
                self.match(DemoParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 98
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 96
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = DemoParser.AddSubContext(self, DemoParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 90
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 91
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 92
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = DemoParser.MulDivContext(self, DemoParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 93
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 94
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 95
                        self.expr(5)
                        pass

             
                self.state = 100
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




