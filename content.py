from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from iconqrc import *
import os
import sys
import pygame
import random

class Content():
    def __init__(self, parent):
        self._parent = parent
        self._ui = self._parent._ui
        self.label_text = self._ui.label_text
        self.label_pix = self._ui.label_pix
        self.label_w = self.label_pix.width()
        self.label_h = self.label_pix.height()

        # the word in love_control
        self.word = []
        filename_word = self.resource_path(os.path.join("word.txt"))
        with open(filename_word, 'r', encoding="utf-8") as f:
            lines_word = f.readlines()

        for line in lines_word:
            self.word.append(line)

        # the word in heart_control
        self.heart = []
        filename_heart = self.resource_path(os.path.join("heart.txt"))
        with open(filename_heart, 'r', encoding="utf-8") as f:
            lines_heart = f.readlines()

        for line in lines_heart:
            self.heart.append(line)

        self.count_len = len(self.word)+1

    # =======================================================
    # set music
    def music_path(self, real_path):
        if hasattr(sys, "_MEIPASS"):
            base_path = sys._MEIPASS

        else:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, real_path)

    def right_sound(self):
        pygame.init()
        pygame.mixer.init()
        s = pygame.mixer.Sound(self.music_path('music/right.wav'))
        s.play()

    def error_sound(self):
        pygame.init()
        pygame.mixer.init()
        s = pygame.mixer.Sound(self.music_path('music/error.wav'))
        s.play()

    # =======================================================
    # set resource
    def resource_path(self, real_path):
        if hasattr(sys, "_MEIPASS"):
            base_path = sys._MEIPASS

        else:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, real_path)

    # =======================================================
    def home_control(self):
        self._ui.label_text.setText(
            "Happy valentines day !!!!!\n\n使用說明: 請先按 Love Start 開啟愛的回憶! <3 \n再按 Next 接續下一章。")

        image_home_pix = QPixmap(os.path.join(':/pix/home_pix.jpg'))

        width, height = self.image_resize(image_home_pix, self.label_w, self.label_h)
        self._ui.label_pix.setPixmap(image_home_pix)
        self._ui.label_pix.resize(width, height)
        self._ui.label_pix.setScaledContents(True)

    def love_control(self):
        self.label_text.setText(self.word[0])
        image_001 = QPixmap(os.path.join(':/pix/001.jpg'))
        width, height = self.image_resize(image_001, self.label_w, self.label_h)
        self._ui.label_pix.setPixmap(image_001)
        self._ui.label_pix.resize(width, height)
        self._ui.label_pix.setScaledContents(True)

    def next_control(self, count):
        if count >= self.count_len:
            count = self.count_len - 1

        if count < 10:
            image = QPixmap(os.path.join(':/pix/00{}.jpg'.format(count)))

        else:
            image = QPixmap(os.path.join(':/pix/0{}.jpg'.format(count)))

        width, height = self.image_resize(image, self.label_w, self.label_h)
        self._ui.label_pix.setPixmap(image)
        self._ui.label_pix.resize(width, height)
        self._ui.label_pix.setScaledContents(True)
        self._ui.label_text.setText(self.word[count-1])

        return count

    def previous_control(self, count):
        if count < 1:
            count = 1

        if count < 10:
            image = QPixmap(os.path.join(':/pix/00{}.jpg'.format(count)))

        else:
            image = QPixmap(os.path.join(':/pix/0{}.jpg'.format(count)))

        width, height = self.image_resize(image, self.label_w, self.label_h)
        self._ui.label_pix.setPixmap(image)
        self._ui.label_pix.resize(width, height)
        self._ui.label_pix.setScaledContents(True)
        self._ui.label_text.setText(self.word[count - 1])

        return count

    def heart_control(self, count):
        self._ui.label_plot.show()
        self._ui.pushButton_click.setText("Click")
        image = QPixmap(os.path.join(':/pix/love_plot.png'.format(count)))
        width, height = self.image_resize(image, self.label_w, self.label_h)
        self._ui.label_plot.setPixmap(image)
        self._ui.label_plot.resize(width, height)
        self._ui.label_plot.setScaledContents(True)

        self._ui.label_text_2.setText(self.heart[0])

        self._ui.pushButton_click.show()

    def heart_click_control(self, heart, count):
        self._ui.label_plot.show()
        if heart == 0:
            image = QPixmap(os.path.join(':/pix/heart_plot.png'.format(count)))
            width, height = self.image_resize(image, self.label_w, self.label_h)
            self._ui.label_plot.setPixmap(image)
            self._ui.label_plot.resize(width, height)
            self._ui.label_plot.setScaledContents(True)

            self._ui.label_text_2.setText(self.heart[1])
            heart = 1

        else:
            image = QPixmap(os.path.join(':/pix/love_plot.png'.format(count)))
            width, height = self.image_resize(image, self.label_w, self.label_h)
            self._ui.label_plot.setPixmap(image)
            self._ui.label_plot.resize(width, height)
            self._ui.label_plot.setScaledContents(True)

            self._ui.label_text_2.setText(self.heart[2])
            heart = 0

        return heart

    def image_resize(self, image, label_w, label_h):
        image_w = image.width()
        image_h = image.height()

        f1 = label_w / image_w
        f2 = label_h / image_h
        factor = min([f1, f2])
        width = int(image_w * factor)
        height = int(image_h * factor)

        return width, height

    # =======================================================
    # play game
    def play_control(self):
        self._ui.stackedWidget.setCurrentIndex(2)
        self._ui.label_play.setText("遊戲說明:\n\n請按 Start 後，選擇一個幸運數字，\n看看今年的運勢如何 ~~")
        self.enable_pushbutton()

    def start_control(self):
        if self._ui.pushButton_start.text() == "Start":
            self.enable_pushbutton()
            self.play_control()
            self.lucky_number = random.randint(1, 9)
            self._ui.label_play.setText("選擇一個幸運數字吧 ~")
            self._ui.pushButton_start.setText("Again")

        else:
            self.play_control()
            self._ui.pushButton_start.setText("Start")

    def btn_1_control(self):
        if self._ui.pushButton_start.text() == "Again":
            if self.lucky_number == 1:
                self._ui.label_play.setText("恭喜! 猜對囉! 一元復始、萬象更新，\n新的一年錦上添花!!!")
                self.right_sound()

            else:
                self._ui.label_play.setText("再接再厲，幸運數字為 {} 唷~".format(self.lucky_number))
                self.error_sound()

                self.disable_pushbutton()
                self._ui.pushButton_1.setEnabled(True)

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("請先按 Start 再開始遊戲哦!")
            msg.setWindowTitle("嘿~ 提醒你!")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

    def btn_2_control(self):
        if self._ui.pushButton_start.text() == "Again":
            if self.lucky_number == 2:
                self._ui.label_play.setText("恭喜! 猜對囉! 祝福你二龍騰飛，工作順利!!!")
                self.right_sound()

            else:
                self._ui.label_play.setText("再接再厲，幸運數字為 {} 唷~".format(self.lucky_number))
                self.error_sound()

            self.disable_pushbutton()
            self._ui.pushButton_2.setEnabled(True)

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("請先按 Start 再開始遊戲哦!")
            msg.setWindowTitle("嘿~ 提醒你!")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

    def btn_3_control(self):
        if self._ui.pushButton_start.text() == "Again":
            if self.lucky_number == 3:
                self._ui.label_play.setText("恭喜! 猜對囉! 祝福你三陽開泰、諸事順遂!!!")
                self.right_sound()

            else:
                self._ui.label_play.setText("再接再厲，幸運數字為 {} 唷~".format(self.lucky_number))
                self.error_sound()

            self.disable_pushbutton()
            self._ui.pushButton_3.setEnabled(True)

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("請先按 Start 再開始遊戲哦!")
            msg.setWindowTitle("嘿~ 提醒你!")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

    def btn_4_control(self):
        if self._ui.pushButton_start.text() == "Again":
            if self.lucky_number == 4:
                self._ui.label_play.setText("恭喜! 猜對囉! 今年必定會四季平安、身體健康!!!")
                self.right_sound()

            else:
                self._ui.label_play.setText("再接再厲，幸運數字為 {} 唷~".format(self.lucky_number))
                self.error_sound()

            self.disable_pushbutton()
            self._ui.pushButton_4.setEnabled(True)

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("請先按 Start 再開始遊戲哦!")
            msg.setWindowTitle("嘿~ 提醒你!")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

    def btn_5_control(self):
        if self._ui.pushButton_start.text() == "Again":
            if self.lucky_number == 5:
                self._ui.label_play.setText("恭喜! 猜對囉! 今年運勢爆棚、五福臨門!!!")
                self.right_sound()

            else:
                self._ui.label_play.setText("再接再厲，幸運數字為 {} 唷~".format(self.lucky_number))
                self.error_sound()

            self.disable_pushbutton()
            self._ui.pushButton_5.setEnabled(True)

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("請先按 Start 再開始遊戲哦!")
            msg.setWindowTitle("嘿~ 提醒你!")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

    def btn_6_control(self):
        if self._ui.pushButton_start.text() == "Again":
            if self.lucky_number == 6:
                self._ui.label_play.setText("恭喜! 猜對囉! 今年必定六六大順、心想事成!!!")
                self.right_sound()

            else:
                self._ui.label_play.setText("再接再厲，幸運數字為 {} 唷~".format(self.lucky_number))
                self.error_sound()

            self.disable_pushbutton()
            self._ui.pushButton_6.setEnabled(True)

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("請先按 Start 再開始遊戲哦!")
            msg.setWindowTitle("嘿~ 提醒你!")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

    def btn_7_control(self):
        if self._ui.pushButton_start.text() == "Again":
            if self.lucky_number == 7:
                self._ui.label_play.setText("恭喜! 猜對囉! 祝福你七星高照，\n天天都是幸運星!!!")
                self.right_sound()

            else:
                self._ui.label_play.setText("再接再厲，幸運數字為 {} 唷~".format(self.lucky_number))
                self.error_sound()

            self.disable_pushbutton()
            self._ui.pushButton_7.setEnabled(True)

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("請先按 Start 再開始遊戲哦!")
            msg.setWindowTitle("嘿~ 提醒你!")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

    def btn_8_control(self):
        if self._ui.pushButton_start.text() == "Again":
            if self.lucky_number == 8:
                self._ui.label_play.setText("恭喜! 猜對囉! 看來今年會八方來財，\n一起發大財!!!")
                self.right_sound()

            else:
                self._ui.label_play.setText("再接再厲，幸運數字為 {} 唷~".format(self.lucky_number))
                self.error_sound()

            self.disable_pushbutton()
            self._ui.pushButton_8.setEnabled(True)

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("請先按 Start 再開始遊戲哦!")
            msg.setWindowTitle("嘿~ 提醒你!")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

    def btn_9_control(self):
        if self._ui.pushButton_start.text() == "Again":
            if self.lucky_number == 9:
                self._ui.label_play.setText("恭喜! 猜對囉! 我們一定會九九同心、久久同心!!!")
                self.right_sound()

            else:
                self._ui.label_play.setText("再接再厲，幸運數字為 {} 唷~".format(self.lucky_number))
                self.error_sound()

            self.disable_pushbutton()
            self._ui.pushButton_9.setEnabled(True)

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("請先按 Start 再開始遊戲哦!")
            msg.setWindowTitle("嘿~ 提醒你!")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

    def disable_pushbutton(self):
        self._ui.pushButton_1.setEnabled(False)
        self._ui.pushButton_2.setEnabled(False)
        self._ui.pushButton_3.setEnabled(False)
        self._ui.pushButton_4.setEnabled(False)
        self._ui.pushButton_5.setEnabled(False)
        self._ui.pushButton_6.setEnabled(False)
        self._ui.pushButton_7.setEnabled(False)
        self._ui.pushButton_8.setEnabled(False)
        self._ui.pushButton_9.setEnabled(False)

    def enable_pushbutton(self):
        self._ui.pushButton_1.setEnabled(True)
        self._ui.pushButton_2.setEnabled(True)
        self._ui.pushButton_3.setEnabled(True)
        self._ui.pushButton_4.setEnabled(True)
        self._ui.pushButton_5.setEnabled(True)
        self._ui.pushButton_6.setEnabled(True)
        self._ui.pushButton_7.setEnabled(True)
        self._ui.pushButton_8.setEnabled(True)
        self._ui.pushButton_9.setEnabled(True)
