from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QFont, QPainter, QColor, QBrush, QPolygon, \
    QLinearGradient
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QFrame
)
from matplotlib.backends.backend_qt5agg import \
    FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class ResultDisplay(QWidget):
    def __init__(self, trans):
        super().__init__()
        self.trans = trans
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        main_layout.setSpacing(15)

        center_layout = QHBoxLayout()
        center_layout.setSpacing(30)

        self.result_label = QLabel("")
        self.result_label.setFont(QFont("Segoe UI", 12))
        self.result_label.setStyleSheet("color: #333;")
        self.result_label.setWordWrap(True)
        self.result_label.setFixedWidth(250)
        center_layout.addWidget(self.result_label,
                                alignment=Qt.AlignmentFlag.AlignTop)

        self.figure = Figure(figsize=(3, 3))
        self.canvas = FigureCanvas(self.figure)
        center_layout.addWidget(self.canvas,
                                alignment=Qt.AlignmentFlag.AlignCenter)

        self.legend_layout = QVBoxLayout()
        self.legend_layout.setSpacing(8)
        center_layout.addLayout(self.legend_layout)

        main_layout.addLayout(center_layout)

        self.score_label = QLabel(self.trans['score'])
        self.score_label.setFont(QFont("Segoe UI", 11, QFont.Weight.Bold))
        self.score_label.setStyleSheet("color: #333;")
        self.score_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        main_layout.addWidget(self.score_label)

        self.score_bar = ScoreBar()
        main_layout.addWidget(self.score_bar)

    def set_results(self, label, proba, score):
        result_text = (
            f"<b>{self.trans['result']}</b><br><br>"
            f"<b>{self.trans['sentiment']}</b> {label}"
        )
        self.result_label.setText(result_text)
        self.score_bar.set_score(score)
        self._plot_pie_chart(proba)

    def _plot_pie_chart(self, proba):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        labels = [self.trans['negative'], self.trans['neutral'],
                  self.trans['positive']]
        colors = ['#ff6f61', '#fdd835', '#66bb6a']

        ax.pie(proba, startangle=140, colors=colors,
               wedgeprops=dict(width=0.4))
        ax.axis('equal')
        self.canvas.draw()

        self._update_legend(proba, labels, colors)

    def _update_legend(self, proba, labels, colors):
        self._clear_layout(self.legend_layout)
        combined = sorted(zip(proba, labels, colors), key=lambda x: -x[0])
        for p, label, color in combined:
            row = QHBoxLayout()

            percent_label = QLabel(f"{p * 100:.1f}%")
            percent_label.setFont(QFont("Segoe UI", 11))
            percent_label.setFixedWidth(60)
            row.addWidget(percent_label)

            color_box = QFrame()
            color_box.setFixedSize(20, 20)
            color_box.setStyleSheet(f"background-color: {color}; "
                                    f"border-radius: 3px;")
            row.addWidget(color_box)

            text_label = QLabel(label)
            text_label.setFont(QFont("Segoe UI", 11))
            row.addWidget(text_label)

            self.legend_layout.addLayout(row)

    def _clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            elif item.layout():
                self._clear_layout(item.layout())


class ScoreBar(QWidget):
    def __init__(self):
        super().__init__()
        self.score = 0.0
        self.setMinimumHeight(80)
        self.setMaximumHeight(100)

    def set_score(self, score):
        self.score = max(-1, min(1, score))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = self.rect().adjusted(30, 30, -30, -20)

        gradient = QLinearGradient(rect.left(), 0, rect.right(), 0)
        gradient.setColorAt(0, QColor(255, 80, 80))
        gradient.setColorAt(0.5, QColor(255, 255, 100))
        gradient.setColorAt(1, QColor(100, 220, 100))

        painter.setBrush(QBrush(gradient))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(rect, 5, 5)

        painter.setPen(QColor(30, 30, 30))
        painter.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        score_text = f"{self.score:+.2f}"
        text_rect = painter.fontMetrics().boundingRect(score_text)
        text_x = (rect.left() + (self.score + 1) / 2 * rect.width() -
                  text_rect.width() / 2)
        text_y = rect.top() - 15
        painter.drawText(int(text_x), int(text_y), score_text)

        pointer_x = rect.left() + (self.score + 1) / 2 * rect.width()
        triangle = QPolygon([
            QPoint(int(pointer_x), rect.bottom() + 6),
            QPoint(int(pointer_x) - 6, rect.bottom() - 10),
            QPoint(int(pointer_x) + 6, rect.bottom() - 10)
        ])
        painter.setBrush(QColor(30, 30, 30))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawPolygon(triangle)
