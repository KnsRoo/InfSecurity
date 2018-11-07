from PyQt5 import QtCore, QtWidgets, QtGui, QtSvg
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QPushButton, QFileDialog
from PyQt5.QtCore import QSize, Qt, pyqtSlot, QRect
from PyQt5.uic import loadUi
import numpy as np, random, os, itertools

class Window(QMainWindow):

    @pyqtSlot()
    def on_oldtext_textChanged(self):
        self.radioButton.setChecked(True)
        self.set_property([self.radioButton, self.start, 'enable'])
        self.set_property([self.generate, self.loadfrom, self.loadto, self.hand_mode, 'disable'])
        self.comboBox.clear()
        self.start.setText('Анализ')
        self.progressBar.setValue(0)

    @pyqtSlot()
    def on_radioButton_clicked(self): self.start.setText('Анализ')

    @pyqtSlot()
    def on_radioButton_2_clicked(self): self.start.setText('Преобразовать')

    @pyqtSlot()
    def on_hand_mode_clicked(self):
        self.start.setEnabled(False)
        t = self.comboBox.currentText().split('x')
        self.M, self.pc = (int(t[1]),int(t[0])), 0
        self.grid = self.genmatrix(self.M, self.grid, self.progressBar, nul = True)
        self.createtable()
        self.progressBar.setValue(0)
        lines = self.frame.findChildren(QtWidgets.QPushButton)
        for item in lines:
            item.setStyleSheet(self.get_QPushButton_style())
            item.setEnabled(True)

    def set_property(self, obj):
        target = obj.pop()
        for item in obj:
            if target == 'enable': item.setEnabled(True)
            if target == 'disable': item.setEnabled(False)

    @pyqtSlot()
    def on_clear_set_clicked(self):
        self.grid, self.M = [], (0,0)
        self.radioButton.setChecked(True)
        self.comboBox.clear()
        self.clear_layout()
        self.start.setText('Анализ') 
        self.set_property([self.comboBox, self.start, 'enable'])
        self.set_property([self.generate, self.loadfrom, self.loadto, self.hand_mode, 'disable'])
        self.progressBar.setValue(0)

    @pyqtSlot()
    def on_clmemo_clicked(self):
        self.oldtext.clear(), self.newtext.clear()

    @pyqtSlot()
    def on_swap_clicked(self):
        tmp = self.oldtext.toPlainText()
        self.oldtext.setPlainText(self.newtext.toPlainText())
        self.newtext.setPlainText(tmp)

    @pyqtSlot()
    def on_loadfrom_clicked(self):
        f = QFileDialog.getOpenFileName(self, 'Open file', os.getcwd(),"Key files (*.mrgkey)")
        if f[0] != '':
            with open(f[0],'r') as file:
                x, y, files = list(file.read().split('x'))
                self.M, files = (int(x),int(y)), list(files)
                self.comboBox.clear()
                self.comboBox.addItem(y+'x'+x)
                self.comboBox.setEnabled(False)
                self.grid = np.zeros(self.M)
                self.createtable()
                for index, item in np.ndenumerate(self.grid):
                    self.progressBar.setValue((index[0]*self.M[0]+index[1])/(self.M[0]*self.M[1])*100)
                    self.grid[index[0]][index[1]] = files.pop(0)
                self.progressBar.setValue(100)
            file.close()
            lines = self.frame.findChildren(QtWidgets.QPushButton)
            if int(x)*int(y)<3601:
                for index, item in np.ndenumerate(self.grid):
                    self.progressBar.setValue((index[0]*self.M[0]+index[1])/(self.M[0]*self.M[1])*100)
                    if item == 0: lines[index[0]*self.M[1]+index[1]].setStyleSheet("background-color: green;" "border: none;")
                    self.progressBar.setValue(100)
            if len(self.phrase) == int(x)*int(y): self.start.setEnabled(True)
            else: self.start.setEnabled(False)

    @pyqtSlot()
    def on_loadto_clicked(self):
        f = QFileDialog.getSaveFileName(self, 'Save file', os.getcwd(),"Key files (*.mrgkey)")
        if f[0]!='':
            with open(f[0],'w') as file:
                file.write(str(self.M[0])+'x'+str(self.M[1])+'x')
                for index,item in np.ndenumerate(self.grid):
                    if item != 0: item = 1
                    file.write(str(item))
            file.close()

    @pyqtSlot()
    def on_generate_clicked(self):
        self.M = tuple(reversed(tuple(map(int, self.comboBox.currentText().split('x')))))
        self.grid = self.genmatrix(self.M, self.grid, self.progressBar)
        if self.M[0]*self.M[1]<3601:
            self.createtable()
            lines = self.frame.findChildren(QtWidgets.QPushButton)
            for index, item in enumerate(lines):
                self.progressBar.setValue(index/len(lines)*100)
                item.setStyleSheet("background-color: rgb(205, 1, 1);" "border: none;")
            self.progressBar.setValue(0)
            for index, item in np.ndenumerate(self.grid):
                if item == 0: lines[index[0]*self.M[1]+index[1]].setStyleSheet("background-color: green;" "border: none;")
                self.progressBar.setValue((index[0]*self.M[0]+index[1])/(self.M[0]*self.M[1])*100)
        self.set_property([self.start, self.loadto, 'enable'])
        self.progressBar.setValue(100)

    @pyqtSlot()
    def on_start_clicked(self):
        if self.start.text() == 'Анализ':
            self.start.setEnabled(False)
            self.phrase = self.oldtext.toPlainText()
            self.comboBox.clear()
            self.comboBox.setEnabled(True)
            a = self.getcombobox(self.phrase, self.oldtext)
            self.comboBox.addItems(a)
            if self.radioButton.isChecked() == True:
                if a:
                    self.set_property([self.generate, self.loadfrom, 'enable'])
                    if len(self.phrase)<3601: self.hand_mode.setEnabled(True)
                    self.start.setText('Преобразовать')
            else: self.set_property([self.hand_mode, self.loadfrom, 'enable'])
        elif self.start.text() == 'Преобразовать':
            if self.radioButton.isChecked() == True: self.newtext.setPlainText(self.crypting('encode',self.M, self.grid, self.oldtext.toPlainText()))
            else: self.newtext.setPlainText(self.crypting('decode', self.M, self.grid, self.oldtext.toPlainText()))
            if self.radioButton.isChecked(): self.start.setText('Анализ')

    @pyqtSlot()
    def matrixclick(self, all_disabled = True):
        sender = self.sender()
        sender.setStyleSheet("background-color: green;" "border: none;")
        sender.setEnabled(False)
        x, y = list(map(int, str(sender.objectName).split('_')))
        lines, self.pc, self.grid[x][y] = self.frame.findChildren(QtWidgets.QPushButton), self.pc+1, 0
        m = [str(x)+'_'+str(self.M[1]-y-1), str(self.M[0]-x-1)+'_'+str(y), str(self.M[0]-x-1)+'_'+str(self.M[1]-y-1)]
        self.progressBar.setValue(self.pc/(len(lines)/4)*100)
        for item in lines:
            if item.objectName in m: item.setEnabled(False)
            if item.isEnabled() == True: all_disabled = False
        if all_disabled: self.set_property([self.start, self.loadto, 'enable'])

    def clear_layout(self):
        lines = self.frame.findChildren(QtWidgets.QPushButton)
        for item in lines:
            self.gridLayout.removeWidget(item)
            item.deleteLater()

    def createtable(self):
        self.clear_layout()
        w, h = int(329/self.M[0]), int(329/self.M[1])
        self.frame.setGeometry(QRect(451,221, (h+1)*self.M[1],(w+1)*self.M[0]))
        for index, item in np.ndenumerate(self.grid):
            button = QPushButton('', self)
            button.setFixedSize(h,w)
            button.setEnabled(False)
            button.setStyleSheet("background-color: rgb(205, 1, 1);" "border: none;")
            button.objectName = str(index[0])+'_'+str(index[1])
            button.clicked.connect(self.matrixclick)
            self.gridLayout.addWidget(button, index[0], index[1])

    def preinit(self):
        self.M, self.grid, self.pc = (0,0), [], 0

    def append_(self, phrase):
        return phrase if len(phrase)%4 == 0 else self.append_(phrase+'.')

    def getcombobox(self, phrase, pt):
        phrase = phrase.replace(' ','').replace('\t','').replace('\n','')
        phrase = self.append_(phrase)
        pt.setPlainText(phrase)
        A, ret = [i for i in range(int(len(phrase)/2)+1) if i%2 == 0], []
        for i, j in itertools.product(A,A):
            if i*j == len(phrase): ret.append(str(i)+'x'+str(j)) 
        return ret

    def get_QPushButton_style(self):
        with open('style.css') as style: str = style.read()
        style.close()
        return str

    def __init__(self, f, g):
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(800, 480))    
        loadUi('form.ui',self) 
        self.setWindowTitle("Метод поворотной решетки")
        self.genmatrix, self.crypting = f, g
        self.preinit()
