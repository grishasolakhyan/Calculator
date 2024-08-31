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
        self.button_pi = btn_object.number_button(164, 163, 40, 40, 'btn pi', cw)
        self.button_e = btn_object.number_button(205, 163, 40, 40, 'btn e', cw)

        self.button_dot = btn_object.number_button(0, 204, 40, 40, 'btn dot', cw)
        self.button_bracket1 = btn_object.number_button(164, 204, 40, 40, 'btn bracket 1', cw)
        self.button_bracket2 = btn_object.number_button(205, 204, 40, 40, 'btn bracket 2', cw)

        self.button_plus = btn_object.number_button(123, 40, 40, 40, 'btn plus', cw)
        self.button_minus = btn_object.number_button(123, 81, 40, 40, 'btn minus', cw)
        self.button_multy = btn_object.number_button(123, 122, 40, 40, 'btn multy', cw)
        self.button_divid = btn_object.number_button(123, 163, 40, 40, 'btn divid', cw)
        self.button_degree = btn_object.number_button(123, 204, 40, 40, 'btn degree', cw)

        self.button_equal = btn_object.number_button(41, 163, 81, 40, 'btn equal', cw)
        self.button_clean = btn_object.number_button(41, 204, 81, 40, 'btn clean', cw)

        self.button_sqrt = btn_object.number_button(164, 40, 40, 40, 'btn sqrt', cw)
        self.button_factorial = btn_object.number_button(205, 40, 40, 40, 'btn factorial', cw)

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
        self.button_pi.setText(_translate("MainWindow", "π"))
        self.button_e.setText(_translate("MainWindow", "e"))

        self.button_dot.setText(_translate("MainWindow", "."))
        self.button_bracket1.setText(_translate("MainWindow", "("))
        self.button_bracket2.setText(_translate("MainWindow", ")"))

        self.button_plus.setText(_translate("MainWindow", "+"))
        self.button_minus.setText(_translate("MainWindow", "-"))
        self.button_multy.setText(_translate("MainWindow", "*"))
        self.button_divid.setText(_translate("MainWindow", "/"))
        self.button_degree.setText(_translate("MainWindow", "^"))

        self.button_equal.setText(_translate("MainWindow", "="))
        self.button_clean.setText(_translate("MainWindow", "C"))

        self.button_sqrt.setText(_translate("MainWondow", "√"))
        self.button_factorial.setText(_translate("MainWondow", "!"))

    def add_functions(self):
        self.button_1.clicked.connect(lambda: self.main_clicked_method(self.button_1.text()))
        self.button_2.clicked.connect(lambda: self.main_clicked_method(self.button_2.text()))
        self.button_3.clicked.connect(lambda: self.main_clicked_method(self.button_3.text()))
        self.button_4.clicked.connect(lambda: self.main_clicked_method(self.button_4.text()))
        self.button_5.clicked.connect(lambda: self.main_clicked_method(self.button_5.text()))
        self.button_6.clicked.connect(lambda: self.main_clicked_method(self.button_6.text()))
        self.button_7.clicked.connect(lambda: self.main_clicked_method(self.button_7.text()))
        self.button_8.clicked.connect(lambda: self.main_clicked_method(self.button_8.text()))
        self.button_9.clicked.connect(lambda: self.main_clicked_method(self.button_9.text()))
        self.button_0.clicked.connect(lambda: self.main_clicked_method(self.button_0.text()))
        self.button_pi.clicked.connect(lambda: self.main_clicked_method(self.button_pi.text()))
        self.button_e.clicked.connect(lambda: self.main_clicked_method(self.button_e.text()))

        self.button_bracket1.clicked.connect(lambda: self.main_clicked_method(self.button_bracket1.text()))
        self.button_bracket2.clicked.connect(lambda: self.main_clicked_method(self.button_bracket2.text()))

        self.button_plus.clicked.connect(lambda: self.main_clicked_method(self.button_plus.text()))
        self.button_minus.clicked.connect(lambda: self.main_clicked_method(self.button_minus.text()))
        self.button_multy.clicked.connect(lambda: self.main_clicked_method(self.button_multy.text()))
        self.button_divid.clicked.connect(lambda: self.main_clicked_method(self.button_divid.text()))
        self.button_degree.clicked.connect(lambda: self.main_clicked_method(self.button_degree.text()))
        self.button_dot.clicked.connect(lambda: self.main_clicked_method(self.button_dot.text()))

        self.button_sqrt.clicked.connect(lambda: self.main_clicked_method(self.button_sqrt.text()))
        self.button_factorial.clicked.connect(lambda: self.main_clicked_method(self.button_factorial.text()))

        self.button_equal.clicked.connect(self.results)
        self.button_clean.clicked.connect(self.clean_results)

    def main_clicked_method(self, value):
        self.write_label_string(value) # функция отвечающая за написание строки в label
        return 0

    def write_label_string(self, val):
        lbl_str = self.label_result.text()
        symbol_pattern = ['+', '-', '/', '*', '^', '.']
        if lbl_str == '':
            self.label_result.setText(self.label_result.text() + val)
        elif lbl_str != '':
            if lbl_str[-1] in symbol_pattern and val in symbol_pattern:
                lbl_str = lbl_str[:-1] + val
                self.label_result.setText(lbl_str)
            elif lbl_str == 'Error':
                self.label_result.setText(val)
            else:
                self.label_result.setText(self.label_result.text() + val)
        return 0

    def collection_of_values(self, label_str):
        if label_str == 'Error':
            raise IncorrectExpression()
        l_list = list(label_str)
        print(f'{l_list} - original list')  # вывод первоначального списка из строки
        len_l_list = len(l_list)
        if len(l_list) == 0: # если строка пустая
            raise EmptyLabelString()

        while True:
            flag1 = True
            len_l_list = len(l_list)
            for i in range(len_l_list - 1): # перебор списка строки выражения по индексу
                if (l_list[i].isdigit() == True and l_list[i + 1].isdigit() == True) or \
                        ('.' in l_list[i] and l_list[i + 1].isdigit() == True) or \
                        (l_list[i].isdigit() == True and '.' in l_list[
                            i + 1]):  # если два элемента списка подряд идут числа, точка и число или число и точка
                    l_list[i] += l_list[i + 1] # добавление соседнего символа из следующего в текущий элемент списка
                    l_list.pop(i + 1) # удаление следующего элемента
                    flag1 = True
                    break
                else:
                    flag1 = False
                    continue
            len_l_list = len(l_list)

            if len_l_list == 1:
                flag1 = False

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
        print(f'{l_list} - new list') # вывод готового текстового списка

        return l_list

    def num_pi_and_e_detection(self, num_list):
        if 'π' in num_list or 'e' in num_list:
            len_num_list = len(num_list)
            for i in range(len_num_list):
                if num_list[i] == 'π':
                    num_list[i] = math.pi
                if num_list[i] == 'e':
                    num_list[i] = math.e
            print(f'{num_list}')
        return num_list

    def calculation(self, num_list):
        if num_list[0] == '*' or \
            num_list[-1] == '*' or \
            num_list[0] == '/' or \
            num_list[-1] == '/' or \
            num_list[0] == '^' or \
            num_list[-1] == '^' or \
            num_list[-1] == '√':
            raise IncorrectExpression()
        num_list = self.num_pi_and_e_detection(num_list)


        while True:
            opened_bracket_count = 0
            closed_bracket_count = 0

            opened_bracket_i = 0
            closed_bracket_i = 0

            if '(' in num_list or ')' in num_list: # поиск скобок и выражения внутри них
                len_num_list = len(num_list)
                for i in range(len_num_list): # проверка на кол-во открытых и закрытых скобок
                    if num_list[i] == '(':
                        opened_bracket_count += 1
                    if num_list[i] == ')':
                        closed_bracket_count += 1
                if opened_bracket_count != closed_bracket_count:
                    raise IncorrectExpression()
                else:
                    for i in range(len_num_list - 1):
                        if (num_list[i] == '(' and num_list[i + 1] == ')') or (num_list[i] == ')' and num_list[i + 1] == '('):  # проверка на корректное указание скобок
                            raise IncorrectExpression()


                for i in range(len_num_list):
                    if num_list[i] == '(':
                        opened_bracket_i = i
                for i in range(len_num_list-1, 0, -1):
                    if num_list[i] == ')':
                        closed_bracket_i = i
                n_list = num_list[opened_bracket_i + 1: closed_bracket_i]
            else:
                n_list = num_list

            len_n_list = len(n_list)
            for i in range(len_n_list - 1):
                if self.isnumeric(n_list[i]) == True and self.isnumeric(n_list[i + 1]) == True:
                    raise IncorrectExpression()


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

                elif '√' in n_list:
                    if n_list[i] == '√' and self.isnumeric(n_list[i + 1]) == True:
                        n_list[i] = math.sqrt(n_list[i + 1])
                        n_list.pop(i+1)
                        break
                    else:
                        # raise  IncorrectExpression()
                        continue

                elif '!' in n_list:
                    if self.isnumeric(n_list[i]) == True and n_list[i + 1] == '!':
                        num_x = n_list[i]
                        if num_x < 0:
                            raise IncorrectExpression()
                        else:
                            if num_x%1 != 0:
                                raise IncorrectExpression()
                            else:
                                num_x = int(num_x)
                                n_list[i] = math.factorial(num_x)
                                n_list.pop(i + 1)
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

                elif '+' in n_list or '-' in n_list: # если есть + или -
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
            label_str = self.label_result.text()
            num_list = self.collection_of_values(label_str)
            result = self.calculation(num_list)
            print(f'Result = {result}')
            self.label_result.setText(str(result))
        except EmptyLabelString:
            print(f'ERROR: EmptyLabelString')
            self.label_result.setText('Error')
        except IncorrectExpression:
            print(f'ERROR: IncorrectExpression')
            self.label_result.setText('Error')
        except ZeroDivisionError:
            print(f'ERROR: ZeroDivisionError')
            self.label_result.setText('Error')
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())