from antlr4 import *
from .DemoVisitor import DemoVisitor
from .DemoParser import DemoParser


class Visitor(DemoVisitor):
    def __init__(self):
        self.variables = {}
        self.subroutines = {}

    def visitRead(self, ctx: DemoParser.ReadContext):
        variable = ctx.ID().getText()
        value = input("> ")
        self.variables[variable] = int(value)

    def visitPrint(self, ctx: DemoParser.PrintContext):
        value = self.visit(ctx.expr())
        print(value)

    def visitAssign(self, ctx: DemoParser.AssignContext):
        variable = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.variables[variable] = value

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

    def visitSubroutine(self, ctx: DemoParser.SubroutineContext):
        name = ctx.ID().getText()
        self.subroutines[name] = ctx.body()
