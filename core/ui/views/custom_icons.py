from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtGui import QPainter, QColor, QBrush, QPainterPath


class CustomIcon(QWidget):
    def __init__(self, icon_type="github", color="#FFFFFF", parent=None):
        super().__init__(parent)
        self.icon_type = icon_type
        self.color = QColor(color)
        self.setFixedSize(20, 20)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        if self.icon_type == "github":
            self.draw_github(painter)
        elif self.icon_type == "telegram":
            self.draw_telegram(painter)

    def draw_github(self, painter):
        # Detailed GitHub "Octocat" head silhouette scaled to 20x20
        path = QPainterPath()

        # Main Head (Ellipse)
        path.addEllipse(QRectF(2, 5, 16, 13))

        # Left Ear
        path.moveTo(4, 6)
        path.lineTo(3, 1)
        path.lineTo(8, 5)

        # Right Ear
        path.moveTo(16, 6)
        path.lineTo(17, 1)
        path.lineTo(12, 5)

        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QBrush(self.color))
        painter.drawPath(path)

        # Eyes (cutouts)
        # Using a dark surfacing color that matches our BASE_BLACK for better visibility
        painter.setBrush(QBrush(QColor("#121212")))
        painter.drawEllipse(QRectF(6, 10, 2.5, 2.5))
        painter.drawEllipse(QRectF(11.5, 10, 2.5, 2.5))

    def draw_telegram(self, painter):
        # Telegram Paper Plane Logo scaled to 20x20
        path = QPainterPath()
        path.moveTo(18, 2)
        path.lineTo(2, 9)
        path.lineTo(7, 12)
        path.lineTo(7, 18)
        path.lineTo(10, 14)
        path.lineTo(14, 18)
        path.lineTo(18, 2)
        path.closeSubpath()

        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QBrush(self.color))
        painter.drawPath(path)
