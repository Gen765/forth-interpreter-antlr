# Generated from forth.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .forthParser import forthParser
else:
    from forthParser import forthParser

# This class defines a complete generic visitor for a parse tree produced by forthParser.

class forthVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by forthParser#program.
    def visitProgram(self, ctx:forthParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forthParser#PushNumber.
    def visitPushNumber(self, ctx:forthParser.PushNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forthParser#DefFunc.
    def visitDefFunc(self, ctx:forthParser.DefFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forthParser#CallFunc.
    def visitCallFunc(self, ctx:forthParser.CallFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forthParser#BodyNumber.
    def visitBodyNumber(self, ctx:forthParser.BodyNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forthParser#Conditional.
    def visitConditional(self, ctx:forthParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forthParser#BodyCall.
    def visitBodyCall(self, ctx:forthParser.BodyCallContext):
        return self.visitChildren(ctx)



del forthParser
