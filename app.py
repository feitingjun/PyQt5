import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QSizePolicy
from PyQt5.QtGui import QIcon, QPainter, QBitmap, QPixmap
from PyQt5.QtCore import QSize, Qt, QPoint
from utils.common import loadqss, drawBackground, drewRadiusRect

class MainWin(QWidget):

    _startPos = None

    def __init__(self):
        super().__init__()

        self.initUI()

    # 初始化窗口实例
    def initUI(self):
        # 设置窗口大小
        # self.resize(350, 500)
        # 设置固定窗口大小，不能拉伸
        self.setFixedSize(350, 500)
        # 设置窗口无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 设置窗口标题
        self.setWindowTitle('测试')
        # 设置窗口图标
        icon = QIcon('./assets/11.jpg')
        self.setWindowIcon(icon)
        # 设置窗口id，用以qss id选择器
        self.setObjectName('mainWin')
        # 加载qss文件
        qssStyle = loadqss('app.qss')
        # 设置qss
        self.setStyleSheet(qssStyle)
        self.setColseIcon()
        # 显示窗口
        self.show()

    def setColseIcon(self):
        icon = QIcon('./assets/close.png')
        btn = QPushButton(self)
        btn.setIcon(icon)
        btn.setObjectName('closeBtn')
        size = QSize(15, 15)
        btn.setIconSize(size)
        btn.setCursor(Qt.PointingHandCursor)
        btn.move(self.width() - 30, 0)
        btn.clicked.connect(self.closeWin)

    # 关闭窗口
    def closeWin(self):
        self.close()

    # 绘制圆角矩形
    # def paintEvent(self, e):
    #     drewRadiusRect(self, 10)
        
    # 窗口大小变化时重绘背景
    def resizeEvent(self, e):
       drawBackground( self, './assets/22.jpg')

    # 鼠标移动时
    def mouseMoveEvent(self, e): 
        offset = e.pos() - self._startPos
        self.move(self.pos() + offset)

    # 鼠标按下时
    def mousePressEvent(self, e):
        # 如果点击按钮为鼠标左键
        if e.button() == Qt.LeftButton:
            # 记录开始坐标
            self._startPos = QPoint(e.x(), e.y())

    # 鼠标松开时
    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self._startPos = None
    

if __name__ == '__main__':
    # app实例
    app = QApplication(sys.argv)
    win = MainWin()
    sys.exit(app.exec_())
