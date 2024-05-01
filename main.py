import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QWidget, QTextEdit
from cryptography import CeaserCipher, VigenereCipher, TablePermutation



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Криптография")
        self.setGeometry(100, 100, 900, 600)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        # Комбобокс для выбора функции
        function_label = QLabel("Выберите метод шифрования:")
        self.function_combo = QComboBox()
        self.function_combo.addItems(["Шифр Цезаря", "Шифр Виженера", "Простая табличная перестановка"])
        # Поле ввода для текста
        input_layout = QHBoxLayout()
        text_label = QLabel("Введите текст:")
        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText("Введите текст здесь...")
        self.text_input.setFixedHeight(100)
        input_layout.addWidget(text_label)
        input_layout.addWidget(self.text_input)
        # Поле ввода для ключа
        input_layout_1 = QHBoxLayout()
        key_label = QLabel("Введите ключ:")
        self.key_input = QLineEdit()
        input_layout_1.addWidget(key_label)
        input_layout_1.addWidget(self.key_input)
        # Создаем горизонтальный layout для кнопок
        button_layout = QHBoxLayout()
        # Кнопка для зашифровки текста
        self.encrypt_button = QPushButton("Зашифроавть")
        self.encrypt_button.clicked.connect(lambda: self.encrypt_text("en"))
        # Кнопка для расшифровки текста
        self.decrypt_button = QPushButton("Расшифроавть")
        self.decrypt_button.clicked.connect(lambda: self.encrypt_text("de"))
        # Добавляем кнопки в горизонтальный layout
        button_layout.addWidget(self.encrypt_button)
        button_layout.addWidget(self.decrypt_button)
        # Поле для вывода результата
        result_label = QLabel("Результат:")
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        main_layout.addWidget(function_label)
        main_layout.addWidget(self.function_combo)
        main_layout.addLayout(input_layout)
        main_layout.addLayout(input_layout_1)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(result_label)
        main_layout.addWidget(self.result_text)


    def encrypt_text(self, crypt):
        text = self.text_input.toPlainText()
        key_data = self.key_input.text()
        crypt_data = crypt
        function_name = self.function_combo.currentText()

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

        self.result_text.setPlainText(result)


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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
