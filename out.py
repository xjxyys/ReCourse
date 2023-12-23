# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'out.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import shutil

class Ui_MainWindow(object):


    def chose_file_path(self):
        self.pathdir = QtWidgets.QFileDialog.getExistingDirectory(None,"选择文件位置")

    def next_p(self):
        if self.ind + 1 <=self.rang:
            self.ind += 1
            self.ranking.setText(str(self.ind))
            self.out_ima.setPixmap(QtGui.QPixmap(".\\out\\"+self.outlist[self.ind-1]).scaled(654,1132))
    def prev_p(self):
        if self.ind -1 >= 1:
            self.ind -= 1
            self.ranking.setText(str(self.ind))
            self.out_ima.setPixmap(QtGui.QPixmap(".\\out\\"+self.outlist[self.ind-1]).scaled(654,1132))
    def save_image(self):
        shutil.copy(".\\out\\"+self.outlist[self.ind-1],self.pathdir+"\\"+self.outlist[self.ind-1])
    def setupUi(self, MainWindow):
        self.ind = 1
        self.pathdir = os.path.dirname(__file__)
        self.outlist = os.listdir(r'.\out')
        self.rang = len(self.outlist)
        MainWindow.setObjectName("MainWindow")
        screen_resolution = QtWidgets.QApplication.desktop().screenGeometry()
        width, height = min(screen_resolution.width() - 100,1000), min(screen_resolution.height() - 100,1200)
        MainWindow.resize(width, height)
        self.display = QtWidgets.QScrollArea(MainWindow)
        self.display.setWidgetResizable(True)
        #self.display.setGeometry(QtCore.QRect(0, 0, 500, 600))
        self.display.setMinimumSize(width,height)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.display.setWidget(self.centralwidget)
        self.centralwidget.setMinimumSize(QtCore.QSize(1000, 1200))
        self.prev_page = QtWidgets.QPushButton(self.centralwidget)
        self.prev_page.setGeometry(QtCore.QRect(20, 1160, 81, 31))
        self.prev_page.setObjectName("prev_page")
        self.next_page = QtWidgets.QPushButton(self.centralwidget)
        self.next_page.setGeometry(QtCore.QRect(880, 1160, 81, 31))
        self.next_page.setObjectName("next_page")
        self.output_im = QtWidgets.QPushButton(self.centralwidget)
        self.output_im.setGeometry(QtCore.QRect(880, 510, 91, 41))
        self.output_im.setObjectName("output_im")
        self.choose_pos = QtWidgets.QPushButton(self.centralwidget)
        self.choose_pos.setGeometry(QtCore.QRect(880, 450, 91, 41))
        self.choose_pos.setObjectName("choose_pos")
        self.out_ima = QtWidgets.QLabel(self.centralwidget)
        self.out_ima.setGeometry(QtCore.QRect(190, 20,654,1132))
        self.out_ima.setText("")
        self.out_ima.setPixmap(QtGui.QPixmap("out\\output1.png").scaled(654,1132))
        self.out_ima.setObjectName("out_ima")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 480, 91, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 0, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.ranking = QtWidgets.QLabel(self.centralwidget)
        self.ranking.setGeometry(QtCore.QRect(570, 0, 54, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ranking.setFont(font)
        self.ranking.setObjectName("ranking")
        #MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.next_page.clicked.connect(self.next_p) # type: ignore
        self.prev_page.clicked.connect(self.prev_p) # type: ignore
        self.choose_pos.clicked.connect(self.chose_file_path) # type: ignore
        self.output_im.clicked.connect(self.save_image) # type: ignore
        self.pushButton_5.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "输出结果 "))
        self.prev_page.setText(_translate("MainWindow", "上一结果"))
        self.next_page.setText(_translate("MainWindow", "下一结果"))
        self.output_im.setText(_translate("MainWindow", "导出为图片"))
        self.choose_pos.setText(_translate("MainWindow", "选择文件位置"))
        self.pushButton_5.setText(_translate("MainWindow", "调整条件"))
        self.label_2.setText(_translate("MainWindow", "排课结果"))
        self.label_3.setText(_translate("MainWindow", "匹配度排名"))
        self.ranking.setText(_translate("MainWindow", "1"))


if __name__ == "__main__":
    import sys
    wd = os.path.dirname(__file__)
    os.chdir(wd)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    sys.exit(app.exec_())
