from autoPickCard import *
from PyQt5.QtWidgets import QApplication
import sys,os
from PickCardLayout import Ui_Dialog
from PyQt5.QtWidgets import QMainWindow,QMessageBox,QHeaderView
from dotenv import load_dotenv
class PickCardView(QMainWindow,Ui_Dialog):
    def __init__(self, parent=None):
        load_dotenv()
        super(PickCardView, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('PIG OUT')

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        Dialog.setFixedSize(301, 320)
        self.onWorkBtn.clicked.connect(self.onWorkPick)
        self.outWorkBtn.clicked.connect(self.outWorkPick)
        self.onWorkbuBtn.clicked.connect(self.onWorkbu)
        self.outWorkbuBtn.clicked.connect(self.outWorkbu)

    def retranslateUi(self, Dialog):
        super().retranslateUi(Dialog)
        self.nameEdt.setText(os.getenv("NAME"))
        self.passwordEdt.setText(os.getenv("PASS"))
        self.bures.setText("忘了")

    def onWorkPick(self):
        loginStatus = AutoLogin(self.nameEdt.text().replace(" ", ""), self.passwordEdt.text().replace(" ", ""))
        if loginStatus:
            onWork()

    def outWorkPick(self):
        loginStatus = AutoLogin(self.nameEdt.text().replace(" ", ""),self.passwordEdt.text().replace(" ", ""))
        if loginStatus:
            outWork()

    def onWorkbu(self):
        loginStatus = AutoLogin(self.nameEdt.text().replace(" ", ""), self.passwordEdt.text().replace(" ", ""))
        if loginStatus:
            onWorkBu(self.budate.text(),self.bures.text())
    def outWorkbu(self):
        loginStatus = AutoLogin(self.nameEdt.text().replace(" ", ""), self.passwordEdt.text().replace(" ", ""))
        if loginStatus:
            outWorkBu(self.budate.text(), self.bures.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PickCardView()
    window.show()
    sys.exit(app.exec_())

