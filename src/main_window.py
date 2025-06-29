from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTextEdit, QPushButton,
    QLabel, QSizePolicy
)

from src.i18n import translations
from src.result_display import ResultDisplay
from src.sentiment_model import get_sentiment


class SentimentApp(QWidget):
    def __init__(self, language='en'):
        super().__init__()
        self.trans = translations[language]
        self.setWindowTitle(self.trans['window_title'])
        self.setGeometry(200, 150, 800, 600)
        self.setStyleSheet("background-color: #f4f4f4;")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 20, 30, 20)
        main_layout.setSpacing(15)

        self.title_label = QLabel(self.trans['enter_text'])
        self.title_label.setFont(QFont("Segoe UI", 14))
        self.title_label.setStyleSheet("color: black;")
        main_layout.addWidget(self.title_label,
                              alignment=Qt.AlignmentFlag.AlignLeft)

        self.text_edit = QTextEdit()
        self.text_edit.setFont(QFont("Segoe UI", 12))
        self.text_edit.setSizePolicy(QSizePolicy.Policy.Expanding,
                                     QSizePolicy.Policy.Expanding)
        self.text_edit.setStyleSheet("""
            QTextEdit {
                background-color: white;
                color: black;
                border: 1px solid #ccc;
                border-radius: 8px;
                padding: 8px;
            }
        """)
        main_layout.addWidget(self.text_edit)

        self.analyze_button = QPushButton(self.trans['analyze'])
        self.analyze_button.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        self.analyze_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.analyze_button.clicked.connect(self.analyze_sentiment)
        main_layout.addWidget(self.analyze_button,
                              alignment=Qt.AlignmentFlag.AlignHCenter)

        self.result_display = ResultDisplay(self.trans)
        main_layout.addWidget(self.result_display)
        self.setLayout(main_layout)

    def analyze_sentiment(self):
        text = self.text_edit.toPlainText().strip()
        if not text:
            self.result_display.result_label.setText(
                self.trans['empty_warning'])
            return

        label = get_sentiment(text, 'label')
        proba = get_sentiment(text, 'proba')
        score = get_sentiment(text, 'score')

        self.result_display.set_results(label, proba, score)
