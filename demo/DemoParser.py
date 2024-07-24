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
        4,1,17,94,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,26,8,0,11,
        0,12,0,27,1,1,1,1,1,1,1,1,1,1,1,1,1,2,4,2,37,8,2,11,2,12,2,38,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,48,8,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,
        1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,
        1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,3,11,84,8,11,
        1,11,1,11,1,11,5,11,89,8,11,10,11,12,11,92,9,11,1,11,0,1,22,12,0,
        2,4,6,8,10,12,14,16,18,20,22,0,1,1,0,15,16,92,0,25,1,0,0,0,2,29,
        1,0,0,0,4,36,1,0,0,0,6,47,1,0,0,0,8,49,1,0,0,0,10,53,1,0,0,0,12,
        57,1,0,0,0,14,61,1,0,0,0,16,66,1,0,0,0,18,69,1,0,0,0,20,74,1,0,0,
        0,22,83,1,0,0,0,24,26,3,2,1,0,25,24,1,0,0,0,26,27,1,0,0,0,27,25,
        1,0,0,0,27,28,1,0,0,0,28,1,1,0,0,0,29,30,5,1,0,0,30,31,5,13,0,0,
        31,32,5,2,0,0,32,33,3,4,2,0,33,34,5,3,0,0,34,3,1,0,0,0,35,37,3,6,
        3,0,36,35,1,0,0,0,37,38,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,5,
        1,0,0,0,40,48,3,8,4,0,41,48,3,10,5,0,42,48,3,12,6,0,43,48,3,14,7,
        0,44,48,3,16,8,0,45,48,3,18,9,0,46,48,3,20,10,0,47,40,1,0,0,0,47,
        41,1,0,0,0,47,42,1,0,0,0,47,43,1,0,0,0,47,44,1,0,0,0,47,45,1,0,0,
        0,47,46,1,0,0,0,48,7,1,0,0,0,49,50,5,4,0,0,50,51,3,22,11,0,51,52,
        5,5,0,0,52,9,1,0,0,0,53,54,5,6,0,0,54,55,5,13,0,0,55,56,5,5,0,0,
        56,11,1,0,0,0,57,58,5,7,0,0,58,59,5,13,0,0,59,60,5,5,0,0,60,13,1,
        0,0,0,61,62,5,13,0,0,62,63,5,8,0,0,63,64,3,22,11,0,64,65,5,5,0,0,
        65,15,1,0,0,0,66,67,5,9,0,0,67,68,5,5,0,0,68,17,1,0,0,0,69,70,5,
        10,0,0,70,71,3,22,11,0,71,72,5,13,0,0,72,73,5,5,0,0,73,19,1,0,0,
        0,74,75,5,11,0,0,75,76,3,22,11,0,76,77,5,13,0,0,77,78,5,5,0,0,78,
        21,1,0,0,0,79,80,6,11,-1,0,80,84,5,13,0,0,81,84,5,12,0,0,82,84,5,
        14,0,0,83,79,1,0,0,0,83,81,1,0,0,0,83,82,1,0,0,0,84,90,1,0,0,0,85,
        86,10,4,0,0,86,87,7,0,0,0,87,89,3,22,11,5,88,85,1,0,0,0,89,92,1,
        0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,23,1,0,0,0,92,90,1,0,0,0,5,
        27,38,47,83,90
    ]

class DemoParser ( Parser ):

    grammarFileName = "Demo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'sub'", "'{'", "'}'", "'print'", "';'", 
                     "'read'", "'gosub'", "'='", "'halt'", "'biz'", "'bgz'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUMBER", "ID", "STRING", "ADD", "SUB", "WS" ]

    RULE_program = 0
    RULE_subroutine = 1
    RULE_body = 2
    RULE_statement = 3
    RULE_print = 4
    RULE_read = 5
    RULE_gosub = 6
    RULE_assign = 7
    RULE_halt = 8
    RULE_biz = 9
    RULE_bgz = 10
    RULE_expr = 11

    ruleNames =  [ "program", "subroutine", "body", "statement", "print", 
                   "read", "gosub", "assign", "halt", "biz", "bgz", "expr" ]

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
    WS=17

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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 11984) != 0)):
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


        def biz(self):
            return self.getTypedRuleContext(DemoParser.BizContext,0)


        def bgz(self):
            return self.getTypedRuleContext(DemoParser.BgzContext,0)


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
            self.state = 47
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
                self.biz()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 7)
                self.state = 46
                self.bgz()
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
            self.state = 49
            self.match(DemoParser.T__3)
            self.state = 50
            self.expr(0)
            self.state = 51
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
            self.state = 53
            self.match(DemoParser.T__5)
            self.state = 54
            self.match(DemoParser.ID)
            self.state = 55
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
            self.state = 57
            self.match(DemoParser.T__6)
            self.state = 58
            self.match(DemoParser.ID)
            self.state = 59
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
            self.state = 61
            self.match(DemoParser.ID)
            self.state = 62
            self.match(DemoParser.T__7)
            self.state = 63
            self.expr(0)
            self.state = 64
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
            self.state = 66
            self.match(DemoParser.T__8)
            self.state = 67
            self.match(DemoParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BizContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(DemoParser.ExprContext,0)


        def ID(self):
            return self.getToken(DemoParser.ID, 0)

        def getRuleIndex(self):
            return DemoParser.RULE_biz

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBiz" ):
                return visitor.visitBiz(self)
            else:
                return visitor.visitChildren(self)




    def biz(self):

        localctx = DemoParser.BizContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_biz)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(DemoParser.T__9)
            self.state = 70
            self.expr(0)
            self.state = 71
            self.match(DemoParser.ID)
            self.state = 72
            self.match(DemoParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BgzContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(DemoParser.ExprContext,0)


        def ID(self):
            return self.getToken(DemoParser.ID, 0)

        def getRuleIndex(self):
            return DemoParser.RULE_bgz

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBgz" ):
                return visitor.visitBgz(self)
            else:
                return visitor.visitChildren(self)




    def bgz(self):

        localctx = DemoParser.BgzContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_bgz)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(DemoParser.T__10)
            self.state = 75
            self.expr(0)
            self.state = 76
            self.match(DemoParser.ID)
            self.state = 77
            self.match(DemoParser.T__4)
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
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                localctx = DemoParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 80
                self.match(DemoParser.ID)
                pass
            elif token in [12]:
                localctx = DemoParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 81
                self.match(DemoParser.NUMBER)
                pass
            elif token in [14]:
                localctx = DemoParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 82
                self.match(DemoParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 90
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = DemoParser.AddSubContext(self, DemoParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 85
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 86
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==15 or _la==16):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 87
                    self.expr(5) 
                self.state = 92
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
                return self.precpred(self._ctx, 4)
         




