from allele import Allele
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QApplication,
        QLabel, QGridLayout, QTextEdit)

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create grid layout
        self.grid = QGridLayout()
        self.textField = QTextEdit(self)
        self.textField.setReadOnly(True)

        btnCross = QPushButton('Cross', self)
        btnStart = QPushButton('Start/Clear', self)

        # Emitted events
        btnCross.clicked.connect(self.startCrossing)
        btnStart.clicked.connect(self.startUp)

        self.grid.addWidget(btnCross,0,0)
        self.grid.addWidget(btnStart,0,1)
        self.grid.addWidget(self.textField,1,0)

        # Initiation of the Window
        self.setLayout(self.grid)
        self.setGeometry(300, 200, 500, 400)
        self.setWindowTitle('Alleles Fixation Simulation')
        self.show()

    # Perform crossing on the allele instance and display the updated info
    def startCrossing(self):
        # If self.alle does not exist, raise an exception
        try:
            self.alle
        except:
            self.textField.append("Please press start to initialize first!")
            return
        if not self.alle._isFixated:
            self.alle.cross()
            # self.grid.addWidget(QLabel(str(self.text()),self))
            self.textField.append(self.textList()+"   "+self.textFreq())
        else:
            self.textField.append("Finished! Rounds: "+str(self.alle._rounds)+" "+self.textFreq())

    def startUp(self):
        # Create an intance of the Allele class
        self.alle = Allele()
        self.textField.clear()
        self.textField.append(self.textList()+"   "+self.textFreq())

    def textList(self):
        return "List: "+" ".join(str(e) for e in self.alle._lst)

    def textFreq(self):
        return "Frequency: "+str(self.alle._freq)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
