from PyQt6.QtWidgets import QApplication
from src.main_window import SentimentApp
from src.language_dialog import LanguageDialog


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    dialog = LanguageDialog()
    if dialog.exec():
        language = dialog.language or 'en'
        window = SentimentApp(language)
        window.show()
        sys.exit(app.exec())
