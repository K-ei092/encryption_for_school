from PyQt6 import QtCore, QtGui, QtWidgets
from cryptography import CeaserCipher, VigenereCipher, TablePermutation
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(646, 450)
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QWidget#centralwidget {border-image: url(\"./img_1_1.jpg\") 0 0 0 0 stretch stretch};")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.label_encryption_method = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_encryption_method.setGeometry(QtCore.QRect(0, 0, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_encryption_method.setFont(font)
        self.label_encryption_method.setStyleSheet("color: rgb(85, 255, 255);")
        self.label_encryption_method.setLineWidth(1)
        self.label_encryption_method.setObjectName("label_encryption_method")
        self.encrypt_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.encrypt_Button.setGeometry(QtCore.QRect(140, 389, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.encrypt_Button.setFont(font)
        self.encrypt_Button.setStyleSheet("background-color: rgb(103, 218, 180);")
        self.encrypt_Button.setAutoRepeat(False)
        self.encrypt_Button.setAutoDefault(False)
        self.encrypt_Button.setObjectName("encrypt_Button")
        self.decrypt_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.decrypt_Button.setGeometry(QtCore.QRect(330, 389, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.decrypt_Button.setFont(font)
        self.decrypt_Button.setStyleSheet("background-color: rgb(189, 200, 137);")
        self.decrypt_Button.setObjectName("decrypt_Button")
        self.label_input_key = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_input_key.setGeometry(QtCore.QRect(0, 40, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_input_key.setFont(font)
        self.label_input_key.setStyleSheet("color: rgb(85, 255, 255);")
        self.label_input_key.setLineWidth(1)
        self.label_input_key.setObjectName("label_input_key")
        self.label_result = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(0, 230, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("color: rgb(85, 255, 255);")
        self.label_result.setLineWidth(1)
        self.label_result.setObjectName("label_result")
        self.textEdit_input_text = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_input_text.setGeometry(QtCore.QRect(20, 130, 611, 101))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(False)
        font.setWeight(50)
        self.textEdit_input_text.setFont(font)
        self.textEdit_input_text.setObjectName("textEdit_input_text")
        self.textEdit_result = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_result.setGeometry(QtCore.QRect(20, 280, 611, 105))
        self.textEdit_result.setFont(font)
        self.textEdit_result.setObjectName("textEdit_result")
        self.textEdit_input_key = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_input_key.setGeometry(QtCore.QRect(310, 50, 321, 31))
        self.textEdit_input_key.setFont(font)
        self.textEdit_input_key.setObjectName("textEdit_input_key")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(310, 10, 321, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_input_text = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_input_text.setGeometry(QtCore.QRect(0, 90, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_input_text.setFont(font)
        self.label_input_text.setStyleSheet("color: rgb(85, 255, 255);")
        self.label_input_text.setLineWidth(1)
        self.label_input_text.setObjectName("label_input_text")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_fuctions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Криптография"))
        self.label_encryption_method.setText(_translate("MainWindow", "     Выберите метод шифрования:"))
        self.encrypt_Button.setText(_translate("MainWindow", "Зашифровать"))
        self.decrypt_Button.setText(_translate("MainWindow", "Расшифровать"))
        self.label_input_key.setText(_translate("MainWindow", "     Введите ключ:"))
        self.label_result.setText(_translate("MainWindow", "     Результат:"))
        self.textEdit_input_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_result.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_input_key.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Простая табличная перестановка"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Шифр Виженера"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Шифр Цезаря"))
        self.label_input_text.setText(_translate("MainWindow", "     Введите текст:"))

    def add_fuctions(self):
        self.encrypt_Button.clicked.connect(lambda: self.encrypt_text("en"))
        self.decrypt_Button.clicked.connect(lambda: self.encrypt_text("de"))

    def encrypt_text(self, crypt):
        text = self.textEdit_input_text.toPlainText()
        key_data = self.textEdit_input_key.toPlainText()
        crypt_data = crypt
        function_name = self.comboBox.currentText()

        if function_name == "Шифр Цезаря":
            try:
                key = int(key_data)
                result = self.ceaser_cipher(text=text, step=key, crypt=crypt_data)
            except ValueError:
                result = "Ошибка: ключ должен быть числом"
        elif function_name == "Шифр Виженера":
            try:
                key = key_data
                result = self.vigenere_cipher(text=text, key=key, crypt=crypt_data)
            except ValueError:
                result = "Ошибка ввода"
        else:
            try:
                key = int(key_data)
                result = self.table_permutation(text=text, key=key, crypt=crypt_data)
            except ValueError:
                result = "Ошибка: ключ должен быть числом"

        self.textEdit_result.setPlainText(result)


    def ceaser_cipher(self, text: str, step: int, crypt: str = 'en'):
        if crypt == 'en':
            ceaser = CeaserCipher(message=text, step=step)
            return ceaser.encrypt()
        elif crypt == 'de':
            ceaser = CeaserCipher(message=text, step=step)
            return ceaser.decrypt()


    def vigenere_cipher(self, text: str, key: str, crypt: str = 'en'):
        if crypt == 'en':
            vigenere = VigenereCipher(message=text, key=key)
            return vigenere.encrypt()
        elif crypt == 'de':
            vigenere = VigenereCipher(message=text, key=key)
            return vigenere.decrypt()


    def table_permutation(self, text: str, key: int, crypt: str = 'en'):
        if crypt == 'en':
            table = TablePermutation(message=text, key=key)
            return table.encrypt()
        elif crypt == 'de':
            table = TablePermutation(message=text, key=key)
            return table.decrypt()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
