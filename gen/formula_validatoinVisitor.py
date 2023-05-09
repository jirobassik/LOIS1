# Generated from D:/Programs/PyCharm 2021.3.3/LOIS1\formula_validatoin.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .formula_validatoinParser import formula_validatoinParser
else:
    from formula_validatoinParser import formula_validatoinParser

# This class defines a complete generic visitor for a parse tree produced by formula_validatoinParser.

class formula_validatoinVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by formula_validatoinParser#formula.
    def visitFormula(self, ctx:formula_validatoinParser.FormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formula_validatoinParser#logic_constant.
    def visitLogic_constant(self, ctx:formula_validatoinParser.Logic_constantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formula_validatoinParser#atomic_formula.
    def visitAtomic_formula(self, ctx:formula_validatoinParser.Atomic_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formula_validatoinParser#complex_formula.
    def visitComplex_formula(self, ctx:formula_validatoinParser.Complex_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formula_validatoinParser#unar_complex_formula.
    def visitUnar_complex_formula(self, ctx:formula_validatoinParser.Unar_complex_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formula_validatoinParser#bin_complex_formula.
    def visitBin_complex_formula(self, ctx:formula_validatoinParser.Bin_complex_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formula_validatoinParser#binary_connection.
    def visitBinary_connection(self, ctx:formula_validatoinParser.Binary_connectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formula_validatoinParser#upper_alph.
    def visitUpper_alph(self, ctx:formula_validatoinParser.Upper_alphContext):
        return self.visitChildren(ctx)



del formula_validatoinParser