import sys
from PyQt5.QtWidgets import (
    QWidget, QLineEdit, QLabel, QPushButton, QScrollArea, QMainWindow,
    QApplication, QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy, QCompleter
)
from PyQt5.QtCore import Qt
from customwidgets import OnOffWidget

import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication)

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        container = QWidget()
        containerLayout = QVBoxLayout()
        container.setLayout(containerLayout)

        self.setCentralWidget(container)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())





# class MainWindow(QMainWindow):

#     def __init__(self, *args, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)

#         container = QWidget()
#         containerLayout = QVBoxLayout()
#         container.setLayout(containerLayout)

#         self.setCentralWidget(container)


# app = QApplication(sys.argv)
# w = MainWindow()
# w.show()
# sys.exit(app.exec_())



# from PyQt5 import QtWidgets, uic
# import sys



# class MyUi(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(MyUi, self).__init__()
#         uic.loadUi("demo.ui",self)
#         #your code
#         self.btnAddToList.clicked.connect(self.foo)
#         self.LNINPUT.returnPressed.connect(self.foo)
#         self.show()
    
#     def foo(self):
#         self.MyList.addItem(self.LNINPUT.text())
#         self.LNINPUT.setText("")
# app = QtWidgets.QApplication(sys.argv)
# window = MyUi()
# app.exec_()