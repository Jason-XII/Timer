from PySide2.QtWidgets import QApplication, QWidget, QDialog, QMessageBox
from PySide2.QtGui import QIcon
from PySide2.QtCore import QTimer
from PySide2.QtMultimedia import QSound
from generated import Ui_Form
from set_generated import Ui_Dialog
from threading import Thread
minute, second = 0, 0
selected = False


class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.set_min, self.ui.set_sec .setMinimum(0)
        self.ui.set_min, self.ui.set_sec .setMaximum(99)
        self.ui.ok.clicked.connect(self.ok)
        self.ui.cancel.clicked.connect(self.no)
        self.select = '倒计时'


    def ok(self):
        global minute, second, selected
        minute, second = self.ui.set_min.value(), self.ui.set_sec.value()
        print(minute, second)
        if minute + second == 0 and self.select == '倒计时':
            QMessageBox.information(self, '提示', '分钟和秒不能为空')
        else:
            widget.change = -1
            widget.method = 'dao'
            widget.time = minute * 60 + second
            widget.ui.min.display(str(minute))
            widget.ui.sec.display(str(second))
            selected = True
            self.hide()

    def no(self):
        global selected
        selected = False
        self.hide()


def handle_set():
    w.show()


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('计时器')
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.handle_timeout)
        self.ui.zheng.setChecked(True)
        self.ui.stop.setEnabled(False)
        self.ui.dao.clicked.connect(handle_set)
        self.ui.start.clicked.connect(self.handle_start)
        self.ui.stop.clicked.connect(self.handle_stop)
        self.ui.zheng.clicked.connect(self.handle_zheng)
        self.ui.setzero.clicked.connect(self.handle_zero)
        self.setWindowIcon(QIcon('clock.gif'))
        self.change = 1
        self.method = 'zheng'
        self.time = 0

    def handle_timeout(self):
        minutes_total = self.time // 60
        seconds = self.time % 60
        self.time += self.change
        self.ui.min.display(str(minutes_total))
        self.ui.sec.display(str(seconds))
        if (minutes_total, seconds) <= (0, 0) and self.method == 'dao':
            self.ui.min.setStyleSheet('color: red; border: none;')
            self.ui.sec.setStyleSheet('color: red; border: none;')
            self.handle_stop()
        elif (minutes_total, seconds) == (0, 3) and self.method == 'dao':
            QSound.play('timer.wav')

    def handle_start(self):
        self.timer.start()
        self.ui.stop.setEnabled(True)
        self.ui.start.setEnabled(False)
        self.ui.min.setStyleSheet('color: green; border: none;')
        self.ui.sec.setStyleSheet('color: green; border: none;')

    def handle_stop(self):
        self.timer.stop()
        self.ui.stop.setEnabled(False)
        self.ui.start.setEnabled(True)
        self.ui.zheng.setChecked(True)
        self.time = 0 if self.method == 'dao' else self.time
        self.change = 1
        self.method = 'zheng'

    def handle_zheng(self):
        self.change = 1

    def handle_zero(self):
        self.time = 0






if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    w = MyDialog()
    app.exec_()
