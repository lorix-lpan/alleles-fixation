from allele import Allele
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QApplication,
        QLabel, QGridLayout)

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create grid layout
        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        # Create an intance of the Allele class
        self.alle = Allele()

        lbl1 = QLabel(str(self.alle._freq), self)
        btnCross = QPushButton('Cross', self)

        btnCross.clicked.connect(self.startCrossing)

        self.grid.addWidget(btnCross, 0, 0)
        self.grid.addWidget(lbl1, 2, 0)

        self.setLayout(self.grid)
        self.setGeometry(300, 200, 500, 400)
        self.setWindowTitle('Alleles Fixation Simulation')
        self.show()

    def startCrossing(self):
        if not self.alle._isFixated:
            self.alle.cross()
        self.grid.addWidget(QLabel(str(self.alle._freq),self), 3, 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
