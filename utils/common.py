
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QBitmap, QPainter
from PyQt5.QtCore  import Qt

# 处理qss文件
def loadqss(style):
    with open(style,"r") as f:
        return f.read()

# 绘制背景
def drawBackground(self, path):
    '''
        QPixmap 类用来绘制图片
            scaled(width, height, aspectRatioMode, transformMode) 设置图片缩放 aspectRatioMode设置长宽比模式
            aspectRatioMode: 
                Qt.KeepAspectRatio 以width和height小的一边保持比例显示 
                Qt.KeepAspectRatioByExpanding 以width和height大的一边保持比例显示 

            scaledToWidth: 指定宽度保持比例显示
            scaledToHeight: 指定高度保持比例显示

            copy(x, y, width, height): 指定起点坐标和宽高裁切图片
    '''
    # 绘制图片
    pixmap = QPixmap(path)
    # 指定图片高度等于窗口高度进行缩放
    pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding)
    # 取图片的中间部分
    widthOffset = (pixmap.width() - self.width())/2
    heightOffset = (pixmap.height() - self.height())/2
    pixmap = pixmap.copy(widthOffset, heightOffset, self.width(), self.height())
    # 调色板
    palette = self.palette() or QPalette()
    # 画刷
    brush = QBrush(pixmap)
    # 将画板画刷设置为背景模式
    palette.setBrush(QPalette.Background, brush)
    self.setPalette(palette)

# 绘制圆角矩形
def drewRadiusRect(self, radiu):
    # QBitmap 单色的像素图，并设置大小
    bitmap = QBitmap(self.size())
    # 填充
    bitmap.fill()
    # 实例画板并制定画板区域
    painter = QPainter(bitmap)
    # 开始绘制
    painter.begin(self)
    # 无边界线的画笔
    painter.setPen(Qt.NoPen)
    # 画刷为黑色
    painter.setBrush(Qt.black)
    # 防止图形走样
    painter.setRenderHint(QPainter.Antialiasing)
    # 在画板上绘制圆角矩形 drawRoundedRect 第一个参数为需要绘制圆角的矩形，第二个参数为圆在x轴的半径，第三个参数为圆在y轴上的半径
    painter.drawRoundedRect(bitmap.rect(), radiu, radiu)
    painter.end()
    self.setMask(bitmap)