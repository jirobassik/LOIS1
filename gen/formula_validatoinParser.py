# Generated from D:/Programs/PyCharm 2021.3.3/LOIS1\formula_validatoin.g4 by ANTLR 4.11.1
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
        4,1,35,45,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,3,0,20,8,0,1,1,1,1,1,2,1,2,1,3,1,3,3,3,28,
        8,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,
        1,7,0,0,8,0,2,4,6,8,10,12,14,0,3,1,0,32,33,1,0,28,31,1,0,1,26,39,
        0,19,1,0,0,0,2,21,1,0,0,0,4,23,1,0,0,0,6,27,1,0,0,0,8,29,1,0,0,0,
        10,34,1,0,0,0,12,40,1,0,0,0,14,42,1,0,0,0,16,20,3,2,1,0,17,20,3,
        4,2,0,18,20,3,6,3,0,19,16,1,0,0,0,19,17,1,0,0,0,19,18,1,0,0,0,20,
        1,1,0,0,0,21,22,7,0,0,0,22,3,1,0,0,0,23,24,3,14,7,0,24,5,1,0,0,0,
        25,28,3,8,4,0,26,28,3,10,5,0,27,25,1,0,0,0,27,26,1,0,0,0,28,7,1,
        0,0,0,29,30,5,34,0,0,30,31,5,27,0,0,31,32,3,0,0,0,32,33,5,35,0,0,
        33,9,1,0,0,0,34,35,5,34,0,0,35,36,3,0,0,0,36,37,3,12,6,0,37,38,3,
        0,0,0,38,39,5,35,0,0,39,11,1,0,0,0,40,41,7,1,0,0,41,13,1,0,0,0,42,
        43,7,2,0,0,43,15,1,0,0,0,2,19,27
    ]

