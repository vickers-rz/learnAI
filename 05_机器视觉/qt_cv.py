import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QSize

class ImageWindow(QWidget):
    def __init__(self, img_cv):
        super().__init__()

        self.img_cv = img_cv
        h, w, _ = img_cv.shape
        self.aspect_ratio = w / h   # 固定比例

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.update_image(w, h)

    def update_image(self, w, h):
        # 保持比例 resize
        new_h = h
        new_w = int(new_h * self.aspect_ratio)

        img_resized = cv2.resize(self.img_cv, (new_w, new_h))

        # BGR → RGB
        rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb.shape
        bytes_per_line = ch * w

        qimg = QImage(rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.label.setPixmap(QPixmap.fromImage(qimg))

    def resizeEvent(self, event):
        # 窗口缩放时保持宽高比
        w = self.width()
        h = int(w / self.aspect_ratio)
        self.resize(w, h)
        self.update_image(w, h)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    img = cv2.imread("test.jpg")
    win = ImageWindow(img)
    win.setWindowTitle("PyQt + OpenCV 固定比例窗口")
    win.show()

    sys.exit(app.exec_())
