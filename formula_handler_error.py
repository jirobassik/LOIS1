from antlr4.error.Errors import InputMismatchException, NoViableAltException
from antlr4.error.ErrorListener import *

class FormulaErrorListener(ErrorListener):
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, type_error):
        red_error = "\033[1;31;20mSyntax error:\033[0m"

        def replace_eof(replace_str: str):
            return replace_str.replace("<EOF>", "empty")

        msg = replace_eof(msg)
        if isinstance(type_error, InputMismatchException):
            expected_tokens = type_error.getExpectedTokens().toString(recognizer.literalNames, recognizer.symbolicNames)
            expected_tokens = replace_eof(expected_tokens)
            ofend_symbol = replace_eof(offendingSymbol.text)
            self.errors.append(line)
            print(f"{red_error} mismatched input '{ofend_symbol}' at line {line}, column {column}. "
                  f"Expected one of the following tokens: {expected_tokens}")
        elif isinstance(type_error, NoViableAltException):
            self.errors.append(line)
            print(f"{red_error} {msg} at line: {line}, column {column}")
        else:
            self.errors.append(line)
            print(f"{red_error} at line {line}, column {column}: {msg}")
        self.underline_error(recognizer, offendingSymbol, line, column)
        print("-" * 50)

    @staticmethod
    def underline_error(recognizer, offendingToken, line, col):
        tokens = recognizer.getInputStream()
        input_str = str(tokens.tokenSource.inputStream)
        lines = input_str.split('\n')
        error_line = lines[line - 1]
        print(error_line)
        print(' ' * col, end='')
        start = offendingToken.start
        stop = offendingToken.stop
        if start >= 0 and stop >= 0:
            if stop < start:
                print('^')
            else:
                num_under = len(range(start, stop + 1))
                print('^' * num_under)
