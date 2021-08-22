import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main_ui import Ui_Dialog
from iconqrc import *
import pygame

from content import Content

class MyWindow(QMainWindow, QDialog):
    def __init__(self):
        super().__init__()
        self._ui = Ui_Dialog()
        self._ui.setupUi(self)

        self.label_w = self._ui.label_pix.width()
        self.label_h = self._ui.label_pix.height()
        self.content = Content(self)

        # ====================================================
        # set music
        pygame.init()
        print("有音樂哦! 注意聽 ~~~")
        pygame.mixer.init()
        pygame.mixer.music.load(self.music_path("music/main.mp3"))
        pygame.mixer.music.play(-1, 8)

        # ====================================================
        # set icon style
        stylesheet = "QPushButton {background: transparent}"

        self._ui.pushButton_home.setIconSize(QSize(32, 32))
        self._ui.pushButton_home.setIcon(QIcon(':/pix/home.png'))

        self._ui.pushButton_love.setIconSize(QSize(32, 32))
        self._ui.pushButton_love.setIcon(QIcon(':/pix/love.png'))

        self._ui.pushButton_next.setIconSize(QSize(32, 32))
        self._ui.pushButton_next.setIcon(QIcon(':/pix/next.png'))

        self._ui.pushButton_previous.setIconSize(QSize(32, 32))
        self._ui.pushButton_previous.setIcon(QIcon(':/pix/previous.png'))

        self._ui.pushButton_heart.setIconSize(QSize(32, 32))
        self._ui.pushButton_heart.setIcon(QIcon(':/pix/heart.png'))

        self._ui.pushButton_play.setIconSize(QSize(32, 32))
        self._ui.pushButton_play.setIcon(QIcon(':/pix/play.png'))

        self._ui.pushButton_close.setIconSize(QSize(32, 32))
        self._ui.pushButton_close.setIcon(QIcon(':/pix/close.png'))

        self._ui.pushButton_click.setIconSize(QSize(32, 32))
        self._ui.pushButton_click.setIcon(QIcon(':/pix/click.png'))

        self._ui.pushButton_start.setIconSize(QSize(32, 32))
        self._ui.pushButton_start.setIcon(QIcon(':/pix/start.png'))

        self._ui.pushButton_1.setIconSize(QSize(80, 80))
        self._ui.pushButton_1.setIcon(QIcon(':/pix/num_1.png'))
        self._ui.pushButton_1.setStyleSheet(stylesheet)

        self._ui.pushButton_2.setIconSize(QSize(80, 80))
        self._ui.pushButton_2.setIcon(QIcon(':/pix/num_2.png'))
        self._ui.pushButton_2.setStyleSheet(stylesheet)

        self._ui.pushButton_3.setIconSize(QSize(80, 80))
        self._ui.pushButton_3.setIcon(QIcon(':/pix/num_3.png'))
        self._ui.pushButton_3.setStyleSheet(stylesheet)

        self._ui.pushButton_4.setIconSize(QSize(80, 80))
        self._ui.pushButton_4.setIcon(QIcon(':/pix/num_4.png'))
        self._ui.pushButton_4.setStyleSheet(stylesheet)

        self._ui.pushButton_5.setIconSize(QSize(80, 80))
        self._ui.pushButton_5.setIcon(QIcon(':/pix/num_5.png'))
        self._ui.pushButton_5.setStyleSheet(stylesheet)

        self._ui.pushButton_6.setIconSize(QSize(80, 80))
        self._ui.pushButton_6.setIcon(QIcon(':/pix/num_6.png'))
        self._ui.pushButton_6.setStyleSheet(stylesheet)

        self._ui.pushButton_7.setIconSize(QSize(80, 80))
        self._ui.pushButton_7.setIcon(QIcon(':/pix/num_7.png'))
        self._ui.pushButton_7.setStyleSheet(stylesheet)

        self._ui.pushButton_8.setIconSize(QSize(80, 80))
        self._ui.pushButton_8.setIcon(QIcon(':/pix/num_8.png'))
        self._ui.pushButton_8.setStyleSheet(stylesheet)

        self._ui.pushButton_9.setIconSize(QSize(80, 80))
        self._ui.pushButton_9.setIcon(QIcon(':/pix/num_9.png'))
        self._ui.pushButton_9.setStyleSheet(stylesheet)

        # =====================================================
        self.count = 0
        self.on_pushButton_home_clicked()

    # =======================================================
    # set music
    def music_path(self, real_path):
        if hasattr(sys, "_MEIPASS"):
            base_path = sys._MEIPASS

        else:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, real_path)

    # =====================================================
    # content
    @pyqtSlot()
    def on_pushButton_home_clicked(self):
        self._ui.stackedWidget.setCurrentIndex(0)
        self.content.home_control()

    @pyqtSlot()
    def on_pushButton_love_clicked(self):
        self._ui.stackedWidget.setCurrentIndex(0)
        self.content.love_control()
        self.count = 1

    @pyqtSlot()
    def on_pushButton_next_clicked(self):
        self._ui.stackedWidget.setCurrentIndex(0)
        self.count += 1
        count = self.content.next_control(self.count)
        self.count = count

    @pyqtSlot()
    def on_pushButton_previous_clicked(self):
        self._ui.stackedWidget.setCurrentIndex(0)
        self.count -= 1
        count = self.content.previous_control(self.count)
        self.count = count

    @pyqtSlot()
    def on_pushButton_heart_clicked(self):
        message = QMessageBox.question(self, "Reminder", '接下來會有驚喜哦!\n\n 你 準備好了嗎?')
        if message == QMessageBox.Yes:
            self._ui.stackedWidget.setCurrentIndex(1)
            self.content.heart_control(self.count)
            self.heart = 0

    @pyqtSlot()
    def on_pushButton_click_clicked(self):
        heart = self.content.heart_click_control(self.heart, self.count)
        self.heart = heart

    # =====================================================
    # play game
    @pyqtSlot()
    def on_pushButton_play_clicked(self):
        self.content.play_control()

    @pyqtSlot()
    def on_pushButton_start_clicked(self):
        self.content.start_control()

    @pyqtSlot()
    def on_pushButton_1_clicked(self):
        self.content.btn_1_control()

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        self.content.btn_2_control()

    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        self.content.btn_3_control()

    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        self.content.btn_4_control()

    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        self.content.btn_5_control()

    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        self.content.btn_6_control()

    @pyqtSlot()
    def on_pushButton_7_clicked(self):
        self.content.btn_7_control()

    @pyqtSlot()
    def on_pushButton_8_clicked(self):
        self.content.btn_8_control()

    @pyqtSlot()
    def on_pushButton_9_clicked(self):
        self.content.btn_9_control()

    # =====================================================
    @pyqtSlot()
    def on_pushButton_close_clicked(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())