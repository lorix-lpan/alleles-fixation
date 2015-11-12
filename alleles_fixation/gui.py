from alleles_fixation.allele import Allele
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QGridLayout,
        QTextEdit, QMessageBox)

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

        self.messageBox = QMessageBox()
        self.messageBox.setGeometry(400,400,300,300)

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
            self.textField.append(self.textList()+"   "+self.textFreq()+" "+self.alle._letters)
        else:
            self.showMessageWindow()

    def showMessageWindow(self):
        self.messageBox.setText("Limit reached!\n"+"Generations: "+str(self.alle._generations))
        self.messageBox.show()


    def startUp(self):
        # Create an intance of the Allele class
        self.alle = Allele()
        self.textField.clear()
        self.textField.append(self.textList()+"   "+self.textFreq()+" "+self.alle._letters)

# Returned texts

    def textList(self):
        return "List: "+" ".join(str(e) for e in self.alle._lst)

    def textFreq(self):
        return "% of A: "+str(self.alle._freq)


# Run the program
def run():
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