class formula_validatoinParser ( Parser ):

    grammarFileName = "formula_validatoin.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'A'", "'B'", "'C'", "'D'", "'E'", "'F'", 
                     "'G'", "'H'", "'I'", "'J'", "'K'", "'L'", "'M'", "'N'", 
                     "'O'", "'P'", "'Q'", "'R'", "'S'", "'T'", "'U'", "'V'", 
                     "'W'", "'X'", "'Y'", "'Z'", "'!'", "'/\\'", "'\\/'", 
                     "'->'", "'~'", "'1'", "'0'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NEGATION", 
                      "CONJUNCTION", "DISJUNCTION", "IMPLICATION", "EQUIVALENT", 
                      "LOGIC_ONE", "LOGIC_ZERO", "OPEN_CIR_BRACKET", "CLOSE_CIR_BRACKET" ]

    RULE_formula = 0
    RULE_logic_constant = 1
    RULE_atomic_formula = 2
    RULE_complex_formula = 3
    RULE_unar_complex_formula = 4
    RULE_bin_complex_formula = 5
    RULE_binary_connection = 6
    RULE_upper_alph = 7

    ruleNames =  [ "formula", "logic_constant", "atomic_formula", "complex_formula", 
                   "unar_complex_formula", "bin_complex_formula", "binary_connection", 
                   "upper_alph" ]

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
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    NEGATION=27
    CONJUNCTION=28
    DISJUNCTION=29
    IMPLICATION=30
    EQUIVALENT=31
    LOGIC_ONE=32
    LOGIC_ZERO=33
    OPEN_CIR_BRACKET=34
    CLOSE_CIR_BRACKET=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logic_constant(self):
            return self.getTypedRuleContext(formula_validatoinParser.Logic_constantContext,0)


        def atomic_formula(self):
            return self.getTypedRuleContext(formula_validatoinParser.Atomic_formulaContext,0)


        def complex_formula(self):
            return self.getTypedRuleContext(formula_validatoinParser.Complex_formulaContext,0)


        def getRuleIndex(self):
            return formula_validatoinParser.RULE_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormula" ):
                listener.enterFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormula" ):
                listener.exitFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormula" ):
                return visitor.visitFormula(self)
            else:
                return visitor.visitChildren(self)




    def formula(self):

        localctx = formula_validatoinParser.FormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_formula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32, 33]:
                self.state = 16
                self.logic_constant()
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]:
                self.state = 17
                self.atomic_formula()
                pass
            elif token in [34]:
                self.state = 18
                self.complex_formula()
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


    class Logic_constantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOGIC_ZERO(self):
            return self.getToken(formula_validatoinParser.LOGIC_ZERO, 0)

        def LOGIC_ONE(self):
            return self.getToken(formula_validatoinParser.LOGIC_ONE, 0)

        def getRuleIndex(self):
            return formula_validatoinParser.RULE_logic_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_constant" ):
                listener.enterLogic_constant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_constant" ):
                listener.exitLogic_constant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic_constant" ):
                return visitor.visitLogic_constant(self)
            else:
                return visitor.visitChildren(self)




    def logic_constant(self):

        localctx = formula_validatoinParser.Logic_constantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_logic_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            _la = self._input.LA(1)
            if not(_la==32 or _la==33):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atomic_formulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def upper_alph(self):
            return self.getTypedRuleContext(formula_validatoinParser.Upper_alphContext,0)


        def getRuleIndex(self):
            return formula_validatoinParser.RULE_atomic_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomic_formula" ):
                listener.enterAtomic_formula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomic_formula" ):
                listener.exitAtomic_formula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomic_formula" ):
                return visitor.visitAtomic_formula(self)
            else:
                return visitor.visitChildren(self)




    def atomic_formula(self):

        localctx = formula_validatoinParser.Atomic_formulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_atomic_formula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.upper_alph()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Complex_formulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unar_complex_formula(self):
            return self.getTypedRuleContext(formula_validatoinParser.Unar_complex_formulaContext,0)


        def bin_complex_formula(self):
            return self.getTypedRuleContext(formula_validatoinParser.Bin_complex_formulaContext,0)


        def getRuleIndex(self):
            return formula_validatoinParser.RULE_complex_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplex_formula" ):
                listener.enterComplex_formula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplex_formula" ):
                listener.exitComplex_formula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplex_formula" ):
                return visitor.visitComplex_formula(self)
            else:
                return visitor.visitChildren(self)




    def complex_formula(self):

        localctx = formula_validatoinParser.Complex_formulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_complex_formula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 25
                self.unar_complex_formula()
                pass

            elif la_ == 2:
                self.state = 26
                self.bin_complex_formula()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unar_complex_formulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_CIR_BRACKET(self):
            return self.getToken(formula_validatoinParser.OPEN_CIR_BRACKET, 0)

        def NEGATION(self):
            return self.getToken(formula_validatoinParser.NEGATION, 0)

        def formula(self):
            return self.getTypedRuleContext(formula_validatoinParser.FormulaContext,0)


        def CLOSE_CIR_BRACKET(self):
            return self.getToken(formula_validatoinParser.CLOSE_CIR_BRACKET, 0)

        def getRuleIndex(self):
            return formula_validatoinParser.RULE_unar_complex_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnar_complex_formula" ):
                listener.enterUnar_complex_formula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnar_complex_formula" ):
                listener.exitUnar_complex_formula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnar_complex_formula" ):
                return visitor.visitUnar_complex_formula(self)
            else:
                return visitor.visitChildren(self)




    def unar_complex_formula(self):

        localctx = formula_validatoinParser.Unar_complex_formulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_unar_complex_formula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(formula_validatoinParser.OPEN_CIR_BRACKET)
            self.state = 30
            self.match(formula_validatoinParser.NEGATION)
            self.state = 31
            self.formula()
            self.state = 32
            self.match(formula_validatoinParser.CLOSE_CIR_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bin_complex_formulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_CIR_BRACKET(self):
            return self.getToken(formula_validatoinParser.OPEN_CIR_BRACKET, 0)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(formula_validatoinParser.FormulaContext)
            else:
                return self.getTypedRuleContext(formula_validatoinParser.FormulaContext,i)


        def binary_connection(self):
            return self.getTypedRuleContext(formula_validatoinParser.Binary_connectionContext,0)


        def CLOSE_CIR_BRACKET(self):
            return self.getToken(formula_validatoinParser.CLOSE_CIR_BRACKET, 0)

        def getRuleIndex(self):
            return formula_validatoinParser.RULE_bin_complex_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBin_complex_formula" ):
                listener.enterBin_complex_formula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBin_complex_formula" ):
                listener.exitBin_complex_formula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBin_complex_formula" ):
                return visitor.visitBin_complex_formula(self)
            else:
                return visitor.visitChildren(self)




    def bin_complex_formula(self):

        localctx = formula_validatoinParser.Bin_complex_formulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_bin_complex_formula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(formula_validatoinParser.OPEN_CIR_BRACKET)
            self.state = 35
            self.formula()
            self.state = 36
            self.binary_connection()
            self.state = 37
            self.formula()
            self.state = 38
            self.match(formula_validatoinParser.CLOSE_CIR_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Binary_connectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONJUNCTION(self):
            return self.getToken(formula_validatoinParser.CONJUNCTION, 0)

        def DISJUNCTION(self):
            return self.getToken(formula_validatoinParser.DISJUNCTION, 0)

        def IMPLICATION(self):
            return self.getToken(formula_validatoinParser.IMPLICATION, 0)

        def EQUIVALENT(self):
            return self.getToken(formula_validatoinParser.EQUIVALENT, 0)

        def getRuleIndex(self):
            return formula_validatoinParser.RULE_binary_connection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary_connection" ):
                listener.enterBinary_connection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary_connection" ):
                listener.exitBinary_connection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinary_connection" ):
                return visitor.visitBinary_connection(self)
            else:
                return visitor.visitChildren(self)




    def binary_connection(self):

        localctx = formula_validatoinParser.Binary_connectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_binary_connection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 4026531840) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Upper_alphContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return formula_validatoinParser.RULE_upper_alph

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpper_alph" ):
                listener.enterUpper_alph(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpper_alph" ):
                listener.exitUpper_alph(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpper_alph" ):
                return visitor.visitUpper_alph(self)
            else:
                return visitor.visitChildren(self)




    def upper_alph(self):

        localctx = formula_validatoinParser.Upper_alphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_upper_alph)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 134217726) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





