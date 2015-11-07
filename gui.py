from allele import Allele
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QApplication,
        QLabel)

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create an intance of the Allele class
        self.alle = Allele()

        lbl1 = QLabel(str(self.alle._freq), self)
        lbl1.move(15, 10)

        self.btn = QPushButton('Cross', self)
        self.btn.move(200,10)

        self.setGeometry(300, 200, 500, 400)
        self.setWindowTitle('Alleles Fixation Simulation')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
