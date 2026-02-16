from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtGui import QPainter, QColor, QBrush, QPainterPath


class CustomIcon(QWidget):
    def __init__(self, icon_type="github", color="#FFFFFF", parent=None):
        super().__init__(parent)
        self.icon_type = icon_type
        self.color = QColor(color)
        self.setFixedSize(24, 24)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        if self.icon_type == "github":
            self.draw_github(painter)
        elif self.icon_type == "telegram":
            self.draw_telegram(painter)

    def draw_github(self, painter):
        # Simplified GitHub Logo Drawing using Paths
        path = QPainterPath()
        # Head/Body circle
        path.addEllipse(QRectF(2, 2, 20, 20))

        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QBrush(self.color))
        painter.drawPath(path)

        # Eyes (cutouts)
        painter.setBrush(QBrush(QColor("#1A1A1A")))
        painter.drawEllipse(QRectF(7, 8, 3, 3))
        painter.drawEllipse(QRectF(14, 8, 3, 3))

    def draw_telegram(self, painter):
        # Telegram Paper Plane Logo
        path = QPainterPath()
        path.moveTo(20, 4)
        path.lineTo(4, 11)
        path.lineTo(9, 14)
        path.lineTo(9, 20)
        path.lineTo(12, 16)
        path.lineTo(16, 20)
        path.lineTo(20, 4)
        path.closeSubpath()

        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QBrush(self.color))
        painter.drawPath(path)
