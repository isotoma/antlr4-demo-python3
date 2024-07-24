# Generated from Demo.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DemoParser import DemoParser
else:
    from DemoParser import DemoParser

# This class defines a complete generic visitor for a parse tree produced by DemoParser.

class DemoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DemoParser#program.
    def visitProgram(self, ctx:DemoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemoParser#subroutine.
    def visitSubroutine(self, ctx:DemoParser.SubroutineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemoParser#body.
    def visitBody(self, ctx:DemoParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemoParser#statement.
    def visitStatement(self, ctx:DemoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemoParser#print.
    def visitPrint(self, ctx:DemoParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemoParser#read.
    def visitRead(self, ctx:DemoParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemoParser#gosub.
    def visitGosub(self, ctx:DemoParser.GosubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemoParser#assign.
    def visitAssign(self, ctx:DemoParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemoParser#halt.
    def visitHalt(self, ctx:DemoParser.HaltContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemoParser#biz.
    def visitBiz(self, ctx:DemoParser.BizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemoParser#bgz.
    def visitBgz(self, ctx:DemoParser.BgzContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemoParser#Number.
    def visitNumber(self, ctx:DemoParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemoParser#AddSub.
    def visitAddSub(self, ctx:DemoParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemoParser#Id.
    def visitId(self, ctx:DemoParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemoParser#String.
    def visitString(self, ctx:DemoParser.StringContext):
        return self.visitChildren(ctx)



del DemoParser