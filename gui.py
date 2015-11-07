from allele import Allele
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QApplication,
        QLabel, QGridLayout, QLineEdit)

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create grid layout
        self.grid = QGridLayout()
        self.le = QLineEdit(self)
        self.le.setReadOnly(True)

        # Create an intance of the Allele class
        self.alle = Allele()

        btnCross = QPushButton('Cross', self)

        # Emitted events
        btnCross.clicked.connect(self.startCrossing)

        self.grid.addWidget(btnCross)
        self.grid.addWidget(self.le)

        # Initiation of the Window
        self.setLayout(self.grid)
        self.setGeometry(300, 200, 500, 400)
        self.setWindowTitle('Alleles Fixation Simulation')
        self.show()

    # Perform crossing on the allele instance and display the updated info
    def startCrossing(self):
        if not self.alle._isFixated:
            self.alle.cross()
            # self.grid.addWidget(QLabel(str(self.text()),self))
            self.le.setText(self.textList()+"   "+self.textFreq())
        else:
            self.le.setText("Finished! Rounds: "+str(self.alle._rounds)+" "+self.textFreq())

    def textList(self):
        return "List: "+" ".join(str(e) for e in self.alle._lst)

    def textFreq(self):
        return "Frequency: "+str(self.alle._freq)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
