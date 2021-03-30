import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTableView, QHeaderView, QVBoxLayout
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)

        mainLayout = QVBoxLayout()
        
        df = pd.read_csv("C:\Users\TESstudent\Desktop\IB\Computer Science\python_scraping_demo\espn_ranking.csv")

            

        players = (df.iloc[:,1])
        model = QStandardItemModel(len(players), 1)
        model.setHorizontalHeaderLabels(["Player"])

        for row, player in enumerate(players):
            item = QStandardItem(player)
            model.setItem(row, 0, item)

        filter_proxy_model = QSortFilterProxyModel()
        filter_proxy_model.setSourceModel(model)
        # case sensitive comment out this line
        filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        filter_proxy_model.setFilterKeyColumn(0)

        search_field = QLineEdit()
        search_field.setStyleSheet("font-size: 25px; height 30px")
        search_field.textChanged.connect(filter_proxy_model.setFilterRegExp)
        mainLayout.addWidget(search_field)

        table = QTableView()
        table.setStyleSheet("font-size: 25px")
        table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setModel(filter_proxy_model)
        mainLayout.addWidget(table)

        self.setLayout(mainLayout)


app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())

