from PyQt5 import QtCore, QtWidgets, QtGui, QtSvg
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QPushButton, QFileDialog
from PyQt5.QtCore import QSize, Qt, pyqtSlot, QRect
from PyQt5.uic import loadUi
import numpy as np, random

class Window(QMainWindow):
    @pyqtSlot()
    def on_oldtext_textChanged(self):
        self.radioButton.setChecked(True)
        self.generate.setEnabled(False)
        self.loadto.setEnabled(True)
        self.hand_mode.setEnabled(False)
        self.loadfrom.setEnabled(False)
        self.loadto.setEnabled(False)
        self.comboBox.clear()
        self.start.setEnabled(True)
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

    @pyqtSlot()
    def on_clear_set_clicked(self):
        self.grid, self.M = [], (0,0)
        self.comboBox.clear()
        self.comboBox.setEnabled(True)
        self.clear_layout()
        self.radioButton.setChecked(True)
        self.start.setText('Анализ')
        self.start.setEnabled(True)
        self.generate.setEnabled(False)
        self.loadfrom.setEnabled(False)
        self.loadto.setEnabled(False)
        self.hand_mode.setEnabled(False)
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
                files = file.read().split('x')
                x,y = files[0], files[1]
                files = list(files[2])
                self.M = (int(x),int(y))
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
        param = self.comboBox.currentText().split('x')
        param = list(map(int,param))
        self.M = (param[1], param[0])
        self.start.setEnabled(True)
        self.grid = self.genmatrix(self.M, self.grid, self.progressBar)
        if param[1]*param[0]<3601:
            self.createtable()
            lines = self.frame.findChildren(QtWidgets.QPushButton)
            for index, item in enumerate(lines):
                self.progressBar.setValue(index/len(lines)*100)
                item.setStyleSheet("background-color: rgb(205, 1, 1);" "border: none;")
            self.progressBar.setValue(0)
            for index, item in np.ndenumerate(self.grid):
                if item == 0: lines[index[0]*self.M[1]+index[1]].setStyleSheet("background-color: green;" "border: none;")
                self.progressBar.setValue((index[0]*self.M[0]+index[1])/(self.M[0]*self.M[1])*100)
        self.loadto.setEnabled(True)
        self.progressBar.setValue(100)


    @pyqtSlot()
    def on_start_clicked(self):
        if self.start.text() == 'Анализ':
            self.start.setEnabled(False)
            self.phrase = self.oldtext.toPlainText()
            self.comboBox.clear()
            self.comboBox.setEnabled(True)
            a = self.getcombobox(self.phrase, self.oldtext)
            self.comboBox.insertItems(0, a)
            if self.radioButton.isChecked() == True:
                if a:
                    self.generate.setEnabled(True)
                    if len(self.phrase)<3601: self.hand_mode.setEnabled(True)
                    self.loadfrom.setEnabled(True)
                    self.start.setText('Преобразовать')
            else:
                self.hand_mode.setEnabled(True)
                self.loadfrom.setEnabled(True)
        elif self.start.text() == 'Преобразовать':
            if self.radioButton.isChecked() == True: self.newtext.setPlainText(self.crypting('encode',self.M, self.grid, self.oldtext.toPlainText()))
            else: self.newtext.setPlainText(self.crypting('decode', self.M, self.grid, self.oldtext.toPlainText()))
            if self.radioButton.isChecked(): self.start.setText('Анализ')

    @pyqtSlot()
    def matrixclick(self, all_disabled = True):
        sender = self.sender()
        sender.setStyleSheet("background-color: green;" "border: none;")
        self.pc+=1
        sender.setEnabled(False)
        a = str(sender.objectName).split('_')
        x,y = int(a[0]),int(a[1])
        self.grid[x][y] = 0
        R,S,U = [x,self.M[1]-y-1], [self.M[0]-x-1,y],[self.M[0]-x-1,self.M[1]-y-1]
        lines = self.frame.findChildren(QtWidgets.QPushButton)
        self.progressBar.setValue(self.pc/(len(lines)/4)*100)
        for item in lines:
            if item.objectName == str(R[0])+'_'+str(R[1]): item.setEnabled(False)
            if item.objectName == str(S[0])+'_'+str(S[1]): item.setEnabled(False)
            if item.objectName == str(U[0])+'_'+str(U[1]): item.setEnabled(False)
            if item.isEnabled() == True: all_disabled = False
        if all_disabled: 
            self.start.setEnabled(True)
            self.loadto.setEnabled(True)

    def clear_layout(self):
        lines = self.frame.findChildren(QtWidgets.QPushButton)
        for item in lines:
            self.gridLayout.removeWidget(item)
            item.deleteLater()

    def createtable(self):
        self.clear_layout()
        w,h = int(329/self.M[0]),int(329/self.M[1])
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

    def append_(self, phrase, pt):
        phrase+='.'
        pt.setPlainText(phrase)
        if len(phrase)%4 != 0: return self.append_(phrase, pt)
        else: return phrase

    def getcombobox(self, phrase, pt):
        phrase = phrase.replace(' ','').replace('\t','').replace('\n','')
        if len(phrase)%4 != 0: phrase = self.append_(phrase, pt)
        ret, sizeof = [], len(phrase)
        for i in range(sizeof):
            for j in range(sizeof):
                if (i%2==0 and j%2==0):
                    if i*j == sizeof: ret.append(str(j)+'x'+str(i))
        return ret

    def get_QPushButton_style(self):
        with open('style.css') as style:
            str = style.read()
        style.close()
        return str

    def __init__(self,f,g):
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(800, 480))    
        loadUi('form.ui',self) 
        self.setWindowTitle("Метод поворотной решетки")
        self.genmatrix = f
        self.crypting = g
        self.preinit()