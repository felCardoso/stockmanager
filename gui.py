from PyQt5.QtWidgets import (
    QWidget,
    QGridLayout,
    QTableWidget,
    QHeaderView,
    QToolBar,
    QAction,
    QPushButton,
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class Ui_InventoryManager(QWidget):
    def setup_ui(self, MainWindow):
        MainWindow.setWindowTitle("Gerenciador de Inventário")
        MainWindow.setGeometry(100, 100, 600, 400)
        MainWindow.setWindowFlags(
            MainWindow.windowFlags() & ~Qt.WindowContextHelpButtonHint
        )
        MainWindow.setWindowIcon(QIcon("images/dresser-duotone.png"))

        self.central_widget = QWidget(MainWindow)
        MainWindow.setCentralWidget(self.central_widget)

        self.layout = QGridLayout()
        self.central_widget.setLayout(self.layout)

        self.inventory_tbl = QTableWidget()
        self.inventory_tbl.setColumnCount(3)
        self.inventory_tbl.setHorizontalHeaderLabels(["ID", "Nome", "Qnt."])
        self.inventory_tbl.setEditTriggers(QTableWidget.NoEditTriggers)
        header = self.inventory_tbl.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        self.inventory_tbl.verticalHeader().setVisible(False)
        self.inventory_tbl.setColumnWidth(0, 10)
        self.inventory_tbl.setColumnWidth(2, 10)
        self.inventory_tbl.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.layout.addWidget(self.inventory_tbl, 0, 0, 1, 3)

        self.add_button = QPushButton("Adicionar Produto")
        self.layout.addWidget(self.add_button, 1, 0)

        self.edit_button = QPushButton("Editar Produto")
        self.layout.addWidget(self.edit_button, 1, 1)

        self.setup_toolbar(MainWindow)

    def setup_toolbar(self, MainWindow):
        toolbar = QToolBar("My main toolbar")
        MainWindow.addToolBar(toolbar)

        self.add_product_action = QAction("Adicionar Produto", MainWindow)
        toolbar.addAction(self.add_product_action)

        self.edit_product_action = QAction("Editar Produto", MainWindow)
        toolbar.addAction(self.edit_product_action)

        self.toggle_theme_action = QAction("Toggle Theme", MainWindow)
        toolbar.addAction(self.toggle_theme_action)
