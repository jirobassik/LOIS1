# Лабораторная работа 2 по дисциплине ЛОИС
# Выполнена студентом группы 021703 БГУИР Озерцом Даниилом Александровичем
# Вариант 3, проверить является ли формула невыполнимой.
# Модуль вычисления таблицы истинности и проверки, является ли формула невыполнимой
from antlr4 import *
from gen.formula_validatoinLexer import formula_validatoinLexer
from gen.formula_validatoinParser import formula_validatoinParser
from gen.formula_validatoinVisitor import formula_validatoinVisitor
from itertools import product


class FormulaVisitor(formula_validatoinVisitor):
    def __init__(self, truth_values):
        self.truth_values = truth_values
        self.num_op = 0

    def visitFormula(self, ctx: formula_validatoinParser.FormulaContext):
        return self.visitChildren(ctx)

    def visitLogic_constant(self, ctx: formula_validatoinParser.Logic_constantContext):
        return True if str(ctx.LOGIC_ONE()) == str(ctx.getChild(0)) else False

    def visitAtomic_formula(self, ctx: formula_validatoinParser.Atomic_formulaContext):
        p = ctx.getText()
        return self.truth_values[p]

    def visitUnar_complex_formula(self, ctx: formula_validatoinParser.Unar_complex_formulaContext):
        negation = ctx.NEGATION().getText()
        formula = self.visit(ctx.formula())
        if negation == "!":
            return bool(not formula)

    def visitBin_complex_formula(self, ctx: formula_validatoinParser.Bin_complex_formulaContext):
        op = ctx.binary_connection().getText()
        self.num_op += 1
        if self.num_op > 15:
            raise ValueError("Слишком много операций")
        left = self.visit(ctx.formula(0))
        right = self.visit(ctx.formula(1))
        if op == "/\\":
            return bool(left and right)
        elif op == "\\/":
            return bool(left or right)
        elif op == "->":
            return bool((not left) or right)
        elif op == "~":
            return bool(left == right)


class ImpossibleFormula:
    def __init__(self, formula: str):
        self.formula = formula
        self.alphs = self.find_alphs()
        self.len_alphs = len(self.alphs)
        self.list_ = []

    def find_alphs(self) -> set[str]:
        return {alph for alph in self.formula if alph.isalpha()}

    def perm(self):
        return product(range(2), repeat=self.len_alphs)

    def zip_perm(self, tuple_val):
        return dict(zip(self.alphs, tuple_val))

    def find_values(self):
        for tuple_perm in self.perm():
            dict_val = self.zip_perm(tuple_perm)
            res_form = self.validate_formula(dict_val)
            self.list_.append(res_form)

    def formula_imp(self):
        return 'Формула невыполнимая' if all(
            value is False for value in self.list_) else 'Формула не является невыполнимой'

    def validate_formula(self, values):
        input_stream = InputStream(self.formula)
        lexer = formula_validatoinLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = formula_validatoinParser(stream)
        tree = parser.formula()
        visitor = FormulaVisitor(values)
        return visitor.visit(tree)
