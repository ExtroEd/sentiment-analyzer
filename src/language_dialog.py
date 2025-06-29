from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class LanguageDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Choose Language")
        self.setFixedSize(300, 200)
        self.setStyleSheet("background-color: #f0f0f0;")

        self.language = None

        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        button_style = """
            QPushButton {
                background-color: #2D89EF;
                color: white;
                border: none;
                padding: 12px;
                font-size: 14px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #1B5CB3;
            }
        """

        self.en_btn = QPushButton("English")
        self.en_btn.setStyleSheet(button_style)
        self.en_btn.setFont(QFont("Segoe UI", 11))
        self.en_btn.clicked.connect(lambda: self.set_language('en'))

        self.ru_btn = QPushButton("Русский")
        self.ru_btn.setStyleSheet(button_style)
        self.ru_btn.setFont(QFont("Segoe UI", 11))
        self.ru_btn.clicked.connect(lambda: self.set_language('ru'))

        layout.addWidget(self.en_btn)
        layout.addWidget(self.ru_btn)

        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

    def set_language(self, lang_code):
        self.language = lang_code
        self.accept()
