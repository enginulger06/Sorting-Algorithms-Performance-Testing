# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sorting.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import random
import time
import numpy as np
import matplotlib.pyplot as plt
class Ui_Dialog(object):
    def hata(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def kontrol(self):
        self.dizi=self.dizi_uzunluk_input.text()
        durum=False
        if self.dizi=="":
            self.hata('Liste Uzunluk Hata!', 'Lütfen List Length Girişine Tamsayı giriniz...')
        else:
            durum = True
        return durum

    def start(self):
        self.saniye={}
        self.liste=[]
        if self.kontrol() == True:
            for i in range(int(self.dizi)):
                self.liste.append(random.randint(0,i))
            print("Liste     : ",self.liste)
            print("---------------------------------------")
            if self.bubblesort_check()==True:
                bubble_start=time.time()*1000
                self.bubble_algo(self.liste)
                bubble_end=time.time()*1000
                self.saniye['Bubble']=(bubble_end-bubble_start)
            if self.mergesort_check()==True:
                merge_start = time.time()*1000
                merge=self.merge_algo(self.liste)
                print("Merge     : ",merge)
                merge_end = time.time()*1000
                self.saniye['Merge'] = (merge_end - merge_start)

            if self.insertionsort_check()==True:
                insertion_start = time.time()*1000
                self.insertion_algo(self.liste)
                insertion_end = time.time()*1000
                self.saniye['Insertion'] = (insertion_end - insertion_start)
            if self.shellsort_check()==True:
                shell_start = time.time()*1000
                self.shell_algo(self.liste)
                shell_end = time.time()*1000
                self.saniye['Shell'] = (shell_end - shell_start)
            if self.selectionsort_check()==True:
                selection_start = time.time()*1000
                self.selection_algo(self.liste)
                selection_end = time.time()*1000
                self.saniye['Selection'] = (selection_end - selection_start)
        print(self.saniye)
        self.grafik(self.saniye)

    def bubblesort_check(self):
        durum = False
        if self.bubble_check.isChecked():
            durum = True
        return durum
    def mergesort_check(self):
        durum = False
        if self.merge_check.isChecked():
            durum = True
        return durum

    def insertionsort_check(self):
        durum = False
        if self.insertion_check.isChecked():
            durum = True
        return durum
    def shellsort_check(self):
        durum = False
        if self.shell_check.isChecked():
            durum = True
        return durum
    def selectionsort_check(self):
        durum = False
        if self.selection_check.isChecked():
            durum = True
        return durum



    def bubble_algo(self,list):
        # Swap the elements to arrange in order
        for iter_num in range(len(list) - 1, 0, -1):
            for idx in range(iter_num):
                if list[idx] > list[idx + 1]:
                    temp = list[idx]
                    list[idx] = list[idx + 1]
                    list[idx + 1] = temp
        print("Bubble    : ", list)

    def merge_algo(self,unsorted_list):
        if len(unsorted_list) <= 1:
            return unsorted_list
            # Find the middle point and devide it
        middle = len(unsorted_list) // 2
        left_list = unsorted_list[:middle]
        right_list = unsorted_list[middle:]

        left_list = self.merge_algo(left_list)
        right_list = self.merge_algo(right_list)
        return list(self.merge(left_list, right_list))


    # Merge the sorted halves

    def merge(self,left_half, right_half):

        res = []
        while len(left_half) != 0 and len(right_half) != 0:
            if left_half[0] < right_half[0]:
                res.append(left_half[0])
                left_half.remove(left_half[0])
            else:
                res.append(right_half[0])
                right_half.remove(right_half[0])
        if len(left_half) == 0:
            res = res + right_half
        else:
            res = res + left_half
        return res

    def insertion_algo(self,InputList):
        for i in range(1, len(InputList)):
            j = i - 1
            nxt_element = InputList[i]
            # Compare the current element with next one

            while (InputList[j] > nxt_element) and (j >= 0):
                InputList[j + 1] = InputList[j]
                j = j - 1
            InputList[j + 1] = nxt_element
        print("Insertion : ",InputList)

    def shell_algo(self,input_liste):

        gap = int(len(input_liste) / 2)
        while gap > 0:

            for i in range(gap, len(input_liste)):
                temp = input_liste[i]
                j = i
                # Sort the sub list for this gap

                while j >= gap and input_liste[j - gap] > temp:
                    input_liste[j] = input_liste[j - gap]
                    j = j - gap
                input_liste[j] = temp

            # Reduce the gap for the next element

            gap = int(gap / 2)
        print("Shell     : ",input_liste)

    def selection_algo(self,input_list):

        for idx in range(len(input_list)):

            min_idx = idx
            for j in range(idx + 1, len(input_list)):
                if input_list[min_idx] > input_list[j]:
                    min_idx = j
            # Swap the minimum value with the compared value

            input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]
        print("Selection : ", input_list)
    def grafik(self, sozluk):

        objects = []
        performance = []
        for i in sozluk:
            objects.append(i)
            performance.append(sozluk[i])

        y_pos = np.arange(len(objects))


        plt.bar(y_pos, performance, align='center', alpha=0.7)
        plt.xticks(y_pos, objects)
        plt.ylabel('Milliseconds')
        plt.title('Sorting Algorithms Performance Testing')

        plt.show()
    def Temizle(self):
        self.dizi_uzunluk_input.clear()
        self.bubble_check.setChecked(False)
        self.insertion_check.setChecked(False)
        self.selection_check.setChecked(False)
        self.shell_check.setChecked(False)
        self.merge_check.setChecked(False)


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 505)
        Dialog.setStyleSheet("QDialog {\n"
"background-color: rgb(246, 255, 213);\n"
"}\n"
".QLabel {\n"
"font: 8pt \"Comic Sans MS\";\n"
"color: rgb(85, 0, 127);\n"
"}\n"
".QCheckBox{\n"
"background-color: rgb(85, 255, 127);\n"
"}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(290, 50, 91, 31))
        self.label.setObjectName("label")
        self.dizi_uzunluk_input = QtWidgets.QLineEdit(Dialog)
        self.dizi_uzunluk_input.setGeometry(QtCore.QRect(400, 50, 161, 31))
        self.dizi_uzunluk_input.setObjectName("dizi_uzunluk_input")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 150, 691, 121))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEnabled(False)
        self.merge_check = QtWidgets.QCheckBox(Dialog)
        self.merge_check.setGeometry(QtCore.QRect(300, 175, 16, 21))
        self.merge_check.setText("")
        self.merge_check.setObjectName("merge_check")
        self.shell_check = QtWidgets.QCheckBox(Dialog)
        self.shell_check.setGeometry(QtCore.QRect(550, 175, 16, 21))
        self.shell_check.setText("")
        self.shell_check.setObjectName("shell_check")
        self.selection_check = QtWidgets.QCheckBox(Dialog)
        self.selection_check.setGeometry(QtCore.QRect(680, 175, 16, 21))
        self.selection_check.setText("")
        self.selection_check.setObjectName("selection_check")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(520, 210, 91, 31))
        self.label_7.setObjectName("label_7")
        self.insertion_check = QtWidgets.QCheckBox(Dialog)
        self.insertion_check.setGeometry(QtCore.QRect(420, 175, 16, 21))
        self.insertion_check.setText("")
        self.insertion_check.setObjectName("insertion_check")
        self.bubble_check = QtWidgets.QCheckBox(Dialog)
        self.bubble_check.setGeometry(QtCore.QRect(170, 175, 16, 21))
        self.bubble_check.setText("")
        self.bubble_check.setObjectName("bubble_check")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(650, 210, 111, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(140, 210, 91, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(270, 210, 91, 31))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(380, 210, 111, 31))
        self.label_11.setObjectName("label_11")
        self.start_btn = QtWidgets.QPushButton(Dialog)
        self.start_btn.setGeometry(QtCore.QRect(342, 350, 121, 31))
        self.start_btn.setStyleSheet("font: 8pt \"8514oem\";\n"
"")
        self.start_btn.setObjectName("start_btn")
        # butona tıklayınca
        self.start_btn.clicked.connect(self.start)


        self.clear_btn = QtWidgets.QPushButton(Dialog)
        self.clear_btn.setGeometry(QtCore.QRect(460, 350, 121, 31))
        self.clear_btn.setStyleSheet("font: 8pt \"8514oem\";\n"
"")
        self.clear_btn.setObjectName("clear_btn")
        # btn tıklayınca
        self.clear_btn.clicked.connect(self.Temizle)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sorting Algorithms Performance Testing"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt;\">List Length</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Shell Sort</span></p><p><span style=\" font-size:9pt; font-weight:600;\"><br/></span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Selection Sort</span></p><p><span style=\" font-size:9pt; font-weight:600;\"><br/></span></p></body></html>"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Bubble Sort</span></p><p><span style=\" font-size:9pt; font-weight:600;\"><br/></span></p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Merge Sort</span></p><p><span style=\" font-size:9pt; font-weight:600;\"><br/></span></p></body></html>"))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Insertion Sort</span></p><p><span style=\" font-size:9pt; font-weight:600;\"><br/></span></p></body></html>"))
        self.start_btn.setText(_translate("Dialog", "Start Test"))
        self.clear_btn.setText(_translate("Dialog", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

