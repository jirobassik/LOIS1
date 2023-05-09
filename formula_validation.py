# Лабораторная работа 1 по дисциплине ЛОИС
# Выполнена студентом группы 021703 БГУИР Озерцом Даниилом Александровичем
# Вариант B, проверить является ли строка формулой логики высказываний.
# Модуль с классом формула
import string
from textwrap import wrap


class Formula:
    def __init__(self, formula):
        self.formula = self.replace_operation(formula)
        self.logic_constant = ('0', '1',)
        self.lat_alph = (
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z',)
        self.negation = '!'
        self.conjunction = '*'
        self.disjunction = '+'
        self.emplication = '@'
        self.equivalent = '~'
        self.open_bracket = '('
        self.close_bracket = ')'
        self.operations = (self.conjunction, self.disjunction, self.emplication, self.equivalent, self.negation,)
        self.operations_for_check = (self.conjunction, self.disjunction, self.emplication, self.equivalent,)

    def find_parens(self) -> dict[int:[int, int]]:
        dict_ind_bracket = {}
        bracket_stack, operation_stack = [], []
        for ind, alph in enumerate(self.formula):
            if alph == '(':
                bracket_stack.append(ind)
                dict_ind_bracket.setdefault(ind, [])
            if alph in self.operations:
                operation_stack.append(ind)
            elif alph == ')':
                try:
                    dict_ind_bracket[bracket_stack.pop()].extend([ind, operation_stack.pop()])
                except IndexError:
                    return False
        if len(bracket_stack) > 0 or len(operation_stack) > 0:
            return False
        return dict_ind_bracket

    def main_validate(self):
        if not self.atomic_formula(self.formula):
            if isinstance(self.find_parens(), dict):
                dict_ind_brackets = self.find_parens()
                if self.main_brackets() and self.check_dict(dict_ind_brackets) \
                        and self.check_num_operation(dict_ind_brackets):
                    check_rule = []
                    for key in dict_ind_brackets:
                        try:
                            ind_operation = dict_ind_brackets[key][1]
                            operation = self.formula[ind_operation]
                            right_alph, left_alph = self.formula[ind_operation + 1], self.formula[ind_operation - 1]
                            right_alph_2, left_alph_2 = self.formula[ind_operation + 2], self.formula[ind_operation - 2]

                            if left_alph == self.open_bracket \
                                    and (right_alph in self.lat_alph or right_alph in self.logic_constant) \
                                    and operation == self.negation:
                                check_rule.append(True)
                                continue

                            if left_alph == self.open_bracket and right_alph == self.open_bracket \
                                    and operation == self.negation:
                                check_rule.append(True)
                                continue

                            if (left_alph in self.lat_alph or left_alph in self.logic_constant) \
                                    and right_alph == self.open_bracket \
                                    and left_alph_2 == self.open_bracket and operation in self.operations_for_check:
                                check_rule.append(True)
                                continue

                            if (right_alph in self.lat_alph or right_alph in self.logic_constant) \
                                    and left_alph == self.close_bracket \
                                    and right_alph_2 == self.close_bracket and operation in self.operations_for_check:
                                check_rule.append(True)
                                continue

                            if (left_alph in self.lat_alph or left_alph in self.logic_constant) \
                                    and (right_alph in self.lat_alph or right_alph in self.logic_constant) \
                                    and right_alph_2 == self.close_bracket and left_alph_2 == self.open_bracket \
                                    and operation in self.operations_for_check:
                                check_rule.append(True)
                                continue

                            if left_alph == self.close_bracket and right_alph == self.open_bracket \
                                    and operation in self.operations_for_check:
                                check_rule.append(True)
                                continue
                        except IndexError:
                            return "Неверный ввод"
                    if len(dict_ind_brackets) != len(check_rule):
                        return "Неверный ввод"
                    else:
                        return "Верный ввод"
                else:
                    return "Неверный ввод"
            else:
                return "Неверный ввод"
        else:
            return "Верный ввод"

    def check_num_operation(self, dict_: dict) -> bool:
        for key in dict_:
            sub_formula = self.formula[key: dict_[key][0] + 1]
            operation = 0
            depth = 0
            for ind, alph in enumerate(sub_formula):
                if alph == self.open_bracket and ind != 0:
                    depth += 1
                if alph == self.close_bracket and ind != len(sub_formula):
                    depth -= 1
                if depth == 0 and alph in self.operations:
                    operation += 1
                if operation > 1:
                    return False
        return True

    def atomic_formula(self, formula: str) -> bool:
        return True if (formula in self.lat_alph or formula in self.logic_constant) and len(formula) == 1 else False

    def main_brackets(self) -> bool:
        return True if self.formula[0] == self.open_bracket and self.formula[-1] == self.close_bracket else False

    def check_empty(self) -> bool:
        return False if self.formula == "" or self.formula.isspace() else True

    @staticmethod
    def check_dict(dict_: dict[int: [int, int]]) -> bool:
        for key in dict_:
            if dict_[key][1] < key or dict_[key][1] > dict_[key][0]:
                return False
        return True

    @staticmethod
    def replace_operation(str_: str) -> str:
        str_ = str_.replace('\/', '+')
        str_ = str_.replace('/\\', '*')
        str_ = str_.replace('->', '@')
        return str_


def split_string(input_string: str) -> list[str]:
    special_chars = ('->', '\/', '/\\',)
    result = []
    current = ""
    count = 0
    while count < len(input_string):
        found_special = False
        for special in special_chars:
            if input_string[count:count + len(special)] == special:
                current += special
                count += len(special)
                found_special = True
                break
        if not found_special:
            current += input_string[count]
            count += 1
        if current != "":
            result.append(current)
            current = ""
    return result

def check_write_symbols(list_symbols: list) -> bool:
    full_oper = ('\\/', '/\\', '->',)
    oper = (*wrap(string.ascii_uppercase, 1), *full_oper, '!', '~', '0', '1', '(', ')',)
    for symbol in list_symbols:
        if symbol not in oper:
            return False
    return True
