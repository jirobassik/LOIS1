# Лабораторная работа 2 по дисциплине ЛОИС
# Выполнена студентом группы 021703 БГУИР Озерцом Даниилом Александровичем
# Вариант 3, проверить является ли формула невыполнимой.
# Главный модуль запуска

from formula_validation import Formula, check_write_symbols, split_string
from imp_formula import ImpossibleFormula
import time

if __name__ == '__main__':
    print("Ограничение по количеству операциям: 15")
    while True:
        inp_formula = input("Введите формулу: ")
        if check_write_symbols(split_string(inp_formula)):
            formula_checker = Formula(inp_formula)
            if formula_checker.check_empty():
                if formula_checker.main_validate() == 'Верный ввод':
                    start = time.time()
                    try:
                        check_imp = ImpossibleFormula(inp_formula)
                        check_imp.find_values()
                        print(check_imp.formula_imp())
                    except ValueError as error_message:
                        print(error_message)
                    stop = time.time() - start
                    # print(stop)
                else:
                    print("Неверный ввод")
            else:
                print("Неверный ввод")
        else:
            print("Неверный ввод")

# while True:
#     inp_formula = input("Введите формулу: ")
#     # if not valid_formula(inp_formula):
#     start = time.time()
#     check_imp = ImpossibleFormula(inp_formula)
#     check_imp.find_values()
#     print(check_imp.formula_imp())
#     stop = time.time() - start
#     print(stop)
#     # else:
#     #     print("Неверный ввод")



# ((((D->B)\/(Q~W))~F)/\(((T->Y)\/(P~L))~U)) Стресс тест
# Невыполнимые ((P\/(P/\Q))~(!P))  (!(P->(P->(Q~Q))))
# (!(A/\(B/\(C/\(D/\(E/\(F/\(G/\(H/\(I/\(J/\(K/\(L/\(M/\(N/\(O/\(P/\(Q/\(R/\(S/\(T/\Z))))))))))))))))))))) > 15
# (!(A/\(B/\(C/\(D/\(E/\(F/\(G/\(H/\(I/\(J/\(K/\(L/\(M/\(N/\(O/\Z)))))))))))))))) 15