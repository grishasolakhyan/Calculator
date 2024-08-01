from PyQt5 import QtCore, QtGui, QtWidgets
import math
import re

class EmptyLabelString(Exception): pass
class IncorrectExpression(Exception): pass
class ZeroDivisionError(Exception): pass

class Buttons:
    def __init__(self):
        pass

    def number_button(self, x, y, a, b, obj_name, cw):
        self.btn = QtWidgets.QPushButton(cw)
        self.btn.setGeometry(QtCore.QRect(x, y, a, b))
        font = QtGui.QFont()

        self.main_window_obj = Ui_MainWindow()

        font.setFamily(self.main_window_obj.btn_font_style())
        font.setPointSize(self.main_window_obj.btn_font_size())
        self.btn.setFont(font)
        self.btn.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(23, 255, 110);")
        self.btn.setObjectName(obj_name)

        return self.btn


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(246, 245)
        MainWindow.setStyleSheet("background-color: rgb(35, 42, 57);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(0, 0, 400, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_result.setObjectName("label_result")

        cw = self.centralwidget
        btn_object = Buttons()

        self.button_1 = btn_object.number_button(0, 122, 40, 40, 'btn 1', cw)
        self.button_2 = btn_object.number_button(41, 122, 40, 40, 'btn 2', cw)
        self.button_3 = btn_object.number_button(82, 122, 40, 40, 'btn 3', cw)
        self.button_4 = btn_object.number_button(0, 81, 40, 40, 'btn 4', cw)
        self.button_5 = btn_object.number_button(41, 81, 40, 40, 'btn 5', cw)
        self.button_6 = btn_object.number_button(82, 81, 40, 40, 'btn 6', cw)
        self.button_7 = btn_object.number_button(0, 40, 40, 40, 'btn 7', cw)
        self.button_8 = btn_object.number_button(41, 40, 40, 40, 'btn 8', cw)
        self.button_9 = btn_object.number_button(82, 40, 40, 40, 'btn 9', cw)
        self.button_0 = btn_object.number_button(0, 163, 40, 40, 'btn 0', cw)

        self.button_plus = btn_object.number_button(123, 40, 40, 40, 'btn plus', cw)
        self.button_minus = btn_object.number_button(123, 81, 40, 40, 'btn minus', cw)
        self.button_multy = btn_object.number_button(123, 122, 40, 40, 'btn multy', cw)
        self.button_divid = btn_object.number_button(123, 163, 40, 40, 'btn divid', cw)
        self.button_dot = btn_object.number_button(0, 204, 40, 40, 'btn dot', cw)
        self.button_degree = btn_object.number_button(123, 204, 40, 40, 'btn degree', cw)
        self.button_bracket1 = btn_object.number_button(164, 204, 40, 40, 'btn bracket 1', cw)
        self.button_bracket2 = btn_object.number_button(205, 204, 40, 40, 'btn bracket 2', cw)

        # self.button_sin = btn_object.number_button(164, 40, 40, 40, 'btn sin', cw)
        # self.button_cos = btn_object.number_button(164, 81, 40, 40, 'btn cos', cw)
        # self.button_tg = btn_object.number_button(164, 122, 40, 40, 'btn tg2', cw)
        # self.button_asin = btn_object.number_button(205, 40, 40, 40, 'btn asin', cw)
        # self.button_acos = btn_object.number_button(205, 81, 40, 40, 'btn acos', cw)
        # self.button_atg = btn_object.number_button(205, 122, 40, 40, 'btn atg', cw)
        #
        # self.button_pi = btn_object.number_button(164, 163, 40, 40, 'btn pi', cw)
        # self.button_e = btn_object.number_button(205, 163, 40, 40, 'btn e', cw)

        self.button_equal = btn_object.number_button(41, 163, 81, 40, 'btn equal', cw)
        self.button_clean = btn_object.number_button(41, 204, 81, 40, 'btn clean', cw)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.label_result.setText(_translate("MainWindow", ""))

        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_0.setText(_translate("MainWindow", "0"))

        self.button_plus.setText(_translate("MainWindow", "+"))
        self.button_minus.setText(_translate("MainWindow", "-"))
        self.button_multy.setText(_translate("MainWindow", "*"))
        self.button_divid.setText(_translate("MainWindow", "/"))
        self.button_dot.setText(_translate("MainWindow", "."))
        self.button_degree.setText(_translate("MainWindow", "^"))
        self.button_bracket1.setText(_translate("MainWindow", "("))
        self.button_bracket2.setText(_translate("MainWindow", ")"))

        # self.button_sin.setText(_translate("MainWindow", "sin"))
        # self.button_cos.setText(_translate("MainWindow", "cos"))
        # self.button_tg.setText(_translate("MainWindow", "tg"))
        # self.button_asin.setText(_translate("MainWindow", "asin"))
        # self.button_acos.setText(_translate("MainWindow", "acos"))
        # self.button_atg.setText(_translate("MainWindow", "atg"))
        #
        # self.button_pi.setText(_translate("MainWindow", "π"))
        # self.button_e.setText(_translate("MainWindow", "e"))

        self.button_equal.setText(_translate("MainWindow", "="))
        self.button_clean.setText(_translate("MainWindow", "C"))

    def add_functions(self):
        self.button_1.clicked.connect(lambda: self.write_number(self.button_1.text()))
        self.button_2.clicked.connect(lambda: self.write_number(self.button_2.text()))
        self.button_3.clicked.connect(lambda: self.write_number(self.button_3.text()))
        self.button_4.clicked.connect(lambda: self.write_number(self.button_4.text()))
        self.button_5.clicked.connect(lambda: self.write_number(self.button_5.text()))
        self.button_6.clicked.connect(lambda: self.write_number(self.button_6.text()))
        self.button_7.clicked.connect(lambda: self.write_number(self.button_7.text()))
        self.button_8.clicked.connect(lambda: self.write_number(self.button_8.text()))
        self.button_9.clicked.connect(lambda: self.write_number(self.button_9.text()))
        self.button_0.clicked.connect(lambda: self.write_number(self.button_0.text()))

        self.button_plus.clicked.connect(lambda: self.write_math_symbol(self.button_plus.text()))
        self.button_minus.clicked.connect(lambda: self.write_math_symbol(self.button_minus.text()))
        self.button_multy.clicked.connect(lambda: self.write_math_symbol(self.button_multy.text()))
        self.button_divid.clicked.connect(lambda: self.write_math_symbol(self.button_divid.text()))

        self.button_dot.clicked.connect(lambda: self.write_number(self.button_dot.text()))
        self.button_degree.clicked.connect(lambda: self.write_number(self.button_degree.text()))
        self.button_bracket1.clicked.connect(lambda: self.write_number(self.button_bracket1.text()))
        self.button_bracket2.clicked.connect(lambda: self.write_number(self.button_bracket2.text()))

        # self.button_sin.clicked.connect(self.btn_sinus)
        # self.button_cos.clicked.connect(self.btn_cosinus)
        # self.button_tg.clicked.connect(self.btn_tangens)
        # self.button_asin.clicked.connect(self.btn_asinus)
        # self.button_acos.clicked.connect(self.btn_acosinus)
        # self.button_atg.clicked.connect(self.btn_atangens)
        #
        # self.button_pi.clicked.connect(self.num_pi)
        # self.button_e.clicked.connect(self.num_e)

        self.button_equal.clicked.connect(self.results)
        self.button_clean.clicked.connect(self.clean_results)

    def write_math_symbol(self, symbol):
        lbl_str = self.label_result.text()
        symbol_pattern = ['+', '-', '/', '*']
        if lbl_str == '':
            self.label_result.setText(self.label_result.text() + symbol)
        elif lbl_str != '':
            lbl_str_list = list(lbl_str)
            if lbl_str_list[-1] in symbol_pattern:
                lbl_str_list[-1] = symbol
                lbl_str = ''.join(lbl_str_list)
                self.label_result.setText(lbl_str)
            else:
                self.label_result.setText(self.label_result.text() + symbol)
        return 0

    def write_number(self, number):
        if self.label_result.text()=="0":
            self.label_result.setText(number)
        else:
            self.label_result.setText(self.label_result.text()+number)

    def collection_of_values(self, l_list):
        len_l_list = len(l_list)
        if len(l_list) == 0: # если строка пустая
            raise EmptyLabelString()

        while True:
            flag1 = True
            len_l_list = len(l_list)
            for i in range(len_l_list - 1):  # перебор списка строки выражения по индексу
                print(f'Iteration #{i + 1}')  # номер итерации

                if (l_list[i].isdigit() == True and l_list[i + 1].isdigit() == True) or \
                        ('.' in l_list[i] and l_list[i + 1].isdigit() == True) or \
                        (l_list[i].isdigit() == True and '.' in l_list[
                            i + 1]):  # если два элемента списка подряд идут числа, точка и число или число и точка
                    print(
                        f'{l_list[i]}[{i}] -> {l_list[i + 1]}[{i + 1}]')  # вывод текущего и следующего элементов
                    l_list[i] += l_list[
                        i + 1]  # добавление соседнего символа из следующего в текущий элемент списка
                    l_list.pop(i + 1)  # удаление следующего элемента
                    print(l_list)
                    flag1 = True  # флаг
                    break

                else:
                    print(
                        f'{l_list[i]}[{i}] -> {l_list[i + 1]}[{i + 1}]')  # вывод текущего и следующего элементов
                    print(l_list)
                    flag1 = False  # флаг
                    continue
            if flag1 == False:
                break

        len_l_list = len(l_list)
        for i in range(len_l_list):  # перебор в списке по индексу
            res = any(chr.isdigit() for chr in l_list[i])  # проверка наличия цифр в элементе
            if res == True:
                if '.' in l_list[i]:  # если есть точка в числовом элементе
                    l_list[i] = float(l_list[i])  # перевод в тип float
                else:
                    l_list[i] = int(l_list[i])  # перевод в тип int
        print(l_list)

        return l_list

    def calculation(self, num_list):
        if num_list[0] == '*' or num_list[0] == '/' or num_list[0] == '^':
            raise IncorrectExpression()
        while True:
            opened_bracket_i = 0
            closed_bracket_i = 0
            if '(' in num_list or ')' in num_list: # поиск скобок и выражения внутри них
                for item in num_list:
                    if item == '(':
                        opened_bracket_i = num_list.index(item)
                for item in reversed(num_list):
                    if item == ')':
                        closed_bracket_i = num_list.index(item)
                n_list = num_list[opened_bracket_i + 1: closed_bracket_i]

                print(f'Opened bracket id = {opened_bracket_i}\nClosed bracket id = {closed_bracket_i}')
                print(f'There is bracket -> {num_list}')
                print(f'Content -> {n_list}')
            else:
                n_list = num_list


            len_n_list = len(n_list)
            if len(num_list) == 1:
                final_result = num_list[0]
                break
            for i in range(len_n_list - 1):
                if '/' in n_list:  # если есть операция деления
                    if i > 0 and n_list[i] == '/' and self.isnumeric(n_list[i - 1]) == True and self.isnumeric(
                            n_list[i + 1]) == True:
                        print(f'{n_list[i - 1]} / {n_list[i + 1]}')

                        if n_list[i+1] == 0:
                            raise ZeroDivisionError()

                        n_list[i - 1] = n_list[i - 1] / n_list[i + 1]
                        del n_list[i:i + 2]
                        print(n_list)
                        break

                elif '^' in n_list: # если есть операция степени
                    if i > 0 and n_list[i] == '^' and self.isnumeric(n_list[i - 1]) == True and self.isnumeric(
                            n_list[i + 1]) == True:
                        print(f'{n_list[i - 1]} ^ {n_list[i + 1]}')
                        n_list[i - 1] = pow(n_list[i - 1], n_list[i + 1])
                        del n_list[i:i + 2]
                        print(n_list)
                        break

                elif '*' in n_list:  # если есть операция умножения
                    if i > 0 and n_list[i] == '*' and self.isnumeric(n_list[i - 1]) == True and self.isnumeric(
                            n_list[i + 1]) == True:
                        print(f'{n_list[i - 1]} * {n_list[i + 1]}')
                        n_list[i - 1] = n_list[i - 1] * n_list[i + 1]
                        del n_list[i:i + 2]
                        print(n_list)
                        break

                elif '+' in n_list or '-' in n_list:
                    if n_list[0] == '+':
                        n_list[1] = 0 + n_list[1]
                        n_list.pop(0)
                        break
                    elif n_list[0] == '-':
                        n_list[1] = 0 - n_list[1]
                        n_list.pop(0)
                        break
                    else:
                        if i > 0 and n_list[i] == '+' and self.isnumeric(n_list[i - 1]) == True and self.isnumeric(
                                n_list[i + 1]) == True:
                            print(f'{n_list[i - 1]} + {n_list[i + 1]}')
                            n_list[i - 1] = n_list[i - 1] + n_list[i + 1]
                            del n_list[i:i + 2]
                            print(n_list)
                            break

                        elif i > 0 and n_list[i] == '-' and self.isnumeric(n_list[i - 1]) == True and self.isnumeric(
                                n_list[i + 1]) == True:
                            print(f'{n_list[i - 1]} - {n_list[i + 1]}')
                            n_list[i - 1] = n_list[i - 1] - n_list[i + 1]
                            del n_list[i:i + 2]
                            print(n_list)
                            break
                else:
                    print(n_list)
                    continue
            num_list[opened_bracket_i] = n_list[0]
            del num_list[opened_bracket_i+1:closed_bracket_i+1]

        return final_result

    def results(self):
        try:
            label_str = self.label_result.text()  # получение строки выражения из label
            print(f'{label_str} - {type(label_str)}')  # вывод строки выражения из label
            label_list = list(label_str)  # перевод строки в список символов
            print(label_list)
            num_list = self.collection_of_values(label_list)
            result = self.calculation(num_list)
            print(f'Result = {result}')
        except EmptyLabelString:
            print(f'ERROR: EmptyLabelString')
        except IncorrectExpression:
            print(f'ERROR: IncorrectExpression')
        except ZeroDivisionError:
            print(f'ERROR: ZeroDivisionError')
        return 0

    def isnumeric(self, obj): # функция проверки на тип(числовой) объекта
        try:
            obj + 0
            return True
        except:
            return False

    def clean_results(self): # функция отчистки строки
        self.label_result.setText("")

    def btn_font_style(self):
        b_fnt_stl="Arial"
        return b_fnt_stl

    def btn_font_size(self):
        b_fnt_sze=12
        return b_fnt_sze

    def num_pi(self):
        self.label_result.setText(str(math.pi))

    def num_e(self):
        self.label_result.setText(str(math.e))

    def btn_sinus(self):
        pp=self.label_result.text()
        if self.label_result.text()=="0":
            self.label_result.setText("math.sin(")
        elif pp[-1]=="+" or pp[-1]=="-" or pp[-1]=="*" or pp[-1]=="/":
            self.label_result.setText(self.label_result.text()+"math.sin(")

    def btn_cosinus(self):
        pp=self.label_result.text()
        if self.label_result.text()=="0":
            self.label_result.setText("math.cos(")
        elif pp[-1]=="+" or pp[-1]=="-" or pp[-1]=="*" or pp[-1]=="/":
            self.label_result.setText(self.label_result.text()+"math.cos(")

    def btn_tangens(self):
        pp=self.label_result.text()
        if self.label_result.text()=="0":
            self.label_result.setText("math.tg(")
        elif pp[-1]=="+" or pp[-1]=="-" or pp[-1]=="*" or pp[-1]=="/":
            self.label_result.setText(self.label_result.text()+"math.tg(")

    def btn_asinus(self):
        pp=self.label_result.text()
        if self.label_result.text()=="0":
            self.label_result.setText("math.asin(")
        elif pp[-1]=="+" or pp[-1]=="-" or pp[-1]=="*" or pp[-1]=="/":
            self.label_result.setText(self.label_result.text()+"math.asin(")

    def btn_acosinus(self):
        pp=self.label_result.text()
        if self.label_result.text()=="0":
            self.label_result.setText("math.acos(")
        elif pp[-1]=="+" or pp[-1]=="-" or pp[-1]=="*" or pp[-1]=="/":
            self.label_result.setText(self.label_result.text()+"math.acos(")

    def btn_atangens(self):
        pp=self.label_result.text()
        if self.label_result.text()=="0":
            self.label_result.setText("math.atg(")
        elif pp[-1]=="+" or pp[-1]=="-" or pp[-1]=="*" or pp[-1]=="/":
            self.label_result.setText(self.label_result.text()+"math.atg(")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())