# Лабораторная работа 1 по дисциплине ЛОИС
# Выполнена студентом группы 021703 БГУИР Озерцом Даниилом Александровичем
# Вариант B, проверить является ли строка формулой логики высказываний.
# Главный модуль запуска

from formula_validation import Formula

while True:
    inp_formula = input("Введите формулу: ")
    a = Formula(inp_formula)
    a.main_validate()
    print("Верный ввод")