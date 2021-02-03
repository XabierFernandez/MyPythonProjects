from __future__ import division

from PySide2.QtCore import QObject, SIGNAL, SLOT
from PySide2.QtWidgets import QDialog, QTextBrowser, QLineEdit, QApplication, QVBoxLayout
import sys


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Calculate")
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type an arithmetic operation")
        #self.lineedit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()
        self.lineedit.returnPressed.connect(self.updateUi)

    def updateUi(self):
        try:
            text = str(self.lineedit.text())
            self.browser.append("%s = <b>%s</b>" % (text, eval(text)))
        except:
            self.browser.append(
                "<font color=red>%s is invalid!</font>" % text)


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
