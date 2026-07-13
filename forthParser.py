# Generated from forth.g4 by ANTLR 4.13.2
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
        4,1,10,49,2,0,7,0,2,1,7,1,2,2,7,2,1,0,5,0,8,8,0,10,0,12,0,11,9,0,
        1,0,1,0,1,1,1,1,1,1,1,1,5,1,19,8,1,10,1,12,1,22,9,1,1,1,1,1,3,1,
        26,8,1,1,2,1,2,1,2,5,2,31,8,2,10,2,12,2,34,9,2,1,2,1,2,5,2,38,8,
        2,10,2,12,2,41,9,2,3,2,43,8,2,1,2,1,2,3,2,47,8,2,1,2,0,0,3,0,2,4,
        0,0,54,0,9,1,0,0,0,2,25,1,0,0,0,4,46,1,0,0,0,6,8,3,2,1,0,7,6,1,0,
        0,0,8,11,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,12,1,0,0,0,11,9,1,0,
        0,0,12,13,5,0,0,1,13,1,1,0,0,0,14,26,5,1,0,0,15,16,5,5,0,0,16,20,
        5,7,0,0,17,19,3,4,2,0,18,17,1,0,0,0,19,22,1,0,0,0,20,18,1,0,0,0,
        20,21,1,0,0,0,21,23,1,0,0,0,22,20,1,0,0,0,23,26,5,6,0,0,24,26,5,
        7,0,0,25,14,1,0,0,0,25,15,1,0,0,0,25,24,1,0,0,0,26,3,1,0,0,0,27,
        47,5,1,0,0,28,32,5,2,0,0,29,31,3,4,2,0,30,29,1,0,0,0,31,34,1,0,0,
        0,32,30,1,0,0,0,32,33,1,0,0,0,33,42,1,0,0,0,34,32,1,0,0,0,35,39,
        5,3,0,0,36,38,3,4,2,0,37,36,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,
        39,40,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,42,35,1,0,0,0,42,43,1,
        0,0,0,43,44,1,0,0,0,44,47,5,4,0,0,45,47,5,7,0,0,46,27,1,0,0,0,46,
        28,1,0,0,0,46,45,1,0,0,0,47,5,1,0,0,0,7,9,20,25,32,39,42,46
    ]

class forthParser ( Parser ):

    grammarFileName = "forth.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'if'", "'else'", "'endif'",
                     "':'", "';'" ]

    symbolicNames = [ "<INVALID>", "NUMBER", "IF", "ELSE", "ENDIF", "COLON",
                      "SEMICOLON", "ID", "COMMENT", "WS", "LEXICAL_ERROR" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_body = 2

    ruleNames =  [ "program", "statement", "body" ]

    EOF = Token.EOF
    NUMBER=1
    IF=2
    ELSE=3
    ENDIF=4
    COLON=5
    SEMICOLON=6
    ID=7
    COMMENT=8
    WS=9
    LEXICAL_ERROR=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(forthParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(forthParser.StatementContext)
            else:
                return self.getTypedRuleContext(forthParser.StatementContext,i)


        def getRuleIndex(self):
            return forthParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = forthParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 162) != 0):
                self.state = 6
                self.statement()
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 12
            self.match(forthParser.EOF)
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


        def getRuleIndex(self):
            return forthParser.RULE_statement


        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PushNumberContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forthParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(forthParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPushNumber" ):
                return visitor.visitPushNumber(self)
            else:
                return visitor.visitChildren(self)


    class CallFuncContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forthParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(forthParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallFunc" ):
                return visitor.visitCallFunc(self)
            else:
                return visitor.visitChildren(self)


    class DefFuncContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forthParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(forthParser.COLON, 0)
        def ID(self):
            return self.getToken(forthParser.ID, 0)
        def SEMICOLON(self):
            return self.getToken(forthParser.SEMICOLON, 0)
        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(forthParser.BodyContext)
            else:
                return self.getTypedRuleContext(forthParser.BodyContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefFunc" ):
                return visitor.visitDefFunc(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = forthParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = forthParser.PushNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.match(forthParser.NUMBER)
                pass
            elif token in [5]:
                localctx = forthParser.DefFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self.match(forthParser.COLON)
                self.state = 16
                self.match(forthParser.ID)
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134) != 0):
                    self.state = 17
                    self.body()
                    self.state = 22
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 23
                self.match(forthParser.SEMICOLON)
                pass
            elif token in [7]:
                localctx = forthParser.CallFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.match(forthParser.ID)
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


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return forthParser.RULE_body


        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ConditionalContext(BodyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forthParser.BodyContext
            super().__init__(parser)
            self._body = None # BodyContext
            self.thenBlock = list() # of BodyContexts
            self.elseBlock = list() # of BodyContexts
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(forthParser.IF, 0)
        def ENDIF(self):
            return self.getToken(forthParser.ENDIF, 0)
        def ELSE(self):
            return self.getToken(forthParser.ELSE, 0)
        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(forthParser.BodyContext)
            else:
                return self.getTypedRuleContext(forthParser.BodyContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)


    class BodyNumberContext(BodyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forthParser.BodyContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(forthParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBodyNumber" ):
                return visitor.visitBodyNumber(self)
            else:
                return visitor.visitChildren(self)


    class BodyCallContext(BodyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forthParser.BodyContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(forthParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBodyCall" ):
                return visitor.visitBodyCall(self)
            else:
                return visitor.visitChildren(self)



    def body(self):

        localctx = forthParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = forthParser.BodyNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.match(forthParser.NUMBER)
                pass
            elif token in [2]:
                localctx = forthParser.ConditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.match(forthParser.IF)
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134) != 0):
                    self.state = 29
                    localctx._body = self.body()
                    localctx.thenBlock.append(localctx._body)
                    self.state = 34
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 35
                    self.match(forthParser.ELSE)
                    self.state = 39
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134) != 0):
                        self.state = 36
                        localctx._body = self.body()
                        localctx.elseBlock.append(localctx._body)
                        self.state = 41
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 44
                self.match(forthParser.ENDIF)
                pass
            elif token in [7]:
                localctx = forthParser.BodyCallContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.match(forthParser.ID)
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
