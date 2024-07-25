from antlr4 import *
from .DemoVisitor import DemoVisitor
from .DemoParser import DemoParser
import sys


class Visitor(DemoVisitor):
    def __init__(self):
        self.variables = {}
        self.subroutines = {}

    def visitPrint(self, ctx: DemoParser.PrintContext):
        value = self.visit(ctx.expr())
        print(value)

    def visitRead(self, ctx: DemoParser.ReadContext):
        variable = ctx.ID().getText()
        value = input("> ")
        self.variables[variable] = int(value)

    def visitGosub(self, ctx: DemoParser.GosubContext):
        return self.visit(self.subroutines[ctx.ID().getText()])

    def visitAssign(self, ctx: DemoParser.AssignContext):
        variable = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.variables[variable] = value

    def visitHalt(self, ctx: DemoParser.HaltContext):
        sys.exit(0)

    def visitNumber(self, ctx: DemoParser.NumberContext):
        return int(ctx.NUMBER().getText())

    def visitId(self, ctx: DemoParser.IdContext):
        variable = ctx.ID().getText()
        return self.variables[variable]

    def visitString(self, ctx: DemoParser.StringContext):
        return ctx.STRING().getText()[1:-1]

    def visitAddSub(self, ctx: DemoParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == DemoParser.ADD:
            return left + right
        else:
            return left - right

    def visitMulDiv(self, ctx: DemoParser.MulDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == DemoParser.MUL:
            return left * right
        else:
            return left // right

    def visitSubroutine(self, ctx: DemoParser.SubroutineContext):
        name = ctx.ID().getText()
        self.subroutines[name] = ctx.body()

    def visitCompare(self, ctx: DemoParser.CompareContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == DemoParser.EQ:
            return left == right
        elif ctx.op.type == DemoParser.NE:
            return left != right
        elif ctx.op.type == DemoParser.LT:
            return left < right
        elif ctx.op.type == DemoParser.LE:
            return left <= right
        elif ctx.op.type == DemoParser.GT:
            return left > right
        elif ctx.op.type == DemoParser.GE:
            return left >= right

    def visitIf(self, ctx: DemoParser.IfContext):
        if self.visit(ctx.compare()):
            return self.visit(ctx.body(0))
        else:
            if ctx.body(1):
                return self.visit(ctx.body(1))
